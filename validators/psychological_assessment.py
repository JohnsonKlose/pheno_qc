"""Psychological assessment features."""

def register(registry, prefix_registry):
    registry["35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"] = __is_not_empty
    registry["35437:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"] = __is_not_empty
    registry["35438:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"] =__is_not_empty
    registry["35439:心理-心理评测:您在完成测试后的信心程度是"] = __is_not_empty
    registry["35440:心理-心理评测:您在完成测试后的信心程度是"] = __is_not_empty
    registry["35441:心理-心理评测:您在完成测试后的疲劳程度是"] = __is_not_empty
    registry["35442:心理-心理评测:您在完成测试后的疲劳程度是"] = __is_not_empty
    registry["35443:心理-心理评测:您认为此测试的有趣程度是"] = __is_not_empty
    registry["35444:心理-心理评测:您认为此测试的有趣程度是"] = __is_not_empty
    registry["35445:心理-心理评测:您认为此测试的难易程度是"] = __is_not_empty
    registry["35446:心理-心理评测:您认为此测试的难易程度是"] = __is_not_empty
    registry["35447:心理-心理评测:您认为系统内指导语讲解部分的清楚程度是"] = __is_not_empty
    registry["35448:心理-心理评测:您认为系统内指导语讲解部分的清楚程度是"] = __is_not_empty

def __is_not_empty(feature_key, final_value, payload) -> bool:
    """
    判断输入是否非空。
    - 适用于字符串类型，去除首尾空格后非空即通过。
    - 其他类型判异常。
    """
    if isinstance(final_value, str):
        return bool(final_value.strip())
    return False
