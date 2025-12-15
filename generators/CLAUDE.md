# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a phenotype quality control (QC) validation framework for medical/scientific data. It validates feature values extracted from medical imaging, questionnaires, molecular assays, and other phenotype data sources. The framework uses a plugin-based validator system where validation rules are registered per-feature or by feature prefix.

## Core Architecture

### Entry Point: `PhenoQCBase`
Located in `pheno_qc_base.py`, this class:
- Accepts raw phenotype JSON data with nested structure (`value_trace.final.value`)
- Extracts final values and runs registered validators
- Returns compressed output with `abnormal` flag (0=valid, 1=invalid)
- Automatically discovers and loads validators from the `validators/` package

### Validator System
All validators live in `validators/` directory. Each module must implement:

```python
def register(registry, prefix_registry):
    registry["exact_feature_key"] = validator_function
    prefix_registry.append(("feature_prefix:", validator_function))
```

**Validator Function Signature:**
```python
def validator_function(feature_key: str, final_value: Any, feature_payload: dict) -> bool
```
- Returns `True` if value is valid (abnormal=0)
- Returns `False` if value is invalid (abnormal=1)
- Must return bool, other types raise TypeError

### Validation Priority
1. Exact key match from `registry`
2. Prefix match from `prefix_registry` (first match wins, order-sensitive)
3. `default_check()` fallback (returns True by default)

### Data Flow
Input JSON → `PhenoQCBase.__init__()` → `evaluate()` → extract `value_trace.final.value` → lookup validator → execute validator → set `abnormal` → compressed output

## Common Commands

### Run Tests
```bash
python -m unittest test_pheno_qc_base.py
```

### Run Single Test
```bash
python -m unittest test_pheno_qc_base.PhenoQCBaseTests.test_exact_age_validator_marks_out_of_range
```

### Interactive Testing
```python
from pheno_qc_base import PhenoQCBase

# Minimal test payload
payload = {
    "feature_key": {
        "feature_name": "Test Feature",
        "metadata": {"description": "Test description"},
        "value_trace": {"final": {"value": "test_value"}},
        "processing_context": {"method_name": "test_method"}
    }
}

qc = PhenoQCBase(payload)
result = qc.evaluate()
```

## Validator Development Guidelines

When creating a new validator (e.g., `validators/new_feature.py`):

1. **Type Tolerance**: Accept both string numbers and numeric types. Use `int(final_value)` or `float(final_value)` with try-except.

2. **Return False for Invalid Types**: When conversion fails, return `False` rather than raising exceptions.

3. **Set Reasonable Bounds**: Use biologically/physically plausible ranges (e.g., age 0-120, not unlimited).

4. **Prefix Order Matters**: In `prefix_registry`, register more specific prefixes before general ones.

5. **Module Auto-Discovery**: No need to modify `__init__.py` or import statements. The framework automatically discovers any module in `validators/` with a `register()` function.

## Example Validators

See `validators/questionnaire_one.py` for a complete reference implementation showing:
- Exact key registration for specific questions
- Prefix registration for question families
- Age validation (0-120 years)
- Yes/No validation (supporting "是/否" and "yes/no")
- Numeric range validation with reasonable bounds

## Repository Structure

- `pheno_qc_base.py` - Core QC framework class
- `test_pheno_qc_base.py` - Unit tests demonstrating validator behavior
- `validators/` - Plugin directory for validation modules
  - `__init__.py` - Package marker with documentation
  - `questionnaire_one.py` - Reference implementation for questionnaire features
  - `molecule_*.py` - Validators for molecular assay features
  - `na_*.py` - Validators for nucleic acid features

## Git Branch Strategy

Main branch: `main`
Current development branch: `guoxin`
