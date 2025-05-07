
from datasets import load_metric
from transformers import AutoTokenizer, T5ForConditionalGeneration
from datasets import load_dataset

def evaluate():
    model = T5ForConditionalGeneration.from_pretrained('t5-base')
    tokenizer = AutoTokenizer.from_pretrained('t5-base')
    dataset = load_dataset('mednli', split='validation[:1%]')

    correct = 0
    total = 0

    for example in dataset:
        input_text = f"premise: {example['premise']} hypothesis: {example['hypothesis']}"
        inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
        output = model.generate(**inputs)
        pred = tokenizer.decode(output[0], skip_special_tokens=True)
        if str(example['label']) in pred:
            correct += 1
        total += 1

    print(f"Accuracy: {correct / total:.2f}")

if __name__ == "__main__":
    evaluate()
