"""
单元测试：validators/otoacoustic_emission_tester.py

测试耳声发射测试相关验证函数。
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


class OtoacousticEmissionTesterTests(unittest.TestCase):
    """测试 otoacoustic_emission_tester.py 中的各验证函数"""

    # ========== is_SNR (信噪比) ==========
    def test_is_SNR_valid_min(self):
        """测试最小值 -100"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(-100)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_max(self):
        """测试最大值 100"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(100)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_zero(self):
        """测试零值"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_positive(self):
        """测试正值 50"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(50)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_negative(self):
        """测试负值 -50"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(-50)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_decimal_positive(self):
        """测试正小数 25.5"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(25.5)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_decimal_negative(self):
        """测试负小数 -25.5"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(-25.5)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_small_decimal(self):
        """测试小数 0.1"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(0.1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_near_min(self):
        """测试接近最小值 -99.9"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(-99.9)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_valid_near_max(self):
        """测试接近最大值 99.9"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(99.9)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_string_number_positive(self):
        """测试字符串数字 '45.5'"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature("45.5")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_string_number_negative(self):
        """测试字符串数字 '-30'"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature("-30")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_string_zero(self):
        """测试字符串 '0'"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature("0")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_SNR_invalid_exceed_positive(self):
        """测试超过正上限 100.1"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(100.1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_SNR_invalid_exceed_positive_large(self):
        """测试远超上限 200"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(200)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_SNR_invalid_exceed_negative(self):
        """测试超过负下限 -100.1"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(-100.1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_SNR_invalid_exceed_negative_large(self):
        """测试远低于下限 -200"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(-200)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_SNR_invalid_string(self):
        """测试无效字符串"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature("invalid")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_SNR_invalid_none(self):
        """测试 None 值"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature(None)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_SNR_invalid_empty_string(self):
        """测试空字符串"""
        feature_key = "35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"

        payload = {feature_key: make_feature("")}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)


if __name__ == "__main__":
    unittest.main()
