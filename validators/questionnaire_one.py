"""Validators for Questionnaire 1 related features (体型、自报饮酒/咖啡等)."""


def register(registry, prefix_registry):
    registry["3790:健康问卷调查-问卷-1:10年前体型图"] = _validate_body_shape_retrospective
    registry["3792:健康问卷调查-问卷-1:20岁时体型图"] = _validate_body_shape_retrospective
    registry["3795:健康问卷调查-问卷-1:从多少岁开始不喝咖啡(岁)"] = _validate_age
    registry["3894:健康问卷调查-问卷-1:饮酒后感到失望"] = is_yes_no
    registry["3818:健康问卷调查-问卷-1:喝酒是否会出现脸红"] = is_yes_no
    registry["3829:健康问卷调查-问卷-1:小时候家里是否有人抽烟"] = is_yes_no
    registry["3835:健康问卷调查-问卷-1:工作场所是否有人抽烟"] = is_yes_no
    registry["3845:健康问卷调查-问卷-1:开始年龄"] = _validate_age
    registry["3851:健康问卷调查-问卷-1:您是否出生在上海"] = _validate_age
    registry["3855:健康问卷调查-问卷-1:成年家里是否有人抽烟"] = is_yes_no
    registry["3859:健康问卷调查-问卷-1:无法戒酒"] = is_yes_no
    registry["3863:健康问卷调查-问卷-1:是否曾有饮酒习惯"] = is_yes_no
    registry["3865:健康问卷调查-问卷-1:是否有喝隔夜茶"] = is_yes_no
    registry["3867:健康问卷调查-问卷-1:是否有饮茶习惯"] = is_yes_no
    registry["3869:健康问卷调查-问卷-1:是否采取过措施控制体重"] = is_yes_no
    registry["3872:健康问卷调查-问卷-1:曾经多少岁开始喝咖啡(岁)"] = _validate_age
    registry["3873:健康问卷调查-问卷-1:曾经平均每周喝咖啡量(ml)"] = _validate_weekly_coffee_ml
    registry["3875:健康问卷调查-问卷-1:现在体型图"] = is_between_1_and_9
    registry["3877:健康问卷调查-问卷-1:现在有多少家庭成员共同和您生活在一起"] = is_natural_number
    registry["3891:健康问卷调查-问卷-1:饮酒习惯影响正常的生活"] = is_yes_no
    registry["3884:健康问卷调查-问卷-1:结束年龄"] = _validate_age
    # 仅对可能有子字段/补充后缀的题号添加前缀规则，其余保持精确匹配。
    prefix_registry.append(
        ("3796:健康问卷调查-问卷-1:从多少岁起", _validate_age)
    )


def _validate_body_shape_retrospective(feature_key, final_value, payload) -> bool:
    """
    规则：值需为 1-5 之间的整数（字符串或数字均可），否则判异常。
    """
    try:
        val = int(final_value)
    except (TypeError, ValueError):
        return False
    return 1 <= val <= 5


def _validate_age(feature_key, final_value, payload) -> bool:
    """
    规则：年龄型数值，取整数且在 0-120 岁之间。
    - 允许字符串数字或数值类型。
    - 其他情况判异常。
    """
    try:
        age = int(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= age <= 120


def is_yes_no(feature_key, final_value, payload) -> bool:
    """
    判断输入是否为“是”或“否”，用于通用二分类问卷题。
    - 接受中文“是/否”（含去除首尾空格）
    - 宽松接受英文 yes/no（不区分大小写）
    """
    if isinstance(final_value, str):
        normalized = final_value.strip().lower()
        return normalized in {"是", "否", "yes", "no"}
    return False


def _validate_weekly_coffee_ml(feature_key, final_value, payload) -> bool:
    """
    规则：平均每周咖啡量（毫升），接受非负实数，设定上限 0-50000 ml 以滤除明显异常。
    - 允许字符串数字或数值类型。
    """
    try:
        vol = float(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= vol <= 50000


def is_between_1_and_9(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 1-9（含）之间，接受字符串数字或数值类型。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 1 <= num <= 9


def is_natural_number(feature_key, final_value, payload) -> bool:
    """
    判断是否为自然数（0,1,2,...），接受字符串数字或数值类型。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return num >= 0