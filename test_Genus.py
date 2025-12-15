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


class MetagenomicsTests(unittest.TestCase):
    
    def test_pcoa_score_validator(self):
        """测试 PCoA 得分校验 (范围 -100 到 100)。"""
        key = "6989:宏基因组-宏基因组-DiversityIndice:Back_PCoA1_WeightedUniFrac"
        
        payload = {
            # 正常值
            key: make_feature("0.5"),
            # 边界值
            "valid_neg": make_feature("-99.9"),
            "valid_pos": make_feature("100"),
            # 异常值
            "invalid_high": make_feature("101"),
            "invalid_low": make_feature("-101"),
            "invalid_str": make_feature("not_a_number"),
        }
        
        # Batch 1: 正常值
        result = PhenoQCBase({key: make_feature("0.5")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 0, "0.5 应为有效 PCoA 得分")

        # Batch 2: 越界值
        result = PhenoQCBase({key: make_feature("150")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1, "150 超出 PCoA 范围")

        # Batch 3: 非数值
        result = PhenoQCBase({key: make_feature("NaN")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1, "字符串应被标记为异常")

    def test_genus_abundance_validator(self):
        """测试属水平丰度校验 (范围 0 到 1)。"""
        key = "7097:宏基因组-宏基因组-Genus:Back_d__Bacteria;__;__;__;__;__"

        # 正常情况
        result = PhenoQCBase({key: make_feature("0.0014")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 0)

        # 边界情况 1.0
        result = PhenoQCBase({key: make_feature("1.0")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 0)

        # 异常情况：大于 1
        result = PhenoQCBase({key: make_feature("1.00001")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1, "丰度大于 1 应标记异常")

        # 异常情况：负数
        result = PhenoQCBase({key: make_feature("-0.1")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1, "丰度不能为负")

    def test_species_abundance_validator(self):
        """测试物种水平丰度校验 (范围 0 到 100)。"""
        key = "10413:宏基因组-宏基因组-species:Actinomyces_graevenitzii"

        # 正常情况 (百分比)
        result = PhenoQCBase({key: make_feature("55.5")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 0)

        # 异常情况：大于 100
        result = PhenoQCBase({key: make_feature("101")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1, "物种丰度 > 100 应异常")

    def test_cytokine_validator(self):
        """测试细胞因子浓度 (范围 0 到 100,000)。"""
        key = "1406:生化-生化检测:Inflammatory_IFN-γ(pg/mL)"

        # 正常高值
        result = PhenoQCBase({key: make_feature("99999")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 0)

        # 异常极高值
        result = PhenoQCBase({key: make_feature("100001")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1)

    def test_metabolic_hormone_validator(self):
        """测试代谢激素浓度 (范围 0 到 1,000,000)。"""
        key = "1416:生化-生化检测:Metabolic_Active_GLP-1(pM)"

        # 正常范围
        result = PhenoQCBase({key: make_feature("500000")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 0)

        # 异常：负值
        result = PhenoQCBase({key: make_feature("-10")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1)

    def test_pathway_genus_abundance_reuse(self):
        """测试通路特征复用 Genus Abundance 规则 (范围 0-1)。"""
        # 注意：shengcheng.py 中 pathway 也是注册到 _validate_genus_abundance
        key = "9868:宏基因组-宏基因组-pathway:1CMET2_PWY"

        result = PhenoQCBase({key: make_feature("0.5")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 0)

        result = PhenoQCBase({key: make_feature("2.0")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1, "Pathway 使用 Genus 规则，大于 1 应异常")

    def test_missing_value_handling(self):
        """测试空值或 None 的处理。"""
        key = "7097:宏基因组-宏基因组-Genus:Back_d__Bacteria;__;__;__;__;__"
        
        # 空字符串
        result = PhenoQCBase({key: make_feature("")}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1, "空字符串应标记异常/无效")

        # None
        result = PhenoQCBase({key: make_feature(None)}).evaluate()
        self.assertEqual(result[key]["abnormal"], 1, "None 应标记异常/无效")


if __name__ == "__main__":
    unittest.main()