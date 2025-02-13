import torch as torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import os
import huggingface_hub

# Log in to Hugging Face
hugging_face_token = os.getenv("HUGGING_FACE_TOKEN")
huggingface_hub.login(token=hugging_face_token)

model = "meta-llama/Llama-3.2-1B-Instruct"


if torch.cuda.is_available():
    print(f"*** Using GPU: {torch.cuda.get_device_name()} ***")
else:
    print("*** No GPU available ***")

start_time = time.time()
print(f"Loading tokenizer for {model}...")
tokenizer = AutoTokenizer.from_pretrained(
    model
)
tokenizer.pad_token = tokenizer.eos_token

print(f"Loading model for {model}...")
model = AutoModelForCausalLM.from_pretrained(
    model
)
print("Model loaded")

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Loading model onto {device}")
model.to(device)
print("Model moved to device")
# Prepare the prompt
prompt = "Tell me a 500 word story about a black cat named George"

# Format the prompt according to Llama 2's chat template
formatted_prompt = f"[INST] {prompt} [/INST]"

inputs = tokenizer.encode_plus(
    formatted_prompt,
    add_special_tokens=True,  # Adds special tokens (e.g., [CLS], [SEP])
    return_tensors="pt",  # Return PyTorch tensors
    padding='max_length',  # Pad to a maximum length specified by the model or manually set
    truncation=True,  # Truncate to a maximum length specified by the model or manually set
    max_length=512  # Specify the maximum length
)
print("Tokenization complete")

# Move each tensor in the inputs dictionary to the correct device
inputs = {k: v.to(device) for k, v in inputs.items()}

print("\nGenerating response...")
  
# Generate the response
outputs = model.generate(
    input_ids=inputs['input_ids'],
    attention_mask=inputs['attention_mask'],
    max_length=1000,  # Adjust based on desired length
    temperature=0.7,
    top_p=0.9,
    do_sample=True,
)
# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
# Clean up the response by removing instruction tokens, the original prompt, and extra whitespace
response = response.replace("[INST]", "").replace("[/INST]", "").strip()
response = response.replace(prompt, "").strip()
end_time = time.time()

print()
print(f"Prompt: {prompt}")
print()
print("Response:")
print(response)
print()
print(f"Time taken: {end_time - start_time:.2f} seconds")
