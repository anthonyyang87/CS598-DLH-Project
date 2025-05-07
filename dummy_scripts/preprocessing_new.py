
import argparse
import os
import pandas as pd

def dedup_mimic_iii(notes_path, out_path):
    df = pd.read_csv(notes_path)
    df_dedup = df.drop_duplicates(subset=["TEXT"])
    df_dedup.to_csv(out_path, index=False)
    print(f"[✓] Deduplicated notes saved to {out_path}")

def replace_deid_tags_mimic_iii(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df["TEXT"] = df["TEXT"].str.replace(r"\[.*?\]", "[REDACTED]", regex=True)
    df.to_csv(output_csv, index=False)
    print(f"[✓] Replaced DEID tags in MIMIC-III notes saved to {output_csv}")

def replace_deid_tags_mimic_iv(input_csv, input_anno_csv, output_csv):
    df = pd.read_csv(input_csv)
    df_anno = pd.read_csv(input_anno_csv)
    # Naive merge of annotations; adjust for real use-case
    for _, row in df_anno.iterrows():
        start, end = int(row['start']), int(row['end'])
        tag_type = row['type']
        df.loc[row['row'], 'TEXT'] = (
            df.loc[row['row'], 'TEXT'][:start] + f"[{tag_type}]" + df.loc[row['row'], 'TEXT'][end:]
        )
    df.to_csv(output_csv, index=False)
    print(f"[✓] Replaced DEID tags in MIMIC-IV notes saved to {output_csv}")

def combine_mimics(input_csv_iii, input_csv_ds, input_csv_rad, carevue_csv, output_csv):
    df_iii = pd.read_csv(input_csv_iii)
    df_ds = pd.read_csv(input_csv_ds)
    df_rad = pd.read_csv(input_csv_rad)
    df_care = pd.read_csv(carevue_csv)
    combined = pd.concat([df_iii, df_ds, df_rad, df_care], ignore_index=True)
    combined.to_csv(output_csv, index=False)
    print(f"[✓] Combined dataset saved to {output_csv}")

def remove_patient_ids(input_csv, mimic_iii_ids, mimic_iv_ids, output_csv):
    df = pd.read_csv(input_csv)
    ids_iii = pd.read_csv(mimic_iii_ids)["subject_id"].tolist()
    ids_iv = pd.read_csv(mimic_iv_ids)["subject_id"].tolist()
    df_filtered = df[~df["SUBJECT_ID"].isin(ids_iii + ids_iv)]
    df_filtered.to_csv(output_csv, index=False)
    print(f"[✓] Patient IDs removed, saved to {output_csv}")

def convert_csv_to_pretraining_format(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df["TEXT"].to_csv(output_csv, index=False, header=False)
    print(f"[✓] Pretraining text saved to {output_csv}")
