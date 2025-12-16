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
    def test_is_float(self):
        valid_key = "1426:DXA体成分-体成分高分辨率数字成像化系统:BSM11__Body_shape_model_11"
        invalid_key = "1437:DXA体成分-体成分高分辨率数字成像化系统:腰椎1_Z-值评分"
        payload = {
            valid_key: make_feature("5"),
            invalid_key: make_feature("fk"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[valid_key]["abnormal"], 0)
        self.assertEqual(result[invalid_key]["abnormal"], 1)
    
    def test_is_non_negative(self):
        valid_key = "10631:影像-CT-chest:original_firstorder_Variance(右)"
        invalid_key = "10921:影像-CT-chest:original_glcm_MCC(左)"
        payload = {
            valid_key: make_feature("5"),
            invalid_key: make_feature("-5"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[valid_key]["abnormal"], 0)
        self.assertEqual(result[invalid_key]["abnormal"], 1)

    def test_is_between_0_and_1(self):
        key = "10633:影像-CT-chest:original_shape_Elongation(右)"
        payload = {
            key: make_feature("0.5"),
            "11335:影像-CT-chest:original_glszm_ZonePercentage(左)": make_feature("3"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 0)
        self.assertEqual(result["11335:影像-CT-chest:original_glszm_ZonePercentage(左)"]["abnormal"], 1)

    def test_is_between_n1_and_p1(self):
        valid_key = "10921:影像-CT-chest:original_glcm_MCC(左)"
        invalid_key = "1429:DXA体成分-体成分高分辨率数字成像化系统:BSM25__Body_shape_model_25"
        payload = {
            valid_key: make_feature("0.5"),
            invalid_key: make_feature("-5"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[valid_key]["abnormal"], 0)
        self.assertEqual(result[invalid_key]["abnormal"], 1)

    def test_make_in_interval(self):
        valid_key = "1961:DXA体成分-体成分高分辨率数字成像化系统:theta(右)"
        invalid_key = "1991:DXA体成分-体成分高分辨率数字成像化系统:阿尔法角(右)"
        payload = {
            valid_key: make_feature("50"),
            invalid_key: make_feature("700"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[valid_key]["abnormal"], 0)
        self.assertEqual(result[invalid_key]["abnormal"], 1)

    def test_default_check_allows_unregistered_feature(self):
        key = "未注册的特征"
        payload = {key: make_feature(None)}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 0)


if __name__ == "__main__":
    unittest.main()