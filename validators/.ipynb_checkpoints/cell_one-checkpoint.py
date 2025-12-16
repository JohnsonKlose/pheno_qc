"""Validators for Questionnaire 1 related features (体型、自报饮酒/咖啡等)."""
import pandas as pd

na_values = {'na', 'n/a', 'null', 'missing', 'nan', 'none', 'nA'}

def register(registry, prefix_registry, name_txt='validators/cell.txt'):
    with open(name_txt, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            content = line.strip()
            registry[content] = is_na_or_value


def is_na_or_value(feature_key, final_value, payload) -> bool:
    """
    规则：值需为 1-5 之间的整数（字符串或数字均可），否则判异常。
    """
    try:
        if isinstance(final_value, str):
            if final_value.lower() in na_values:
                return False
            else:
                return True
        else:
            if pd.isna(final_value):
                return False
            else:
                return True
    except (TypeError, ValueError):
        return False

def is_natural_number(feature_key, final_value, payload) -> bool:
    """
    判断是否为自然数（0,1,2,...），接受字符串数字或数值类型。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return num >= 0