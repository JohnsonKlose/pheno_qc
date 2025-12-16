"""
单元测试：validators/sleep_instrument_monitoring.py

测试睡眠仪器监测相关验证函数。
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


class SleepInstrumentMonitoringTests(unittest.TestCase):
    """测试 sleep_instrument_monitoring.py 中的各验证函数"""

    # ========== is_between_0_and_1000 ==========
    def test_is_between_0_and_1000_valid_min(self):
        """测试最小值 0"""
        feature_key = "37147:睡眠-睡眠仪器和监控中心:REM睡眠潜伏期(min)"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_valid_max(self):
        """测试最大值 1000"""
        feature_key = "37147:睡眠-睡眠仪器和监控中心:REM睡眠潜伏期(min)"

        payload = {feature_key: make_feature(1000)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_valid_middle(self):
        """测试中间值 500"""
        feature_key = "37147:睡眠-睡眠仪器和监控中心:REM睡眠潜伏期(min)"

        payload = {feature_key: make_feature(500)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_is_between_0_and_1000_invalid_negative(self):
        """测试负数"""
        feature_key = "37147:睡眠-睡眠仪器和监控中心:REM睡眠潜伏期(min)"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_is_between_0_and_1000_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "37147:睡眠-睡眠仪器和监控中心:REM睡眠潜伏期(min)"

        payload = {feature_key: make_feature(1001)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    # ========== _validate_hundred_scale_score ==========
    def test_validate_hundred_scale_score_valid_min(self):
        """测试最小值 0"""
        feature_key = "37149:睡眠-睡眠仪器和监控中心:SpO2概况-清醒期平均SpO2(%)"

        payload = {feature_key: make_feature(0)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_valid_max(self):
        """测试最大值 100"""
        feature_key = "37149:睡眠-睡眠仪器和监控中心:SpO2概况-清醒期平均SpO2(%)"

        payload = {feature_key: make_feature(100)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_valid_decimal(self):
        """测试小数 66.6"""
        feature_key = "37149:睡眠-睡眠仪器和监控中心:SpO2概况-清醒期平均SpO2(%)"

        payload = {feature_key: make_feature(66.6)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 0)

    def test_validate_hundred_scale_score_invalid_negative(self):
        """测试负数"""
        feature_key = "37149:睡眠-睡眠仪器和监控中心:SpO2概况-清醒期平均SpO2(%)"

        payload = {feature_key: make_feature(-1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

    def test_validate_hundred_scale_score_invalid_exceed(self):
        """测试超过上限"""
        feature_key = "37149:睡眠-睡眠仪器和监控中心:SpO2概况-清醒期平均SpO2(%)"

        payload = {feature_key: make_feature(100.1)}

        qc = PhenoQCBase(payload)

        result = qc.evaluate()
        qc.evaluate()
        self.assertEqual(result[feature_key]["abnormal"], 1)

if __name__ == "__main__":
    unittest.main()