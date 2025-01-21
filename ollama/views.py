from django.shortcuts import render
from .ollama_service import get_ollama_response
from .form import PromptForm

def ollama(request):
    response = None
    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['description']
            response = get_ollama_response(prompt)
    else:
        form = PromptForm()

    return render(request, 'ollama.html', {'form': form, 'response': response})
