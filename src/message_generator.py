from transformers import pipeline

generator = pipeline("conversational", model="tinkoff-ai/ruDialoGPT-medium")


def generate(text: str) -> str:
    inputs = generator.tokenizer(f"@@ПЕРВЫЙ@@{text}@@ВТОРОЙ@@", return_tensors="pt")

    generated_token_ids = generator.model.generate(
        **inputs,
        top_k=10,
        top_p=0.95,
        num_beams=3,
        num_return_sequences=1,
        do_sample=True,
        no_repeat_ngram_size=2,
        temperature=1.2,
        repetition_penalty=1.2,
        length_penalty=1.0,
        eos_token_id=50257,
        max_new_tokens=60
    )
    result = [generator.tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids][0]
    last_second = result.split("@@ВТОРОЙ@@")[-1].split("@@ПЕРВЫЙ@@")[0]
    return last_second
