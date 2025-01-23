from django.shortcuts import render
from InterfAz.models import Prompt
from .form import PromptForm
from .ollama_service import get_ollama_response

def ollama(request):
    form = PromptForm()
    response = None

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt_instance = form.save(commit=False)
            prompt_instance.ai = Prompt.AI.OLLAMA  # Automatically set AI type to Ollama
            
            # Get the response from Ollama service
            prompt_instance.response = get_ollama_response(prompt_instance.request)
            
            prompt_instance.save()
            response = prompt_instance.response

    return render(request, 'ollama.html', {'form': form, 'response': response})

# View to display stored prompts filtered by AI type
def prompts_list(request):
    prompts = Prompt.objects.filter(ai=Prompt.AI.OLLAMA)  # Filter only Ollama prompts
    return render(request, 'prompts_list.html', {'data': prompts})
