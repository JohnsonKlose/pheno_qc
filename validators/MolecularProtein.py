"""
Validators for 分子蛋白.
"""

from typing import Any, Dict


def register(registry, prefix_registry):
    """
    分子蛋白质相关特征的校验函数,只有PBMC和Proteome两类。
    """
    prefix_registry.append(
        ("分子蛋白质-分子蛋白-PBMC", _validate_pbmc_protein)
    )

    prefix_registry.append(
        ("分子蛋白质-分子蛋白-Proteome", _validate_proteome_protein)
    )


def _validate_pbmc_protein(feature_key: str, final_value: Any, payload: Dict[str, Any]) -> bool:
    """
    PBMC 分子蛋白特征的异常值检测（阈值规则版）。

    规则：
    - 接受字符串数字或数值类型
    - 不接受 None、空字符串或非数值类型
    - 不接受 NaN / inf
    - 合理范围设定为 0 到 1e5（含边界）
    """
    # 1) 缺失值直接异常
    if final_value is None or final_value == "":
        return False

    # 2) 尝试转换为 float
    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False

    # 3) NaN / inf 视为异常
    if value != value:
        return False
    if value in (float("inf"), float("-inf")):
        return False

    # 4) 阈值判断
    return 0.0 <= value <= 1e5


def _validate_proteome_protein(feature_key: str, final_value: Any, payload: Dict[str, Any]) -> bool:
    """
    Proteome 分子蛋白特征的异常值检测（阈值规则版）。

    规则：
    - 接受字符串数字或数值类型
    - 不接受 None、空字符串或非数值类型
    - 不接受 NaN / inf
    - 合理范围设定为 0 到 1e5（含边界）
    """
    # 1) 缺失值直接异常
    if final_value is None or final_value == "":
        return False

    # 2) 尝试转换为 float
    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False

    # 3) NaN / inf 视为异常
    if value != value:
        return False
    if value in (float("inf"), float("-inf")):
        return False

    # 4) 阈值判断
    return 0.0 <= value <= 1e5
