#!/usr/bin/env python3
"""Code generator for na_wholeblood.py validator based on dingmap.csv."""

import csv
import os

# Read dingmap.csv and extract wholeblood entries
csv_path = os.path.join(os.path.dirname(__file__), '..', 'validators', 'dingmap.csv')
wholeblood_entries = []

print("Reading dingmap.csv...")
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header

    for row in reader:
        if len(row) < 3:
            continue

        # Column 0: row number, Column 2: feature description (opu)
        row_num = row[0]
        feature_desc = row[2]

        # Filter for wholeblood entries
        if '核酸-核酸-WholeBlood:' in feature_desc or '核酸-WholeBlood' in feature_desc:
            wholeblood_entries.append((row_num, feature_desc))

print(f"Found {len(wholeblood_entries)} wholeblood entries")

# Generate the validator code
output_path = os.path.join(os.path.dirname(__file__), '..', 'validators', 'na_wholeblood.py')

print(f"Generating {output_path}...")

with open(output_path, 'w', encoding='utf-8') as f:
    # Write header
    f.write('"""Validators for Nucleic Acid - Whole Blood transcriptome features."""\n')
    f.write('\n\n')

    # Write register function
    f.write('def register(registry, prefix_registry):\n')
    f.write('    """Register validators for whole blood transcriptome features.\n')
    f.write('    \n')
    f.write(f'    Total features: {len(wholeblood_entries)}\n')
    f.write('    All whole blood features are expected to be log2FPKM values (numeric).\n')
    f.write('    """\n')

    # Register all entries with the numeric validator
    for row_num, feature_desc in wholeblood_entries:
        feature_key = f"{row_num}:{feature_desc}"
        f.write(f'    registry["{feature_key}"] = _validate_log2fpkm\n')

    f.write('\n\n')

    # Write validator functions
    f.write('def _validate_log2fpkm(feature_key, final_value, payload) -> bool:\n')
    f.write('    """\n')
    f.write('    Validate log2FPKM values for whole blood transcriptome features.\n')
    f.write('    \n')
    f.write('    Rules:\n')
    f.write('    - Must be numeric (int or float)\n')
    f.write('    - Reasonable range: -20 to 20 (log2 scale)\n')
    f.write('    - Accepts both string numbers and numeric types\n')
    f.write('    """\n')
    f.write('    try:\n')
    f.write('        value = float(final_value)\n')
    f.write('    except (TypeError, ValueError):\n')
    f.write('        return False\n')
    f.write('    \n')
    f.write('    # Log2FPKM values typically range from -20 to 20\n')
    f.write('    return -20 <= value <= 20\n')

print(f"Successfully generated {output_path}")
print(f"Registered {len(wholeblood_entries)} whole blood feature validators")
