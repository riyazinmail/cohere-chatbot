from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# model_name = "google/flan-t5-small" --- this is not giving correct answer
# model_name = "google/flan-t5-base"
model_name = "google/flan-t5-xl"
# mistralai/Mistral-7B-Instruct-v0.2
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def chat(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
