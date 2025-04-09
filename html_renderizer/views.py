from django.shortcuts import render
from .form import Generated_Html_Form
from .models import Generated_Html

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


def show_generated_html(request, html_id):
    # Retrieve the saved HTML using its ID
    try:
        html_instance = Generated_Html.objects.get(id=html_id)
        return render(request, "display_html.html", {"html_code": html_instance.html_code})
    except Generated_Html.DoesNotExist:
        return render(request, "404.html")