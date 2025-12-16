"""Validators for My Assigned Features (Bio-impedance, Fingerprint, etc.)."""
import pandas as pd
import os

# 1. 定义通用常量
na_values = {'na', 'n/a', 'null', 'missing', 'nan', 'none', 'nA', ''}

# 2. 定义指纹数据的合法值白名单
FINGERPRINT_ALLOW_LIST = {'蚊香', '牛奶', 'B', '粽子', '甘草', '桡箕', '玫瑰', '豆豉', 't缺失', '一般型', '姜', '海带', '酱油', '帐弓', 'c缺失', '蜂蜜', '黄瓜', '胶水', 'Level_4', '猿线', '桂圆', '茴香', '葱', '机油', '川掌纹', '豆浆', '非真实花纹', '咖啡', '爽身粉', '鱼', '简斗', '芝麻油', 'Level_7', '杏仁', '臭豆腐', 'A', '榨菜', 'd缺失', 'Level_6', '酸奶', '花生', '2个远箕纹', '无缺失', '双箕斗', '泡菜', 'AS', '椰子', '柠檬', 'Level_8', '烤红薯', '悉尼线', '胡椒', 'Level_5', '核桃', '杉木', '荔枝', '闻不到味道或者无法辨别', 'C', '芥末', '腐乳', '油漆', '橡胶', '橘子', '爆米花', '番茄', '尺箕', '皮革', '奶油', '樟脑', '火药', '消毒水', '简弓', '柚子', '绿茶', 'Level_9', '汽油', 'AD', '红枣', '真实花纹', '橙子', '香蕉', '花椒油', '孜然', '梨', '醋', '薄荷'}

def register(registry, prefix_registry):
    # 获取当前文件所在目录，确保能找到 txt
    curr_dir = os.path.dirname(__file__)
    
    # --- 注册数值型规则 ---
    numeric_txt = os.path.join(curr_dir, 'my_numeric_keys.txt')
    if os.path.exists(numeric_txt):
        with open(numeric_txt, "r", encoding="utf-8") as file:
            for line in file:
                content = line.strip()
                if content:
                    registry[content] = is_valid_numeric

    # --- 注册因子型(指纹)规则 ---
    factor_txt = os.path.join(curr_dir, 'my_factor_keys.txt')
    if os.path.exists(factor_txt):
        with open(factor_txt, "r", encoding="utf-8") as file:
            for line in file:
                content = line.strip()
                if content:
                    registry[content] = is_valid_fingerprint


def is_valid_numeric(feature_key, final_value, payload) -> bool:
    """
    数值型校验：
    1. 过滤 NA/空值
    2. 确保能转为数字 (float)
    """
    try:
        # 1. 字符串类型的空值检查
        if isinstance(final_value, str):
            if final_value.strip().lower() in na_values:
                return False
            # 尝试转数字
            float(final_value)
            return True
        
        # 2. 数值类型的检查
        elif isinstance(final_value, (int, float)):
            if pd.isna(final_value): # 检查 NaN
                return False
            return True
            
        # 其他类型视为异常
        else:
            return False
            
    except (ValueError, TypeError):
        return False


def is_valid_fingerprint(feature_key, final_value, payload) -> bool:
    """
    指纹校验：
    检查值是否在定义的白名单(FINGERPRINT_ALLOW_LIST)中
    """
    if final_value is None:
        return False
        
    # 统一转成字符串并去空格
    val_str = str(final_value).strip()
    
    # 检查是否是空值字样
    if val_str.lower() in na_values:
        return False
        
    # 核心校验：是否在白名单里
    return val_str in FINGERPRINT_ALLOW_LIST