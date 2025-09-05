from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained(
    "model/mistral",  # folder containing the GGUF file
    model_file="mistral-7b-instruct-v0.2.Q4_K_M.gguf",  # exact filename
    model_type="mistral"  # required for correct tokenizer and generation
)


def chat(user_input):
    system_prompt = "You are a friendly AI assistant. Keep answers short and conversational."
    full_prompt = f"[INST] {system_prompt}\nUser: {user_input}\nAssistant: [/INST]"
    return llm(full_prompt, max_new_tokens=100)
