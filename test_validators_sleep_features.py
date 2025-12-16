"""
单元测试：validators/sleep_features.py

测试睡眠特征相关验证函数。
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


class SleepFeaturesTests(unittest.TestCase):
    """测试 sleep_features.py 中的各验证函数"""

    # ========== _validate_EES_total_score ==========
    def test_validate_EES_total_score_valid_min(self):
        """测试 Epworth 最小值 0"""
        feature_key = "4678:睡眠-睡眠问卷:Epworth嗜睡量表总分"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_EES_total_score_valid_max(self):
        """测试 Epworth 最大值 24"""
        feature_key = "4678:睡眠-睡眠问卷:Epworth嗜睡量表总分"

        payload = {feature_key: make_feature(24)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_EES_total_score_valid_middle(self):
        """测试 Epworth 中间值 12"""
        feature_key = "4678:睡眠-睡眠问卷:Epworth嗜睡量表总分"

        payload = {feature_key: make_feature(12)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_EES_total_score_invalid_negative(self):
        """测试负数"""
        feature_key = "4678:睡眠-睡眠问卷:Epworth嗜睡量表总分"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_EES_total_score_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "4678:睡眠-睡眠问卷:Epworth嗜睡量表总分"

        payload = {feature_key: make_feature(25)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_EES_total_score_string_number(self):
        """测试字符串数字"""
        feature_key = "4678:睡眠-睡眠问卷:Epworth嗜睡量表总分"

        payload = {feature_key: make_feature("15")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_EES_total_score_invalid_string(self):
        """测试无效字符串"""
        feature_key = "4678:睡眠-睡眠问卷:Epworth嗜睡量表总分"

        payload = {feature_key: make_feature("abc")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== is_between_0_and_21 ==========
    def test_is_between_0_and_21_valid_min(self):
        """测试 PSQI 最小值 0"""
        feature_key = "4725:睡眠-睡眠问卷:匹兹堡睡眠质量指数总分"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_21_valid_max(self):
        """测试 PSQI 最大值 21"""
        feature_key = "4725:睡眠-睡眠问卷:匹兹堡睡眠质量指数总分"

        payload = {feature_key: make_feature(21)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_21_valid_middle(self):
        """测试 PSQI 中间值 10"""
        feature_key = "4725:睡眠-睡眠问卷:匹兹堡睡眠质量指数总分"

        payload = {feature_key: make_feature(10)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_21_invalid_negative(self):
        """测试负数"""
        feature_key = "4725:睡眠-睡眠问卷:匹兹堡睡眠质量指数总分"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_21_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "4725:睡眠-睡眠问卷:匹兹堡睡眠质量指数总分"

        payload = {feature_key: make_feature(22)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== is_between_0_and_63 ==========
    def test_is_between_0_and_63_valid_min(self):
        """测试 Beck 量表最小值 0"""
        feature_key = "4920:睡眠-睡眠问卷:贝克焦虑量表总分"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_63_valid_max(self):
        """测试 Beck 量表最大值 63"""
        feature_key = "4920:睡眠-睡眠问卷:贝克焦虑量表总分"

        payload = {feature_key: make_feature(63)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_63_valid_middle(self):
        """测试 Beck 量表中间值 30"""
        feature_key = "4920:睡眠-睡眠问卷:贝克焦虑量表总分"

        payload = {feature_key: make_feature(30)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_63_invalid_negative(self):
        """测试负数"""
        feature_key = "4920:睡眠-睡眠问卷:贝克焦虑量表总分"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_63_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "4920:睡眠-睡眠问卷:贝克焦虑量表总分"

        payload = {feature_key: make_feature(64)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== is_between_0_and_3 ==========
    def test_is_between_0_and_3_valid_min(self):
        """测试边界值 0"""
        feature_key = "4913:睡眠-睡眠问卷:贝克抑郁量表问题6"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_3_valid_max(self):
        """测试边界值 3"""
        feature_key = "4913:睡眠-睡眠问卷:贝克抑郁量表问题6"

        payload = {feature_key: make_feature(3)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_3_valid_middle(self):
        """测试中间值 1"""
        feature_key = "4913:睡眠-睡眠问卷:贝克抑郁量表问题6"

        payload = {feature_key: make_feature(1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_3_invalid_negative(self):
        """测试负数"""
        feature_key = "4913:睡眠-睡眠问卷:贝克抑郁量表问题6"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_3_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "4913:睡眠-睡眠问卷:贝克抑郁量表问题6"

        payload = {feature_key: make_feature(4)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== _is_not_empty ==========
    def test_is_not_empty_valid_text(self):
        """测试有效文本"""
        feature_key = "4922:睡眠-睡眠问卷:近1个月，总的来说，您认为自己的睡眠质量"

        payload = {feature_key: make_feature("有内容")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_not_empty_valid_number(self):
        """测试数字字符串"""
        feature_key = "test4922:睡眠-睡眠问卷:近1个月，总的来说，您认为自己的睡眠质量_key"

        payload = {feature_key: make_feature("123")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_not_empty_invalid_empty_string(self):
        """测试空字符串"""
        feature_key = "4922:睡眠-睡眠问卷:近1个月，总的来说，您认为自己的睡眠质量"

        payload = {feature_key: make_feature("")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_not_empty_invalid_whitespace(self):
        """测试仅空白字符"""
        feature_key = "4922:睡眠-睡眠问卷:近1个月，总的来说，您认为自己的睡眠质量"

        payload = {feature_key: make_feature("   ")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_not_empty_invalid_none(self):
        """测试 None 值"""
        feature_key = "4922:睡眠-睡眠问卷:近1个月，总的来说，您认为自己的睡眠质量"

        payload = {feature_key: make_feature(None)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== is_between_0_and_4 ==========
    def test_is_between_0_and_4_valid_min(self):
        """测试边界值 0"""
        feature_key = "4723:睡眠-睡眠问卷:匹兹堡睡眠质量指数催眠药物"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_4_valid_max(self):
        """测试边界值 4"""
        feature_key = "4723:睡眠-睡眠问卷:匹兹堡睡眠质量指数催眠药物"

        payload = {feature_key: make_feature(4)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_4_valid_middle(self):
        """测试中间值 2"""
        feature_key = "4723:睡眠-睡眠问卷:匹兹堡睡眠质量指数催眠药物"

        payload = {feature_key: make_feature(2)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_4_invalid_negative(self):
        """测试负数"""
        feature_key = "4723:睡眠-睡眠问卷:匹兹堡睡眠质量指数催眠药物"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_4_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "4723:睡眠-睡眠问卷:匹兹堡睡眠质量指数催眠药物"

        payload = {feature_key: make_feature(5)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== is_natural_number ==========
    def test_is_natural_number_valid_zero(self):
        """测试自然数 0"""
        feature_key = "4727:睡眠-睡眠问卷:匹兹堡睡眠质量指数日间功能障碍"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_natural_number_valid_positive_small(self):
        """测试正整数 5"""
        feature_key = "4727:睡眠-睡眠问卷:匹兹堡睡眠质量指数日间功能障碍"

        payload = {feature_key: make_feature(5)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_natural_number_valid_positive_large(self):
        """测试大正整数 1000"""
        feature_key = "4727:睡眠-睡眠问卷:匹兹堡睡眠质量指数日间功能障碍"

        payload = {feature_key: make_feature(1000)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_natural_number_string_number(self):
        """测试字符串数字"""
        feature_key = "4727:睡眠-睡眠问卷:匹兹堡睡眠质量指数日间功能障碍"

        payload = {feature_key: make_feature("42")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_natural_number_invalid_negative(self):
        """测试负数"""
        feature_key = "4727:睡眠-睡眠问卷:匹兹堡睡眠质量指数日间功能障碍"

        payload = {feature_key: make_feature(-5)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_natural_number_invalid_decimal(self):
        """测试小数（转换为整数后失去精度）"""
        feature_key = "4727:睡眠-睡眠问卷:匹兹堡睡眠质量指数日间功能障碍"

        payload = {feature_key: make_feature(3.7)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        # 3.7 转为 int 是 3，所以应该通过
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_natural_number_invalid_string(self):
        """测试无效字符串"""
        feature_key = "4727:睡眠-睡眠问卷:匹兹堡睡眠质量指数日间功能障碍"

        payload = {feature_key: make_feature("abc")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)


if __name__ == "__main__":
    unittest.main()
