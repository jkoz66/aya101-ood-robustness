from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

checkpoint = "CohereForAI/aya-101"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
aya_model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

questions = [
    "Aký je chemický vzorec vody?",,
    # ... add questions here
]

for i, q in enumerate(questions, start=1):
    inputs = tokenizer.encode(q, return_tensors="pt")
    outputs = aya_model.generate(inputs, max_new_tokens=128)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Q{i}: {q}")
    print(f"A{i}: {answer}\n")