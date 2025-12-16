"""
单元测试：validators/ophthalmic_optical.py

测试眼科光学测量相关验证函数。
"""

import unittest
from pheno_qc_base import PhenoQCBase


def make_feature(final_value):
    """辅助函数，构造最小有效 feature payload。"""
    return {
        "value_trace": {
            "final": {
                "value": final_value
            }
        }
    }


class OphthalmicOpticalTests(unittest.TestCase):
    """测试 ophthalmic_optical.py 中的各验证函数"""

    # ========== is_between_0_and_1 ==========
    def test_is_between_0_and_1_valid_min(self):
        """测试最小值 0"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1_valid_max(self):
        """测试最大值 1"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature(1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1_valid_decimal(self):
        """测试小数 0.5"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature(0.5)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1_valid_small_decimal(self):
        """测试小数 0.001"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature(0.001)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1_valid_near_max(self):
        """测试接近最大值 0.999"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature(0.999)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1_string_number(self):
        """测试字符串数字 '0.75'"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature("0.75")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1_invalid_negative(self):
        """测试负数 -0.1"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature(-0.1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1_invalid_exceed(self):
        """测试超过上限 1.1"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature(1.1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1_invalid_string(self):
        """测试无效字符串"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature("abc")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1_invalid_none(self):
        """测试 None 值"""
        feature_key = "35475:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域似圆度(右)"

        payload = {feature_key: make_feature(None)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== _validate_hundred_scale_score ==========
    def test_validate_hundred_scale_score_valid_min(self):
        """测试最小值 0"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_valid_max(self):
        """测试最大值 100"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(100)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_valid_middle(self):
        """测试中间值 50"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(50)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_valid_decimal(self):
        """测试小数 75.5"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(75.5)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_valid_near_min(self):
        """测试接近最小值 0.1"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(0.1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_valid_near_max(self):
        """测试接近最大值 99.9"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(99.9)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_string_number(self):
        """测试字符串数字 '85'"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature("85")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_string_decimal(self):
        """测试字符串小数 '66.6'"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature("66.6")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_invalid_negative(self):
        """测试负数 -1"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_hundred_scale_score_invalid_exceed(self):
        """测试超过上限 100.1"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(100.1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_hundred_scale_score_invalid_large_exceed(self):
        """测试远超上限 200"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(200)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_hundred_scale_score_invalid_string(self):
        """测试无效字符串"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature("invalid")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_hundred_scale_score_invalid_none(self):
        """测试 None 值"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature(None)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_hundred_scale_score_invalid_empty_string(self):
        """测试空字符串"""
        feature_key = "35477:感官-眼科光学相干断层扫描仪:3x3以黄斑为中心_FAZ区域周长(右)(m)"

        payload = {feature_key: make_feature("")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)


if __name__ == "__main__":
    unittest.main()
