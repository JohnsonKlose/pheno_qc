import unittest

from pheno_qc_base import PhenoQCBase


def make_feature(final_value, feature_name="示例特征", description="示例描述"):
    """构造最小化的 feature payload，用于测试。"""
    return {
        "feature_name": feature_name,
        "metadata": {"description": description},
        "value_trace": {"final": {"value": final_value}},
        "processing_context": {"method_name": "单元测试"},
    }


class PhenoQCBaseTests(unittest.TestCase):
    
    def test_yes_no_validator(self):
        key = "3786:人体能量代谢-人体能量代谢:呼吸交换率"
        payload = {
            key: make_feature("Na"),
            "2693:细胞-细胞-Morphology:SSC_MFI_in_P1_pDCs": make_feature(0.5),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["2693:细胞-细胞-Morphology:SSC_MFI_in_P1_pDCs"]["abnormal"], 0)

        
    def test_default_check_allows_unregistered_feature(self):
        key = "未注册的特征"
        payload = {key: make_feature(None)}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 0)


    def test_is_nature(self):
        key = "3787:人体能量代谢-人体能量代谢:摄氧量(ml/min)"
        payload = {key: make_feature(-1)}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 0)


if __name__ == "__main__":
    unittest.main()
