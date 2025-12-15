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
    def test_exact_age_validator_marks_out_of_range(self):
        valid_key = "3845:健康问卷调查-问卷-1:开始年龄"
        invalid_key = "3884:健康问卷调查-问卷-1:结束年龄"
        payload = {
            valid_key: make_feature("30"),
            invalid_key: make_feature("130"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[valid_key]["abnormal"], 0)
        self.assertEqual(result[invalid_key]["abnormal"], 1)
        self.assertEqual(result[valid_key]["final_value"], "30")

    def test_prefix_validator_applies_for_child_questions(self):
        key = "3796:健康问卷调查-问卷-1:从多少岁起喝酒"
        payload = {key: make_feature("abc")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    def test_yes_no_validator(self):
        key = "3891:健康问卷调查-问卷-1:饮酒习惯影响正常的生活"
        payload = {
            key: make_feature("是"),
            "3894:健康问卷调查-问卷-1:饮酒后感到失望": make_feature("maybe"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 0)
        self.assertEqual(result["3894:健康问卷调查-问卷-1:饮酒后感到失望"]["abnormal"], 1)

    def test_default_check_allows_unregistered_feature(self):
        key = "未注册的特征"
        payload = {key: make_feature(None)}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 0)


if __name__ == "__main__":
    unittest.main()
