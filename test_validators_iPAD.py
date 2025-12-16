"""
单元测试：validators/iPAD.py

测试 iPAD 心理测试相关验证函数。
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


class iPADTests(unittest.TestCase):
    """测试 iPAD.py 中的各验证函数"""

    # ========== is_between_0_and_1000 ==========
    def test_is_between_0_and_1000_valid_min(self):
        """测试最小值 0"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_valid_max(self):
        """测试最大值 1000"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(1000)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_valid_middle(self):
        """测试中间值 500"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(500)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_valid_small(self):
        """测试小值 1"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_valid_large(self):
        """测试大值 999"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(999)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_string_number(self):
        """测试字符串数字 '123'"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature("123")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_string_zero(self):
        """测试字符串 '0'"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature("0")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_invalid_negative(self):
        """测试负数"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(1001)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_invalid_large_exceed(self):
        """测试远超上限"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(5000)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_invalid_string(self):
        """测试无效字符串"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature("abc")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_invalid_none(self):
        """测试 None 值"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(None)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_invalid_empty_string(self):
        """测试空字符串"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature("")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_decimal_rounded(self):
        """测试小数（将被转换为整数）"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(500.9)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        # 500.9 转为 int 是 500，应该通过
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_boundary_minus_one(self):
        """测试边界值 -1（无效）"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_boundary_plus_one(self):
        """测试边界值 1001（无效）"""
        feature_key = "35435:心理-iPAD:IED_Test_IEDYSTCO"

        payload = {feature_key: make_feature(1001)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)


if __name__ == "__main__":
    unittest.main()
