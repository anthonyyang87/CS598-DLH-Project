
from transformers import T5ForConditionalGeneration, Trainer, TrainingArguments, AutoTokenizer
from datasets import load_dataset

def main():
    model_name = 't5-base'
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    dataset = load_dataset('mednli', split='train[:1%]')

    def preprocess(example):
        input_text = f"premise: {example['premise']} hypothesis: {example['hypothesis']}"
        target = example['label'] if example['label'] != -1 else 0  # default to 0
        return tokenizer(input_text, truncation=True, padding='max_length', max_length=128, return_tensors='pt'), {'labels': target}

    tokenized_dataset = dataset.map(lambda x: {
        'input_ids': tokenizer(x['premise'], x['hypothesis'], truncation=True, padding='max_length', max_length=128)['input_ids'],
        'labels': 0 if x['label'] == -1 else x['label']
    })

    args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="no",
        per_device_train_batch_size=2,
        num_train_epochs=1,
        save_steps=10_000,
        logging_dir="./logs",
        remove_unused_columns=False
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=tokenized_dataset,
    )

    trainer.train()

if __name__ == "__main__":
    main()
