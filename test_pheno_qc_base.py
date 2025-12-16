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
        payload = {key: make_feature(_is_not_empty)}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 0)

    def test_na_exrna_validator_accepts_valid_log2rpm(self):
        """Test exRNA validator accepts valid log2RPM values including negatives."""
        valid_key = "61709:核酸-核酸-exRNA:5_8S_rRNA.1:rRNA:log2RPM"
        payload = {
            valid_key: make_feature("-5.5"),
            "61710:核酸-核酸-exRNA:5_8S_rRNA.2:rRNA:log2RPM": make_feature("3.2"),
            "61711:核酸-核酸-exRNA:A2M:protein_coding:log2RPM": make_feature("-6.64385618977472"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[valid_key]["abnormal"], 0)
        self.assertEqual(result["61710:核酸-核酸-exRNA:5_8S_rRNA.2:rRNA:log2RPM"]["abnormal"], 0)
        self.assertEqual(result["61711:核酸-核酸-exRNA:A2M:protein_coding:log2RPM"]["abnormal"], 0)

    def test_na_exrna_validator_marks_out_of_range(self):
        """Test exRNA validator marks out-of-range values as abnormal."""
        key = "61709:核酸-核酸-exRNA:5_8S_rRNA.1:rRNA:log2RPM"
        payload = {
            key: make_feature("50"),
            "61710:核酸-核酸-exRNA:5_8S_rRNA.2:rRNA:log2RPM": make_feature("-50"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["61710:核酸-核酸-exRNA:5_8S_rRNA.2:rRNA:log2RPM"]["abnormal"], 1)

    def test_na_exrna_validator_marks_non_numeric(self):
        """Test exRNA validator marks non-numeric values as abnormal."""
        key = "61709:核酸-核酸-exRNA:5_8S_rRNA.1:rRNA:log2RPM"
        payload = {key: make_feature("not_a_number")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    def test_na_wholeblood_validator_accepts_valid_log2fpkm(self):
        """Test wholeblood validator accepts valid log2FPKM values including negatives."""
        valid_key = "37804:核酸-核酸-WholeBlood:A1BG:ENSG00000121410:log2FPKM"
        payload = {
            valid_key: make_feature("-0.604"),
            "37806:核酸-核酸-WholeBlood:A2M:ENSG00000175899:log2FPKM": make_feature("2.5"),
            "37807:核酸-核酸-WholeBlood:A2MP1:ENSG00000256069:log2FPKM": make_feature("-6.64385618977472"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[valid_key]["abnormal"], 0)
        self.assertEqual(result["37806:核酸-核酸-WholeBlood:A2M:ENSG00000175899:log2FPKM"]["abnormal"], 0)
        self.assertEqual(result["37807:核酸-核酸-WholeBlood:A2MP1:ENSG00000256069:log2FPKM"]["abnormal"], 0)

    def test_na_wholeblood_validator_marks_out_of_range(self):
        """Test wholeblood validator marks out-of-range values as abnormal."""
        key = "37804:核酸-核酸-WholeBlood:A1BG:ENSG00000121410:log2FPKM"
        payload = {
            key: make_feature("50"),
            "37806:核酸-核酸-WholeBlood:A2M:ENSG00000175899:log2FPKM": make_feature("-50"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["37806:核酸-核酸-WholeBlood:A2M:ENSG00000175899:log2FPKM"]["abnormal"], 1)

    def test_na_wholeblood_validator_marks_non_numeric(self):
        """Test wholeblood validator marks non-numeric values as abnormal."""
        key = "37804:核酸-核酸-WholeBlood:A1BG:ENSG00000121410:log2FPKM"
        payload = {key: make_feature("invalid_value")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    # ========== molecule_aminometabolites.py tests ==========
    def test_molecule_aminometabolites_validator_accepts_valid_concentrations(self):
        """Test aminometabolites validator accepts valid concentration values."""
        key1 = "4961:分子代谢-分子代谢-AminoMetabolites:(±)-Octopamine(μmol/L)"
        key2 = "4962:分子代谢-分子代谢-AminoMetabolites:1,2-Diaminopropane(μmol/L)"
        payload = {
            key1: make_feature("0.007"),
            key2: make_feature("100"),
            "4963:分子代谢-分子代谢-AminoMetabolites:1,3-Diaminopropane(μmol/L)": make_feature("5000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key1]["abnormal"], 0)
        self.assertEqual(result[key2]["abnormal"], 0)
        self.assertEqual(result["4963:分子代谢-分子代谢-AminoMetabolites:1,3-Diaminopropane(μmol/L)"]["abnormal"], 0)

    def test_molecule_aminometabolites_validator_marks_out_of_range(self):
        """Test aminometabolites validator marks out-of-range values as abnormal."""
        key = "4961:分子代谢-分子代谢-AminoMetabolites:(±)-Octopamine(μmol/L)"
        payload = {
            key: make_feature("-10"),
            "4962:分子代谢-分子代谢-AminoMetabolites:1,2-Diaminopropane(μmol/L)": make_feature("15000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["4962:分子代谢-分子代谢-AminoMetabolites:1,2-Diaminopropane(μmol/L)"]["abnormal"], 1)

    def test_molecule_aminometabolites_validator_marks_non_numeric(self):
        """Test aminometabolites validator marks non-numeric values as abnormal."""
        key = "4961:分子代谢-分子代谢-AminoMetabolites:(±)-Octopamine(μmol/L)"
        payload = {key: make_feature("not_a_number")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    # ========== molecule_bileacidsserum.py tests ==========
    def test_molecule_bileacidsserum_validator_accepts_valid_concentrations(self):
        """Test bile acids serum validator accepts valid concentration values."""
        key1 = "5068:分子代谢-分子代谢-BileAcidsSerum:12-Ketodeoxycholic_acid(nM)"
        key2 = "5069:分子代谢-分子代谢-BileAcidsSerum:3,7-Dihydroxy-5-cholestenoic_acid(nM)"
        payload = {
            key1: make_feature("12.5"),
            key2: make_feature("500"),
            "5070:分子代谢-分子代谢-BileAcidsSerum:3-ketolithocholic_acid(nM)": make_feature("50000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key1]["abnormal"], 0)
        self.assertEqual(result[key2]["abnormal"], 0)
        self.assertEqual(result["5070:分子代谢-分子代谢-BileAcidsSerum:3-ketolithocholic_acid(nM)"]["abnormal"], 0)

    def test_molecule_bileacidsserum_validator_marks_out_of_range(self):
        """Test bile acids serum validator marks out-of-range values as abnormal."""
        key = "5068:分子代谢-分子代谢-BileAcidsSerum:12-Ketodeoxycholic_acid(nM)"
        payload = {
            key: make_feature("-5"),
            "5069:分子代谢-分子代谢-BileAcidsSerum:3,7-Dihydroxy-5-cholestenoic_acid(nM)": make_feature("150000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["5069:分子代谢-分子代谢-BileAcidsSerum:3,7-Dihydroxy-5-cholestenoic_acid(nM)"]["abnormal"], 1)

    def test_molecule_bileacidsserum_validator_marks_non_numeric(self):
        """Test bile acids serum validator marks non-numeric values as abnormal."""
        key = "5068:分子代谢-分子代谢-BileAcidsSerum:12-Ketodeoxycholic_acid(nM)"
        payload = {key: make_feature("invalid")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    # ========== molecule_carnitinemetabolites.py tests ==========
    def test_molecule_carnitinemetabolites_validator_accepts_valid_concentrations(self):
        """Test carnitine metabolites validator accepts valid concentration values."""
        key1 = "5096:分子代谢-分子代谢-CarnitineMetabolites:3-dehydroxycarnitine(nM)"
        key2 = "5097:分子代谢-分子代谢-CarnitineMetabolites:C0(nM)"
        payload = {
            key1: make_feature("1000"),
            key2: make_feature("73773"),
            "5098:分子代谢-分子代谢-CarnitineMetabolites:C1-Phe(nM)": make_feature("500000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key1]["abnormal"], 0)
        self.assertEqual(result[key2]["abnormal"], 0)
        self.assertEqual(result["5098:分子代谢-分子代谢-CarnitineMetabolites:C1-Phe(nM)"]["abnormal"], 0)

    def test_molecule_carnitinemetabolites_validator_marks_out_of_range(self):
        """Test carnitine metabolites validator marks out-of-range values as abnormal."""
        key = "5096:分子代谢-分子代谢-CarnitineMetabolites:3-dehydroxycarnitine(nM)"
        payload = {
            key: make_feature("-100"),
            "5097:分子代谢-分子代谢-CarnitineMetabolites:C0(nM)": make_feature("2000000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["5097:分子代谢-分子代谢-CarnitineMetabolites:C0(nM)"]["abnormal"], 1)

    def test_molecule_carnitinemetabolites_validator_marks_non_numeric(self):
        """Test carnitine metabolites validator marks non-numeric values as abnormal."""
        key = "5096:分子代谢-分子代谢-CarnitineMetabolites:3-dehydroxycarnitine(nM)"
        payload = {key: make_feature("NaN")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    # ========== molecule_elements.py tests ==========
    def test_molecule_elements_validator_accepts_valid_concentrations(self):
        """Test elements validator accepts valid concentration values."""
        key1 = "5228:分子代谢-分子代谢-Elements:107_Ag(μg/L)"
        key2 = "5229:分子代谢-分子代谢-Elements:11_B(μg/L)"
        payload = {
            key1: make_feature("0.07"),
            key2: make_feature("11.8"),
            "5230:分子代谢-分子代谢-Elements:123_Sb(μg/L)": make_feature("5000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key1]["abnormal"], 0)
        self.assertEqual(result[key2]["abnormal"], 0)
        self.assertEqual(result["5230:分子代谢-分子代谢-Elements:123_Sb(μg/L)"]["abnormal"], 0)

    def test_molecule_elements_validator_marks_out_of_range(self):
        """Test elements validator marks out-of-range values as abnormal."""
        key = "5228:分子代谢-分子代谢-Elements:107_Ag(μg/L)"
        payload = {
            key: make_feature("-1"),
            "5229:分子代谢-分子代谢-Elements:11_B(μg/L)": make_feature("15000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["5229:分子代谢-分子代谢-Elements:11_B(μg/L)"]["abnormal"], 1)

    def test_molecule_elements_validator_marks_non_numeric(self):
        """Test elements validator marks non-numeric values as abnormal."""
        key = "5228:分子代谢-分子代谢-Elements:107_Ag(μg/L)"
        payload = {key: make_feature("text")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    # ========== molecule_lipid.py tests ==========
    def test_molecule_lipid_validator_accepts_valid_concentrations(self):
        """Test lipid validator accepts valid concentration values (updated limit: 10,000)."""
        key1 = "5259:分子代谢-分子代谢-Lipid:ACar_(0:0)(μmol/L)"
        key2 = "5260:分子代谢-分子代谢-Lipid:ACar_(10:0)-iso1(μmol/L)"
        payload = {
            key1: make_feature("0.76"),
            key2: make_feature("500"),
            "5261:分子代谢-分子代谢-Lipid:ACar_(10:0-DC)-iso1(μmol/L)": make_feature("2500"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key1]["abnormal"], 0)
        self.assertEqual(result[key2]["abnormal"], 0)
        self.assertEqual(result["5261:分子代谢-分子代谢-Lipid:ACar_(10:0-DC)-iso1(μmol/L)"]["abnormal"], 0)

    def test_molecule_lipid_validator_marks_out_of_range(self):
        """Test lipid validator marks out-of-range values as abnormal (new limit: 10,000)."""
        key = "5259:分子代谢-分子代谢-Lipid:ACar_(0:0)(μmol/L)"
        payload = {
            key: make_feature("-5"),
            "5260:分子代谢-分子代谢-Lipid:ACar_(10:0)-iso1(μmol/L)": make_feature("10001"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["5260:分子代谢-分子代谢-Lipid:ACar_(10:0)-iso1(μmol/L)"]["abnormal"], 1)

    def test_molecule_lipid_validator_marks_non_numeric(self):
        """Test lipid validator marks non-numeric values as abnormal."""
        key = "5259:分子代谢-分子代谢-Lipid:ACar_(0:0)(μmol/L)"
        payload = {key: make_feature("invalid_lipid")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    # ========== molecule_lipoprotein.py tests ==========
    def test_molecule_lipoprotein_validator_accepts_valid_values(self):
        """Test lipoprotein validator accepts valid values (ratios, concentrations)."""
        key1 = "6630:分子代谢-分子代谢-lipoprotein:ABA1R"
        key2 = "6631:分子代谢-分子代谢-lipoprotein:ABHCR"
        payload = {
            key1: make_feature("0.55"),
            key2: make_feature("1.3"),
            "6632:分子代谢-分子代谢-lipoprotein:ABPN": make_feature("1500"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key1]["abnormal"], 0)
        self.assertEqual(result[key2]["abnormal"], 0)
        self.assertEqual(result["6632:分子代谢-分子代谢-lipoprotein:ABPN"]["abnormal"], 0)

    def test_molecule_lipoprotein_validator_marks_out_of_range(self):
        """Test lipoprotein validator marks out-of-range values as abnormal."""
        key = "6630:分子代谢-分子代谢-lipoprotein:ABA1R"
        payload = {
            key: make_feature("-1"),
            "6631:分子代谢-分子代谢-lipoprotein:ABHCR": make_feature("15000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["6631:分子代谢-分子代谢-lipoprotein:ABHCR"]["abnormal"], 1)

    def test_molecule_lipoprotein_validator_marks_non_numeric(self):
        """Test lipoprotein validator marks non-numeric values as abnormal."""
        key = "6630:分子代谢-分子代谢-lipoprotein:ABA1R"
        payload = {key: make_feature("not_numeric")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    # ========== molecule_smallmolecule.py tests ==========
    def test_molecule_smallmolecule_validator_accepts_valid_values(self):
        """Test small molecule validator accepts both concentrations and peak areas."""
        key1 = "6932:分子代谢-分子代谢-smallMolecule:2_ABA"
        key2 = "6933:分子代谢-分子代谢-smallMolecule:2_HBA"
        payload = {
            key1: make_feature("35"),
            key2: make_feature("500"),
            "6934:分子代谢-分子代谢-smallMolecule:2_KG": make_feature("60000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key1]["abnormal"], 0)
        self.assertEqual(result[key2]["abnormal"], 0)
        self.assertEqual(result["6934:分子代谢-分子代谢-smallMolecule:2_KG"]["abnormal"], 0)

    def test_molecule_smallmolecule_validator_marks_out_of_range(self):
        """Test small molecule validator marks out-of-range values as abnormal."""
        key = "6932:分子代谢-分子代谢-smallMolecule:2_ABA"
        payload = {
            key: make_feature("-10"),
            "6933:分子代谢-分子代谢-smallMolecule:2_HBA": make_feature("150000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["6933:分子代谢-分子代谢-smallMolecule:2_HBA"]["abnormal"], 1)

    def test_molecule_smallmolecule_validator_marks_non_numeric(self):
        """Test small molecule validator marks non-numeric values as abnormal."""
        key = "6932:分子代谢-分子代谢-smallMolecule:2_ABA"
        payload = {key: make_feature("abc123")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)

    # ========== molecule_sterolmetabolites.py tests ==========
    def test_molecule_sterolmetabolites_validator_accepts_valid_concentrations(self):
        """Test sterol metabolites validator accepts valid concentration values."""
        key1 = "6604:分子代谢-分子代谢-SterolMetabolites:11-Deoxycortisol(uM)"
        key2 = "6605:分子代谢-分子代谢-SterolMetabolites:11-Hydroxyandrostenedione(uM)"
        payload = {
            key1: make_feature("0.003"),
            key2: make_feature("0.046"),
            "6606:分子代谢-分子代谢-SterolMetabolites:16α_-Hydroxyestrone(uM)": make_feature("2000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key1]["abnormal"], 0)
        self.assertEqual(result[key2]["abnormal"], 0)
        self.assertEqual(result["6606:分子代谢-分子代谢-SterolMetabolites:16α_-Hydroxyestrone(uM)"]["abnormal"], 0)

    def test_molecule_sterolmetabolites_validator_marks_out_of_range(self):
        """Test sterol metabolites validator marks out-of-range values as abnormal."""
        key = "6604:分子代谢-分子代谢-SterolMetabolites:11-Deoxycortisol(uM)"
        payload = {
            key: make_feature("-5"),
            "6605:分子代谢-分子代谢-SterolMetabolites:11-Hydroxyandrostenedione(uM)": make_feature("15000"),
        }

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)
        self.assertEqual(result["6605:分子代谢-分子代谢-SterolMetabolites:11-Hydroxyandrostenedione(uM)"]["abnormal"], 1)

    def test_molecule_sterolmetabolites_validator_marks_non_numeric(self):
        """Test sterol metabolites validator marks non-numeric values as abnormal."""
        key = "6604:分子代谢-分子代谢-SterolMetabolites:11-Deoxycortisol(uM)"
        payload = {key: make_feature("not_valid")}

        result = PhenoQCBase(payload).evaluate()

        self.assertEqual(result[key]["abnormal"], 1)


if __name__ == "__main__":
    unittest.main()
