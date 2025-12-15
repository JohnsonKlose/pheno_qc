import unittest
from pheno_qc_base import PhenoQCBase

def make_feature(final_value, feature_name="骨超声特征"):
    """构造最小化的 feature payload，模拟系统输入格式。"""
    return {
        "feature_name": feature_name,
        "metadata": {"description": "骨超声自动校验测试"},
        "value_trace": {"final": {"value": final_value}},
        "processing_context": {"method_name": "单元测试"},
    }

class BoneUltrasoundQCTests(unittest.TestCase):
    
    # 1. 测试 SOS (声波速度) - 范围: 1000 - 2000
    def test_sos_validator(self):
        """测试SOS正常范围"""
        key = "11701:超声-跟骨超声:SOS"
        normal_values = ["1450.5", "1500", "1600.25", "1550"]
        
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"SOS正常值{val}应通过校验")
    
        extreme_values = ["999", "2001", "-100", "0", "", "nan", "abc"]
        
        for val in extreme_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"SOS异常值{val}应被标记")

    # 2. 测试 T值/Z值 - 范围: -10 到 10
    # ===== 骨强度测试 =====
    def test_bone_strength_validator(self):
        """测试骨强度校验"""
        key = "11702:超声-跟骨超声:骨强度"
        
        # 正常值
        normal_cases = ["80.5", "100", "150", "0"]
        for val in normal_cases:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"骨强度正常值{val}应通过校验")
        
        # 异常值
        abnormal_cases = ["-101", "201", "abc", None]
        for val in abnormal_cases:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"骨强度异常值{val}应被标记")
    
    # ===== Z值/T值测试 =====
    def test_z_t_score_validator(self):
        """测试Z值/T值校验"""
        z_key = "11705:超声-跟骨超声:Z值"
        t_key = "11703:超声-跟骨超声:T值"
        
        # 正常范围
        normal_values = ["-2.5", "0", "1.2", "-3.0", "2.8"]
        for val in normal_values:
            for key in [z_key, t_key]:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 0, f"{key}正常值{val}应通过校验")
        
        # 异常范围
        abnormal_values = ["-11", "10.1", "25", "-25"]
        for val in abnormal_values:
            for key in [z_key, t_key]:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 1, f"{key}异常值{val}应被标记")
    
    # ===== 百分比测试 =====
    def test_percentage_validators(self):
        """测试百分比校验器"""
        young_key = "11704:超声-跟骨超声:%年轻成人"
        age_key = "11706:超声-跟骨超声:%年龄匹配"
        
        # 正常百分比
        normal_percent = ["85.5", "100", "120", "50", "200"]
        for val in normal_percent:
            for key in [young_key, age_key]:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 0, f"{key}正常值{val}应通过校验")
        
        # 异常百分比
        abnormal_percent = ["-1", "251", "300", "-10"]
        for val in abnormal_percent:
            for key in [young_key, age_key]:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 1, f"{key}异常值{val}应被标记")
    
    # ===== BUA测试 =====
    def test_bua_validator(self):
        """测试BUA校验"""
        key = "11721:超声-跟骨超声:BUA"
        
        # 正常BUA值
        normal_values = ["75.5", "100", "130", "20", "199"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"BUA正常值{val}应通过校验")
        
        # 异常BUA值
        abnormal_values = ["19", "201", "-1", "0", "abc"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"BUA异常值{val}应被标记")
    
    # ===== AIB测试 =====
    def test_aib_validator(self):
        """测试AIB校验（多个频率）"""
        aib_keys = [
            "11707:超声-骨超声:2.25MHz单脉冲左脚跟骨外侧超声表观积分背散射(AIB)",
            "11708:超声-骨超声:2.25MHz多脉冲左脚跟骨外侧超声表观积分背散射(AIB)",
            "11709:超声-骨超声:3.5MHz单脉冲左脚跟骨外侧超声表观积分背散射(AIB)",
            "11710:超声-骨超声:3.5MHz多脉冲左脚跟骨外侧超声表观积分背散射(AIB)",
        ]
        
        # 正常AIB值（负值）
        normal_values = ["-30.5", "-40", "-25.2", "-60", "-15"]
        for key in aib_keys:
            for val in normal_values:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 0, f"{key}正常值{val}应通过校验")
        
        # 异常AIB值
        abnormal_values = ["-71", "-9", "0", "10", "-5", "abc"]
        for key in aib_keys:
            for val in abnormal_values:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 1, f"{key}异常值{val}应被标记")
    
    # ===== FIAB测试 =====
    def test_fiab_validator(self):
        """测试FIAB校验"""
        fiab_keys = [
            "11722:超声-骨超声:3.5MHz单脉冲左脚跟骨外侧表观背散射零频截距(FIAB)",
            "11725:超声-骨超声:3.5MHz多脉冲左脚跟骨外侧表观背散射零频截距(FIAB)",
            "11738:超声-骨超声:2.25MHz多脉冲左脚跟骨外侧表观背散射零频截距(FIAB)",
            "11741:超声-骨超声:2.25MHz单脉冲左脚跟骨外侧表观背散射零频截距(FIAB)",
        ]
        
        # 正常FIAB值
        normal_values = ["-40.5", "-30", "-60", "-10.2"]
        for key in fiab_keys:
            for val in normal_values:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 0, f"{key}正常值{val}应通过校验")
        
        # 异常FIAB值
        abnormal_values = ["-81", "1", "10", "-100", "abc"]
        for key in fiab_keys:
            for val in abnormal_values:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 1, f"{key}异常值{val}应被标记")
    
    # ===== FSAB测试 =====
    def test_fsab_validator(self):
        """测试FSAB校验"""
        fsab_keys = [
            "11723:超声-骨超声:3.5MHz单脉冲左脚跟骨外侧表观背散射频率斜率(FSAB)",
            "11726:超声-骨超声:3.5MHz多脉冲左脚跟骨外侧表观背散射频率斜率(FSAB)",
            "11739:超声-骨超声:2.25MHz多脉冲左脚跟骨外侧表观背散射频率斜率(FSAB)",
            "11742:超声-骨超声:2.25MHz单脉冲左脚跟骨外侧表观背散射频率斜率(FSAB)",
        ]
        
        # 正常FSAB值（可正可负）
        normal_values = ["-5.5", "8.2", "0", "-15", "15", "10.5"]
        for key in fsab_keys:
            for val in normal_values:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 0, f"{key}正常值{val}应通过校验")
        
        # 异常FSAB值
        abnormal_values = ["-21", "21", "-30", "30", "abc"]
        for key in fsab_keys:
            for val in abnormal_values:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 1, f"{key}异常值{val}应被标记")
    
    # ===== SCS测试 =====
    def test_scs_validator(self):
        """测试SCS校验"""
        scs_keys = [
            "11724:超声-骨超声:3.5MHz单脉冲左脚跟骨外侧超声背散射频谱质心偏移(SCS)",
            "11727:超声-骨超声:3.5MHz多脉冲左脚跟骨外侧超声背散射频谱质心偏移(SCS)",
            "11740:超声-骨超声:2.25MHz多脉冲左脚跟骨外侧超声背散射频谱质心偏移(SCS)",
            "11743:超声-骨超声:2.25MHz单脉冲左脚跟骨外侧超声背散射频谱质心偏移(SCS)",
        ]
        
        # 正常SCS值
        normal_values = ["-200", "150", "0", "300", "-350", "250.5"]
        for key in scs_keys:
            for val in normal_values:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 0, f"{key}正常值{val}应通过校验")
        
        # 异常SCS值
        abnormal_values = ["-501", "501", "-600", "600", "abc"]
        for key in scs_keys:
            for val in abnormal_values:
                payload = {key: make_feature(val)}
                result = PhenoQCBase(payload).evaluate()
                self.assertEqual(result[key]["abnormal"], 1, f"{key}异常值{val}应被标记")

if __name__ == "__main__":
    unittest.main()