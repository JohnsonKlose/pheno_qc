"""
单元测试：validators/traditional_chinese_med.py

测试中医表型相关验证函数。
"""

import unittest
from pheno_qc_base import PhenoQCBase


def make_feature(final_value, feature_key="test_key"):
    """
    辅助函数，构造最小有效 feature payload。
    """
    return {
        "feature_key": feature_key,
        "value_trace": {
            "final": {
                "value": final_value
            }
        }
    }


class TraditionalChineseMedTests(unittest.TestCase):
    """测试 traditional_chinese_med.py 中的各验证函数"""

    # ========== is_between_0_and_1000 ==========
    def test_is_between_0_and_1000_valid_min(self):
        """测试边界值 0"""
        feature_key = "37755:中医表型-中医四诊:Aa(收缩期面积)(左手)"
        payload = {feature_key: make_feature(0, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_valid_max(self):
        """测试边界值 1000"""
        feature_key = "37755:中医表型-中医四诊:Aa(收缩期面积)(左手)"

        payload = {feature_key: make_feature(1000)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_valid_middle(self):
        """测试中间值 500"""
        feature_key = "37755:中医表型-中医四诊:Aa(收缩期面积)(左手)"

        payload = {feature_key: make_feature(500)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_invalid_negative(self):
        """测试负数无效"""
        feature_key = "37755:中医表型-中医四诊:Aa(收缩期面积)(左手)"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "37755:中医表型-中医四诊:Aa(收缩期面积)(左手)"

        payload = {feature_key: make_feature(1001)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_string_number(self):
        """测试字符串数字"""
        feature_key = "37755:中医表型-中医四诊:Aa(收缩期面积)(左手)"

        payload = {feature_key: make_feature("123")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_invalid_string(self):
        """测试无效字符串"""
        feature_key = "37755:中医表型-中医四诊:Aa(收缩期面积)(左手)"

        payload = {feature_key: make_feature("abc")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== is_between_1_and_5 ==========
    def test_is_between_1_and_5_valid_min(self):
        """测试边界值 1"""
        feature_key = "37728:中医表型-中医四诊:失眠"

        payload = {feature_key: make_feature(1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_1_and_5_valid_max(self):
        """测试边界值 5"""
        feature_key = "37728:中医表型-中医四诊:失眠"

        payload = {feature_key: make_feature(5)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_1_and_5_invalid_zero(self):
        """测试 0 无效"""
        feature_key = "37728:中医表型-中医四诊:失眠"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_1_and_5_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "37728:中医表型-中医四诊:失眠"

        payload = {feature_key: make_feature(6)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== __is_not_empty ==========
    def test__is_not_empty_valid(self):
        """测试非空字符串"""
        feature_key = "37595:中医表型-中医四诊:气虚质得分(分)"

        payload = {feature_key: make_feature("有内容")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test__is_not_empty_invalid_empty_string(self):
        """测试空字符串"""
        feature_key = "37595:中医表型-中医四诊:气虚质得分(分)"

        payload = {feature_key: make_feature("")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_whitespace(self):
        """测试仅空白字符"""
        feature_key = "37595:中医表型-中医四诊:气虚质得分(分)"

        payload = {feature_key: make_feature("   ")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test__is_not_empty_invalid_none(self):
        """测试 None 值"""
        feature_key = "37595:中医表型-中医四诊:气虚质得分(分)"

        payload = {feature_key: make_feature(None)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== _validate_lab_value ==========
    def test_validate_lab_value_L_valid_min(self):
        """测试 L 通道最小值 0"""
        feature_key = "37691:中医表型-中医四诊:面象-唇色-面色(Lab值)_L"
        payload = {feature_key: make_feature(0, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_lab_value_L_valid_max(self):
        """测试 L 通道最大值 100"""
        feature_key = "37691:中医表型-中医四诊:面象-唇色-面色(Lab值)_L"
        payload = {feature_key: make_feature(100, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_lab_value_L_invalid_exceed(self):
        """测试 L 通道超过上限"""
        feature_key = "37691:中医表型-中医四诊:面象-唇色-面色(Lab值)_L"
        payload = {feature_key: make_feature(101, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_lab_value_L_invalid_negative(self):
        """测试 L 通道负数"""
        feature_key = "37691:中医表型-中医四诊:面象-唇色-面色(Lab值)_L"
        payload = {feature_key: make_feature(-1, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_lab_value_a_valid_min(self):
        """测试 a 通道最小值 -128"""
        feature_key = "37692:中医表型-中医四诊:面象-唇色-面色(Lab值)_a"
        payload = {feature_key: make_feature(-128, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_lab_value_a_valid_max(self):
        """测试 a 通道最大值 127"""
        feature_key = "37692:中医表型-中医四诊:面象-唇色-面色(Lab值)_a"
        payload = {feature_key: make_feature(127, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_lab_value_a_invalid_exceed(self):
        """测试 a 通道超过上限"""
        feature_key = "37692:中医表型-中医四诊:面象-唇色-面色(Lab值)_a"
        payload = {feature_key: make_feature(128, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_lab_value_a_invalid_too_low(self):
        """测试 a 通道低于下限"""
        feature_key = "37692:中医表型-中医四诊:面象-唇色-面色(Lab值)_a"
        payload = {feature_key: make_feature(-129, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_lab_value_b_valid_min(self):
        """测试 b 通道最小值 -128"""
        feature_key = "37693:中医表型-中医四诊:面象-唇色-面色(Lab值)_b"
        payload = {feature_key: make_feature(-128, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_lab_value_b_valid_max(self):
        """测试 b 通道最大值 127"""
        feature_key = "37693:中医表型-中医四诊:面象-唇色-面色(Lab值)_b"
        payload = {feature_key: make_feature(127, feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_lab_value_invalid_string(self):
        """测试无效字符串"""
        feature_key = "37691:中医表型-中医四诊:面象-唇色-面色(Lab值)_L"
        payload = {feature_key: make_feature("abc", feature_key)}
        qc = PhenoQCBase(payload)
        result = qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)


if __name__ == "__main__":
    unittest.main()
