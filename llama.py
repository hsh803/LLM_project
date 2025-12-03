# -*- coding: utf-8 -*-
https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
https://huggingface.co/blog/how-to-generate

!pip install transformers huggingface-hub torch

from huggingface_hub import login
login(token='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')

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Check if a GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the LLaMA 3.2-1B-Instruct tokenizer and model from Hugging Face
model_name = "meta-llama/Llama-3.2-1B-Instruct"  # Replace with your model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, pad_token_id=tokenizer.eos_token_id)
model = model.to(device)

def post_correct_sentence(sentence, model, tokenizer, device="cpu"):
    """Generate a corrected version of a sentence using LLaMA with focused output."""
    # Stronger correction prompt with no additional text
    correction_prompt = f"Correct the following transcription for any spelling or grammatical errors and output only corrected transcription: {sentence}."

    messages = [
        {"role": "system", "content": "You are a text correction assistant. Correct transcription errors in spelling and grammar. Output only the corrected sentence, nothing else."},
        {"role": "user", "content": correction_prompt},
    ]

    # Format the conversation into a string for tokenization
    chat_prompt = ""
    for message in messages:
        role, content = message["role"], message["content"]
        chat_prompt += f"<{role}>: {content}\n"

    # Tokenize the input sentence
    inputs = tokenizer(chat_prompt, return_tensors="pt").to(device)

    # Generate correction using greedy decoding
    corrected_ids = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=len(sentence.split()) + 20,
        do_sample=False
    )

    corrected_sentence = tokenizer.decode(corrected_ids[0], skip_special_tokens=True)
    corrected_sentence = corrected_sentence.split("<assistant>:")[-1].strip()

    return corrected_sentence

input_file = "/content/common500_lm.txt"
output_file = "/content/common500_llama_lm.txt"

with open(input_file, "r", encoding="utf-8") as f:
    transcriptions = [line.strip() for line in f if line.strip()]

# Post-correct ASR outputs
corrected_sentences = [post_correct_sentence(sentence, model, tokenizer, device=device) for sentence in transcriptions]

with open(output_file, "w", encoding="utf-8") as f:
    for corrected_sentence in corrected_sentences:
        f.write(corrected_sentence + "\n")

print(f"Corrected transcriptions saved to {output_file}")