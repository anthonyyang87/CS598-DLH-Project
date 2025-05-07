#!/bin/bash

# Set PYTHONPATH
export PYTHONPATH=$(pwd)
echo "PYTHONPATH set to $PYTHONPATH"

# Input paths (you can modify these as needed)
RAW_MIMIC_III=data/raw_data/NOTEEVENTS.csv
RAW_DISCHARGE=data/raw_datasets/discharge.csv
RAW_DISCHARGE_ANN=data/raw_datasets/discharge_annotation.csv
RAW_RADIOLOGY=data/raw_datasets/radiology.csv
RAW_RADIOLOGY_ANN=data/raw_datasets/radiology_annotation.csv
CAREVIEW_NOTES=data/raw_datasets/MIMIC_III_CAREVIEW_NOTEEVENTS.csv
REMOVE_III_IDS=data/ids_to_remove_mimic_iii_only.csv
REMOVE_IV_IDS=data/mimic_iv_ids_to_remove.csv

# Output paths
DEDUP_III=data/NOTEEVENTS_DEDUP.csv
III_REPLACED=data/NOTEEVENTS_DEDUP_REPLACED_TAGS.csv
DISCHARGE_REPLACED=data/DISCHARGE_REPLACED_DEID_TAGS.csv
RADIOLOGY_REPLACED=data/RADIOLOGY_REPLACED_DEID_TAGS.csv
COMBINED=data/ALL_COMBINED_III_IV_REPLACED_TAGS.csv
FINAL_CLEAN=data/COMBINED_III_IV_TRAIN_REPLACED_TAGS.csv
TEXT_ONLY=data/COMBINED_III_IV_TRAIN_REPLACED_TAGS_TEXT_ONLY.csv

# 1. De-duplicate MIMIC-III notes
python preprocessing/dedup_mimic_iii.py --notes-path "$RAW_MIMIC_III" --out-path "$DEDUP_III"

# 2. Replace DEID tags in MIMIC-III
python preprocessing/replace_deid_tags.py \
    --type "mimic-iii" \
    --input-csv "$DEDUP_III" \
    --output-csv "$III_REPLACED"

# 3. Replace DEID tags in MIMIC-IV discharge
python preprocessing/replace_deid_tags.py \
    --type "mimic-iv" \
    --input-csv "$RAW_DISCHARGE" \
    --input-annotation-csv "$RAW_DISCHARGE_ANN" \
    --output-csv "$DISCHARGE_REPLACED"

# 4. Replace DEID tags in MIMIC-IV radiology
python preprocessing/replace_deid_tags.py \
    --type "mimic-iv" \
    --input-csv "$RAW_RADIOLOGY" \
    --input-annotation-csv "$RAW_RADIOLOGY_ANN" \
    --output-csv "$RADIOLOGY_REPLACED"

# 5. Combine all CSVs
python preprocessing/combine_mimics.py \
    --input-csv-iii "$III_REPLACED" \
    --input-csv-ds "$DISCHARGE_REPLACED" \
    --input-csv-rad "$RADIOLOGY_REPLACED" \
    --carevue-csv "$CAREVIEW_NOTES" \
    --output-csv "$COMBINED"

# 6. Remove patient IDs from fine-tuning data
python preprocessing/remove_patient_ids.py \
    --input-csv "$COMBINED" \
    --mimic-iii "$REMOVE_III_IDS" \
    --mimic-iv "$REMOVE_IV_IDS" \
    --output-csv "$FINAL_CLEAN"

# 7. Convert to text-only pretraining format
python preprocessing/convert_csv_to_pretraining_format.py \
    --input-csv "$FINAL_CLEAN" \
    --output-csv "$TEXT_ONLY"