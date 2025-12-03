# -*- coding: utf-8 -*-
!pip install jiwer pandas openpyxl

import pandas as pd
from jiwer import wer

# Load Excel file with references and hypotheses
input_file = "/content/common_500_llama_lm.xlsx"  # Replace with your input file path
output_file = "/content/common_500_llama_lm_wer.xlsx"  # Replace with desired output file path

# Read the Excel file
df = pd.read_excel(input_file)

# Check that columns 'Reference' and 'Hypothesis' exist
if 'reference' not in df.columns or 'hypothesis' not in df.columns:
    raise ValueError("Input file must contain 'Reference' and 'Hypothesis' columns")

# Calculate WER for each pair and store in a new column
df['WER'] = df.apply(lambda row: wer(row['reference'], row['hypothesis']), axis=1)

# Save the DataFrame with the new WER column to a new Excel file
df.to_excel(output_file, index=False)

print("WER calculations complete. Results saved to", output_file)