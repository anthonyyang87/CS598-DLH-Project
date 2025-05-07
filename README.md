
# Clinical Language Model Reproduction (Way Simpplified Version)

This repository provides a simplified reproduction of the paper: **"Do We Still Need Clinical Language Models?"**

**Original Paper Publication**: https://arxiv.org/abs/2302.08091
**Original Paper Repository**: https://github.com/elehman16/do-we-still-need-clinical-lms

## Project Structure

- `scripts/preprocess.py`: Prepares MedNLI dataset for model training using the Clinical-T5 tokenizer.
- `scripts/train.py`: Simplified training loop using HuggingFace Transformers.
- `scripts/evaluate.py`: Evaluation of trained model on classification metrics.
- `requirements.txt`: All essential Python packages required.
- `data/`: Expected directory for raw and processed dataset files.
- `models/`: Checkpoints will be saved here.
- `outputs/`: Evaluation results will be stored here.

## Environment Setup

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage Instructions

### 1. Data Preparation

Ensure MedNLI dataset is downloaded and placed under `data/MedNLI/` with files like:
- `train.tsv`
- `dev.tsv`
- `test.tsv`

Then run preprocessing:

```bash
python preprocess.py
```

### 2. Training

```bash
python train.py --model_name t5-base --output_dir models/
```

This will save checkpoints in `models/`.

### 3. Evaluation

```bash
python evaluate.py --model_path models/ --data_path data/processed/mednli_dev.json
```

Metrics like accuracy and classification report will be printed.

## Notes

- This setup is optimized for single-GPU training (e.g., NVIDIA 3070Ti).
- LoRA support is not included but could be added using `peft` and `transformers` integration.
- Adjust batch size in `train.py` if you run out of memory.

## License

MIT
