# Clinical Language Model Reproduction Using LLM (Simplified Preprocessing Reproduction)

***Disclaimer: This project is a simplified and partial reproduction due to hardware constraints.***  

This repository provides a streamlined implementation to reproduce the **preprocessing pipeline** of the paper:  
**"Do We Still Need Clinical Language Models?"** by Lehman et al.

**Original Paper**: https://arxiv.org/abs/2302.08091  
**Original Repository**: https://github.com/elehman16/do-we-still-need-clinical-lms

---

## 🔧 Project Structure

- `scripts/preprocessing/`: Full set of Python preprocessing scripts (e.g., DEID tag replacement, note deduplication)
- `run_preprocessing_pipeline.sh`: Main bash script to run the full preprocessing pipeline
- `data/`: Directory expected to hold raw input files such as MIMIC-III/IV, RadQA, Discharge data, and annotations
- `output/`: Preprocessed text output (DEID tags replaced, combined notes, and ready for pretraining)

---

## ⚙️ Environment Setup

We recommend using `conda` or `venv`:

```bash
conda create -n clinical-preprocess python=3.9
conda activate clinical-preprocess
pip install -r requirements.txt
```

---

## 📥 Data Access Instructions

To reproduce preprocessing and clinical tasks, you must obtain access to the following datasets:

### 🔐 Required Credentialing
Before accessing most datasets, complete the **CITI "Data or Specimens Only Research" course** and sign the corresponding **Data Use Agreement (DUA)** with PhysioNet or MIT Lab.

### 📚 Dataset Links

| Dataset               | Description                                   | Access Link                                                                 |
|------------------------|-----------------------------------------------|------------------------------------------------------------------------------|
| **MedNLI**             | Clinical natural language inference dataset   | [PhysioNet MedNLI](https://physionet.org/content/mednli/1.0.0/)              |
| **RadQA**              | Radiology question answering dataset          | [PhysioNet RadQA](https://physionet.org/content/radqa/1.0.0/)                |
| **Discharge Notes**    | Annotated hospital discharge summaries        | [Labelled Hospital Notes](https://physionet.org/content/labelled-notes-hospital-course/1.2.0/) |
| **MIMIC-III CareVue**  | Clinical notes from CareVue EHR system        | [MIMIC-III CareVue](https://physionet.org/content/mimic3-carevue/1.4/)       |
| **Noteevents**         | Full set of clinical notes                    | [Kaggle Noteevents](https://www.kaggle.com/datasets/hussameldinanwer/noteevents-mimic-iii) |

### 🔧 Directory Structure

After downloading, organize the files like this:

data/
├── raw_datasets/
│ ├── NOTEEVENTS.csv
│ ├── discharge.csv
│ ├── discharge_annotation.csv
│ ├── radiology.csv
│ ├── radiology_annotation.csv
│ ├── MIMIC_III_CAREVIEW_NOTEEVENTS.csv
├── MedNLI/
│ ├── train.tsv
│ ├── dev.tsv
│ ├── test.tsv

## 🚀 Preprocessing Pipeline Usage

To run the complete preprocessing flow on your local machine:

```bash
bash run_preprocessing_pipeline.sh \
  data/raw/NOTEEVENTS.csv \
  data/raw/discharge.csv \
  data/raw/discharge_annotation.csv \
  data/raw/radiology.csv \
  data/raw/radiology_annotation.csv \
  data/raw/MIMIC_III_CAREVIEW_NOTEEVENTS.csv \
  output/
```

### Output files include:
- `output/NOTEEVENTS_DEDUP_REPLACED_TAGS.csv`
- `output/DISCHARGE_REPLACED_DEID_TAGS.csv`
- `output/RADIOLOGY_REPLACED_DEID_TAGS.csv`
- `output/ALL_COMBINED_III_IV_REPLACED_TAGS.csv`
- `output/COMBINED_III_IV_TRAIN_REPLACED_TAGS.csv`
- `output/COMBINED_III_IV_TRAIN_REPLACED_TAGS_TEXT_ONLY.csv`

---

## 📌 Limitations

- Only preprocessing was reproduced due to memory and GPU limitations.
- Full training of Clinical-T5 or large model variants was not attempted.
- Evaluation and downstream task performance were not replicated.

---

## 📄 License

MIT