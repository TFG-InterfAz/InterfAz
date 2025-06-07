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


def show_generated_html(request, html_id):
    # Retrieve the saved HTML using its ID
    try:
        html_instance = Generated_Html.objects.get(id=html_id)
        allowed_tags = ['html', 'head', 'title', 'meta', 'body', 'style','form', 'input', 'label', 'select', 'option', 'button',
        'table', 'thead', 'tbody', 'tr', 'th', 'td','div', 'span', 'p', 'b', 'i', 'u', 'br', 'h1', 'h2','nav', 'header','section', 
        'article', 'main', 'aside', 'footer', 'script']
        allowed_attrs = {'*': ['class', 'id', 'name', 'type', 'value', 'placeholder', 'style']
}
        cleaned_html = bleach.clean(html_instance.html_code, tags=allowed_tags,attributes=allowed_attrs, strip=True)
        return render(request, "display_html.html", {"html_code": cleaned_html})
    except Generated_Html.DoesNotExist:
        return render(request, "404.html")
    

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