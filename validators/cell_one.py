"""Validators for Questionnaire 1 related features (体型、自报饮酒/咖啡等)."""
import pandas as pd

na_values = {'na', 'n/a', 'null', 'missing', 'nan', 'none', 'nA', 'NA', 'Na'}

def register(registry, prefix_registry, name_txt='validators/cell.txt'):
    with open(name_txt, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            content = line.strip()
            registry[content] = is_na_or_greater_zero
            # prefix_registry[content] = is_greater_zero


def is_na_or_greater_zero(feature_key, final_value, payload) -> bool:
    """
    规则：判断是否为na，以及是否不小于0。
    """
    try:
        if isinstance(final_value, str):
            if final_value.lower() in na_values:
                return False
            else:
                # return True
                num = float(final_value)
                return num >= 0
        else:
            if pd.isna(final_value):
                return False
            else:
                # return True
                num = final_value
                return num >= 0
    except (TypeError, ValueError):
        return False

def is_greater_zero(feature_key, final_value, payload) -> bool:
    """
    判断是否为大于0，接受字符串数字或数值类型。
    """
    try:
        num = float(final_value)
    except (TypeError, ValueError):
        return False
    return num >= 0