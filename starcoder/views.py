from django.shortcuts import render
from django.http import JsonResponse
from transformers import AutoModelForCausalLM, AutoTokenizer
from accelerate import infer_auto_device_map
from starcoder.form import PromptForm
from starcoder.models import Prompt
# Model checkpoint
checkpoint = "gpt2-medium"  # Use a capable model; upgrade if possible.

# Globals for the model and tokenizer
MODEL = None
TOKENIZER = None

def load_model_and_tokenizer():
    global MODEL, TOKENIZER

    try:
        # Initialize tokenizer
        TOKENIZER = AutoTokenizer.from_pretrained(checkpoint)

        # Generate a device map for memory optimization
        model_temp = AutoModelForCausalLM.from_pretrained(checkpoint, low_cpu_mem_usage=True)
        device_map = infer_auto_device_map(
            model_temp,
            max_memory={"cpu": "6GB"}  # Adjust based on your system memory
        )

        # Load the model with the device map
        MODEL = AutoModelForCausalLM.from_pretrained(
            checkpoint,
            device_map=device_map,
            low_cpu_mem_usage=True
        )

        print("Model and tokenizer loaded successfully.")
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
            prompt_entry = Prompt.objects.create(request=prompt)
            try:
                # Generate text with better generation parameters
                inputs = TOKENIZER(prompt, return_tensors="pt")
                outputs = MODEL.generate(
                    inputs.input_ids,
                    max_length=300,  # Limit the output length
                    temperature=0.7,  # Balance randomness and determinism
                    top_k=50,         # Top-k sampling for variety
                    top_p=0.9,        # Nucleus sampling for quality
                    repetition_penalty=1.2  # Penalize repetitive content
                )
                response_raw = TOKENIZER.decode(outputs[0], skip_special_tokens=True)

                # Post-process the response to ensure valid HTML
                lines = response_raw.splitlines()
                cleaned_lines = []
                for line in lines:
                    cleaned_lines.append(line)
                    if line.strip() == "</html>":  # Stop at the closing HTML tag
                        break
                response = "\n".join(cleaned_lines)

                prompt_entry.response = response
                prompt_entry.save()

            except Exception as e:
                response = f"Error generating response: {e}"
    else:
        form = PromptForm()

    return render(request, "generate_code.html", {"form": form, "response": response})


def show_prompts(request):
    prompts = Prompt.objects.all()

    return render(request, "show_all_promps.html", {"data": prompts})