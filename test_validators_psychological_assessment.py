"""
单元测试：validators/psychological_assessment.py

测试心理评测相关验证函数。
"""

import unittest
from pheno_qc_base import PhenoQCBase


def make_feature(final_value):
    """
    辅助函数，构造最小有效 feature payload。
    """
    return {
        "value_trace": {
            "final": {
                "value": final_value
            }
        }
    }


class PsychologicalAssessmentTests(unittest.TestCase):
    """测试 psychological_assessment.py 中的各验证函数"""

    # ========== __is_not_empty ==========
    def test__is_not_empty_valid_chinese_text(self):
        """测试有效中文文本"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("经常")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_english_text(self):
        """测试有效英文文本"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("sometimes")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_number_string(self):
        """测试数字字符串"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("123")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_mixed_content(self):
        """测试混合内容"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("答案A")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_single_char(self):
        """测试单个字符"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("是")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_with_leading_whitespace(self):
        """测试前导空格但有内容"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("  有内容")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_with_trailing_whitespace(self):
        """测试尾随空格但有内容"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("有内容  ")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_with_spaces_around(self):
        """测试两边空格但有内容"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("  有内容  ")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_special_chars(self):
        """测试特殊字符"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("!@#$%")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_valid_newline_and_text(self):
        """测试包含换行符但有内容"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("\n有内容\n")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_invalid_empty_string(self):
        """测试空字符串"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_whitespace_only(self):
        """测试仅空格"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("   ")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_tab_only(self):
        """测试仅制表符"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("\t\t")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_newline_only(self):
        """测试仅换行符"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("\n\n")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_mixed_whitespace(self):
        """测试混合空白字符"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature("  \t\n  ")}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_none(self):
        """测试 None 值"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature(None)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_number(self):
        """测试数字类型（非字符串）"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature(123)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_zero(self):
        """测试数字 0（非字符串）"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature(0)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_boolean(self):
        """测试布尔值（非字符串）"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature(True)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_list(self):
        """测试列表类型（非字符串）"""
        feature_key = "35436:心理-心理评测:您在完成每个任务的过程中，出现分心情况的频率约为"
        payload = {feature_key: make_feature([])}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)


if __name__ == "__main__":
    unittest.main()
