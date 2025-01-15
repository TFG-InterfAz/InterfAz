from django.shortcuts import render
from django.http import JsonResponse
from transformers import AutoModelForCausalLM, AutoTokenizer
from accelerate import infer_auto_device_map
from .form import PromptForm

# Model checkpoint
checkpoint = "gpt2"

# Globals for the model and tokenizer
MODEL = None
TOKENIZER = None

def load_model_and_tokenizer():
    global MODEL, TOKENIZER

    try:
        # Initialize tokenizer
        TOKENIZER = AutoTokenizer.from_pretrained(checkpoint)

        # Generate a device map for disk offloading
        model_temp = AutoModelForCausalLM.from_pretrained(checkpoint, low_cpu_mem_usage=True)
        device_map = infer_auto_device_map(
            model_temp,
            max_memory={"cpu": "6GB"}  # Adjust memory as needed for your system
        )

        # Load the model with the device map
        MODEL = AutoModelForCausalLM.from_pretrained(
            checkpoint,
            device_map=device_map,
            low_cpu_mem_usage=True
        )

        print("Model and tokenizer loaded successfully with disk offloading.")
    except Exception as e:
        print("Error loading model or tokenizer:", e)
        TOKENIZER, MODEL = None, None

# Ensure the model and tokenizer are loaded at server start
load_model_and_tokenizer()

def prompt_view(request):
    response = None

    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['description']
            try:
                # Generate text
                inputs = TOKENIZER(prompt, return_tensors="pt")
                outputs = MODEL.generate(**inputs, max_length=1000)
                response = TOKENIZER.decode(outputs[0], skip_special_tokens=True)
                print("AI Response:", response)  # Debugging: Check the full response

            except Exception as e:
                response = f"Error generating response: {e}"
    else:
        form = PromptForm()

    return render(request, "generate_code.html", {"form": form, "response": response})
