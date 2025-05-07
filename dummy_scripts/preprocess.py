
from datasets import load_dataset
from transformers import AutoTokenizer

def preprocess(dataset_name='mednli', model_name='t5-base'):
    print("Loading dataset...")
    dataset = load_dataset("mednli", split='train')
    print("Dataset loaded. Sample:", dataset[0])

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    def tokenize_fn(example):
        return tokenizer(example['premise'], example['hypothesis'], truncation=True, padding='max_length', max_length=128)
    
    print("Tokenizing...")
    tokenized_dataset = dataset.map(tokenize_fn)
    print("Done tokenizing. Sample:", tokenized_dataset[0])
    return tokenized_dataset

if __name__ == "__main__":
    preprocess()
