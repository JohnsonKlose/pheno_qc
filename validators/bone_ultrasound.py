"""
Validators for Bone Ultrasound related features (23 features).
Focus: Eliminating extreme outliers and measurement errors.
"""

def register(registry, prefix_registry):
    # 按照文件中的 Index:Pheno 格式穷举所有 23 个特征

# ===== 跟骨超声参数 =====
    # ===== 基本参数 =====
    registry["11701:超声-跟骨超声:SOS"] = _validate_SOS
    registry["11702:超声-跟骨超声:骨强度"] = _validate_bone_strength
    registry["11703:超声-跟骨超声:T值"] = _validate_z_t_score
    registry["11704:超声-跟骨超声:%年轻成人"] = _validate_percentage_young_adult
    registry["11705:超声-跟骨超声:Z值"] = _validate_z_t_score
    registry["11706:超声-跟骨超声:%年龄匹配"] = _validate_percentage_age_matched

    # ===== 骨超声 - AIB参数 =====
    registry["11707:超声-骨超声:2.25MHz单脉冲左脚跟骨外侧超声表观积分背散射(AIB)"] = _validate_AIB
    registry["11708:超声-骨超声:2.25MHz多脉冲左脚跟骨外侧超声表观积分背散射(AIB)"] = _validate_AIB
    registry["11709:超声-骨超声:3.5MHz单脉冲左脚跟骨外侧超声表观积分背散射(AIB)"] = _validate_AIB
    registry["11710:超声-骨超声:3.5MHz多脉冲左脚跟骨外侧超声表观积分背散射(AIB)"] = _validate_AIB
    
    # ===== BUA参数 =====
    registry["11721:超声-跟骨超声:BUA"] = _validate_BUA
    
    # ===== 3.5MHz单脉冲背散射频谱参数 =====
    registry["11722:超声-骨超声:3.5MHz单脉冲左脚跟骨外侧表观背散射零频截距(FIAB)"] = _validate_FIAB
    registry["11723:超声-骨超声:3.5MHz单脉冲左脚跟骨外侧表观背散射频率斜率(FSAB)"] = _validate_FSAB
    registry["11724:超声-骨超声:3.5MHz单脉冲左脚跟骨外侧超声背散射频谱质心偏移(SCS)"] = _validate_SCS
    
    # ===== 3.5MHz多脉冲背散射频谱参数 =====
    registry["11725:超声-骨超声:3.5MHz多脉冲左脚跟骨外侧表观背散射零频截距(FIAB)"] = _validate_FIAB
    registry["11726:超声-骨超声:3.5MHz多脉冲左脚跟骨外侧表观背散射频率斜率(FSAB)"] = _validate_FSAB
    registry["11727:超声-骨超声:3.5MHz多脉冲左脚跟骨外侧超声背散射频谱质心偏移(SCS)"] = _validate_SCS
    
    # ===== 2.25MHz多脉冲背散射频谱参数 =====
    registry["11738:超声-骨超声:2.25MHz多脉冲左脚跟骨外侧表观背散射零频截距(FIAB)"] = _validate_FIAB
    registry["11739:超声-骨超声:2.25MHz多脉冲左脚跟骨外侧表观背散射频率斜率(FSAB)"] = _validate_FSAB
    registry["11740:超声-骨超声:2.25MHz多脉冲左脚跟骨外侧超声背散射频谱质心偏移(SCS)"] = _validate_SCS
    
    # ===== 2.25MHz单脉冲背散射频谱参数 =====
    registry["11741:超声-骨超声:2.25MHz单脉冲左脚跟骨外侧表观背散射零频截距(FIAB)"] = _validate_FIAB
    registry["11742:超声-骨超声:2.25MHz单脉冲左脚跟骨外侧表观背散射频率斜率(FSAB)"] = _validate_FSAB
    registry["11743:超声-骨超声:2.25MHz单脉冲左脚跟骨外侧超声背散射频谱质心偏移(SCS)"] = _validate_SCS
    
  #  print("已注册 23 个骨超声特征校验器")



# --- 具体校验函数实现 ---
def _validate_SOS(feature_key, final_value, payload) -> bool:
    """
    SOS (声波速度) 校验
    正常范围: 1400-1700 m/s
    异常: <1000或>2000 m/s
    """
    if not validate_numeric_value(final_value, allow_negative=False, allow_zero=False):
        return False
    
    try:
        sos_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # 生理范围: 1400-1700 m/s
    # 剔除明显异常: <1000或>2000
    return 1000 <= sos_val <= 2000

def _validate_z_t_score(feature_key, final_value, payload) -> bool:
    """Z值/T值 QC: 标准差倍数，超过10倍属于极端录入错误。"""
    if not validate_numeric_value(final_value, allow_negative=True, allow_zero=True):
        return False
    try:
        val = float(final_value)
        return -10 <= val <= 10
    except: return False

def _validate_bone_strength(feature_key, final_value, payload) -> bool:
    """
    骨强度校验
    正常范围: 50-150
    异常: <0或>200
    """
    if not validate_numeric_value(final_value, allow_negative=False, allow_zero=True):
        return False
    
    try:
        strength_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # 骨强度通常为正值，可能为0但很少负值
    # 根据样本数据，有负值(-58.1852)，但可能是异常
    # 设置范围: -100 ~ 200
    return -100 <= strength_val <= 200


def _validate_percentage_young_adult(feature_key, final_value, payload) -> bool:
    """
    %年轻成人校验
    正常范围: 80-120%
    异常: <50%或>150%
    """
    if not validate_numeric_value(final_value, allow_negative=True, allow_zero=True):
        return False
    
    try:
        perc_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # 百分比范围: 0-250%
    # 但正常应在50-150%之间
    return 0 <= perc_val <= 250

def _validate_percentage_age_matched(feature_key, final_value, payload) -> bool:
    """
    %年龄匹配校验
    正常范围: 80-120%
    异常: <50%或>150%
    """
    if not validate_numeric_value(final_value, allow_negative=True, allow_zero=True):
        return False
    
    try:
        perc_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # 百分比范围: 0-250%
    return 0 <= perc_val <= 250


def _validate_BUA(feature_key, final_value, payload) -> bool:
    """
    BUA (宽带超声衰减) 校验
    正常范围: 50-130 dB/MHz
    异常: <20或>150
    """
    if not validate_numeric_value(final_value, allow_negative=False, allow_zero=True):
        return False
    
    try:
        bua_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # BUA范围: 20-200 dB/MHz
    return 20 <= bua_val <= 200

def _validate_AIB(feature_key, final_value, payload) -> bool:
    """
    AIB (表观积分背散射) 校验
    正常范围: -60 ~ -15 dB
    根据频率不同略有差异
    """
    if not validate_numeric_value(final_value, allow_negative=True, allow_zero=False):
        return False
    
    try:
        aib_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # AIB为负值，通常范围: -70 ~ -10 dB
    return -70 <= aib_val <= -10


def _validate_FIAB(feature_key, final_value, payload) -> bool:
    """
    FIAB (表观背散射零频截距) 校验
    正常范围: -60 ~ -15 dB
    """
    if not validate_numeric_value(final_value, allow_negative=True, allow_zero=False):
        return False
    
    try:
        fiab_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # FIAB为负值，范围: -80 ~ 0 dB
    return -80 <= fiab_val <= 0

def _validate_FSAB(feature_key, final_value, payload) -> bool:
    """
    FSAB (表观背散射频率斜率) 校验
    范围: -15 ~ +15 dB/MHz
    可正可负
    """
    if not validate_numeric_value(final_value, allow_negative=True, allow_zero=True):
        return False
    
    try:
        fsab_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # FSAB范围: -20 ~ +20 dB/MHz
    return -20 <= fsab_val <= 20


def _validate_SCS(feature_key, final_value, payload) -> bool:
    """
    SCS (频谱质心偏移) 校验
    范围根据数据样本: -350 ~ +350
    """
    if not validate_numeric_value(final_value, allow_negative=True, allow_zero=True):
        return False
    
    try:
        scs_val = float(final_value)
    except (ValueError, TypeError):
        return False
    
    # SCS范围: -500 ~ +500 
    return -500 <= scs_val <= 500



# ==================== 通用校验函数 ====================

def validate_numeric_value(value, allow_negative=True, allow_zero=True, allow_special_strings=False):
    """通用数值校验基础函数"""
    if value is None:
        return False
    
    # 检查是否为字符串
    if isinstance(value, str):
        value_str = value.strip()
        
        # 检查特殊字符串
        if not allow_special_strings:
            if value_str.lower() in ['', 'na', 'nan', 'null', 'none', 'inf', '-inf', 'infinity', '-infinity']:
                return False
        
        # 尝试转换为数值
        try:
            value = float(value_str)
        except (ValueError, TypeError):
            # 如果不能转换且不允许特殊字符串
            if not allow_special_strings:
                return False
            # 允许特殊字符串时返回True
            return True
    
    # 检查数值类型
    if not isinstance(value, (int, float)):
        return False
    
    # 检查是否为特殊数值
    import math
    if math.isinf(value) or math.isnan(value):
        return False
    
    # 检查是否允许零值
    if not allow_zero and value == 0:
        return False
    
    # 检查是否允许负值
    if not allow_negative and value < 0:
        return False
    
    return True