#!/usr/bin/env python3
"""Code generator for molecule_elements.py validator based on dingmap.csv."""

import csv
import os

# Read dingmap.csv and extract elements entries
csv_path = os.path.join(os.path.dirname(__file__), '..', 'validators', 'dingmap.csv')
elements_entries = []

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

        # Filter for elements entries
        if '分子代谢-分子代谢-Elements:' in feature_desc:
            elements_entries.append((row_num, feature_desc))

print(f"Found {len(elements_entries)} elements entries")

# Generate the validator code
output_path = os.path.join(os.path.dirname(__file__), '..', 'validators', 'molecule_elements.py')

print(f"Generating {output_path}...")

with open(output_path, 'w', encoding='utf-8') as f:
    # Write header
    f.write('"""Validators for Molecular Metabolome - Elements features."""\n')
    f.write('\n\n')

    # Write register function
    f.write('def register(registry, prefix_registry):\n')
    f.write('    """Register validators for elements features.\n')
    f.write('    \n')
    f.write(f'    Total features: {len(elements_entries)}\n')
    f.write('    Element features are concentration values in μg/L or mg/L.\n')
    f.write('    """\n')

    # Register all entries with the numeric validator
    for row_num, feature_desc in elements_entries:
        feature_key = f"{row_num}:{feature_desc}"
        f.write(f'    registry["{feature_key}"] = _validate_concentration\n')

    f.write('\n\n')

    # Write validator functions
    f.write('def _validate_concentration(feature_key, final_value, payload) -> bool:\n')
    f.write('    """\n')
    f.write('    Validate concentration values for element features.\n')
    f.write('    \n')
    f.write('    Rules:\n')
    f.write('    - Must be numeric (int or float)\n')
    f.write('    - Must be non-negative (>= 0)\n')
    f.write('    - Reasonable upper limit: 10000 mg/L (accommodates both μg/L and mg/L units)\n')
    f.write('    - Accepts both string numbers and numeric types\n')
    f.write('    \n')
    f.write('    Note: Features use mixed units (μg/L for trace elements, mg/L for major elements).\n')
    f.write('    The validator treats all as raw numeric values since conversion is unit-dependent.\n')
    f.write('    """\n')
    f.write('    try:\n')
    f.write('        value = float(final_value)\n')
    f.write('    except (TypeError, ValueError):\n')
    f.write('        return False\n')
    f.write('    \n')
    f.write('    # Concentration must be non-negative and within reasonable range\n')
    f.write('    # 10000 mg/L accommodates major elements like Na, S, Cl\n')
    f.write('    return 0 <= value <= 10000\n')

print(f"Successfully generated {output_path}")
print(f"Registered {len(elements_entries)} elements feature validators")
