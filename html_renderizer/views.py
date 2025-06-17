from django.shortcuts import render,get_object_or_404
from .form import Generated_Html_Form
from .models import Generated_Html
from django.db.models import Q

import bleach

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .form import Generated_Html_Form
from .models import Generated_Html
import re

def normalize_inline_scripts(html_code):
    pattern = re.compile(
        r"""<script>\s*document\.addEventListener\(\s*['"]DOMContentLoaded['"]\s*,\s*function\s*\(\)\s*\{(.*?)\}\s*\);?\s*</script>""",
        re.DOTALL
    )

    def replacer(match):
        script_body = match.group(1).strip()
        return f"<script>(function(){{\n{script_body}\n}})();</script>"

    return pattern.sub(replacer, html_code)


def generate_html_view(request):
    response = None
    response_id = None  # Inicializar la variable para evitar el error

    if request.method == "POST":
        form = Generated_Html_Form(request.POST)
        if form.is_valid():
            instance = form.save()  # Guardamos el formulario
            response = instance.html_code  # Código HTML generado
            response_id = instance.id  # ID del objeto guardado
            
            return redirect('show_generated_html', html_id=response_id)  # Redirige a la vista con el id del HTML generado
    else:
        form = Generated_Html_Form()

    return render(request, "generate_code.html", {"form": form, "response": response, "response_id": response_id})


def show_generated_html(request, html_id):
    try:
        html_instance = Generated_Html.objects.get(id=html_id)
        original_html = html_instance.html_code

        # 1. Extraer y eliminar scripts antes de limpiar
        script_pattern = re.compile(r"<script.*?>.*?</script>", re.DOTALL | re.IGNORECASE)
        script_blocks = script_pattern.findall(original_html)
        html_without_scripts = script_pattern.sub('', original_html)

        # 2. Limpiar el HTML sin scripts
        allowed_tags = [
            'html', 'head', 'title', 'meta', 'body', 'style', 'form', 'input', 'label', 'select', 'option', 'button',
            'table', 'thead', 'tbody', 'tr', 'th', 'td', 'div', 'span', 'p', 'b', 'i', 'u', 'br', 'h1', 'h2',
            'nav', 'header', 'section', 'article', 'main', 'aside', 'footer', 'textarea', 'script', 'li', 'ul', 'a',
            'svg', 'polyline', 'line', 'circle', 'text', 'canvas'
        ]
        allowed_attrs = {
            '*': [
                'class', 'id', 'name', 'type', 'value', 'placeholder', 'style', 'data-text',
                'x', 'y', 'cx', 'cy', 'r', 'width', 'height', 'viewBox',
                'stroke', 'stroke-width', 'fill', 'points', 'transform', 'text-anchor'
            ]
        }

        html_cleaned = bleach.clean(
            html_without_scripts,
            tags=allowed_tags,
            attributes=allowed_attrs,
            strip=True
        )

        # 3. Normalizar y reinyectar los scripts al final
        scripts_normalized = [normalize_inline_scripts(script) for script in script_blocks]
        html_final = html_cleaned + "\n" + "\n".join(scripts_normalized)

        return render(request, "display_html.html", {"html_code": html_final})

    except Generated_Html.DoesNotExist:
        return render(request, "404.html")
    
    
def get_all_html(request):
    query    = request.GET.get('q', '')
    ai_filter= request.GET.get('ai', '')

    qs = Generated_Html.objects.all()

    if query:
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(prompt__icontains=query)
        )

    if ai_filter:
        qs = qs.filter(ai=ai_filter)

    return render(request, "show_all_html.html", {
        "data":       qs.distinct(),
        "query":      query,
        "ai_filter":  ai_filter,
        "ai_choices": Generated_Html.AI_selector.choices,
    })


    

def modify_html(request, html_id):
     
    html = get_object_or_404(Generated_Html, id=html_id)

    if request.method == 'POST':
        form = Generated_Html_Form(request.POST, instance=html)
        if form.is_valid():
            form.save()
            return redirect('show_all_html')  
    else:
        form = Generated_Html_Form(instance=html)
        
    return render(request, 'modify_html.html', {'form': form})


def delete_html(request, html_id):
     
    html_instance = get_object_or_404(Generated_Html, id=html_id)
    
    if request.method == "POST":
        html_instance.delete()
        return redirect('show_all_html')  # Redirige a la lista después de borrar

    return render(request, "delete.html", {"html": html_instance})