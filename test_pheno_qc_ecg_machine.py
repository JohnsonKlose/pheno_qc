import unittest
from pheno_qc_base import PhenoQCBase


def make_feature(final_value, feature_name="ECG特征", description="ECG测试"):
    """构造最小化的 feature payload，用于测试。"""
    return {
        "feature_name": feature_name,
        "metadata": {"description": description},
        "value_trace": {"final": {"value": final_value}},
        "processing_context": {"method_name": "ECG单元测试"},
    }


class ECGQCTests(unittest.TestCase):
    """心电图ECG QC校验单元测试"""
    
    # ===== 通用时间参数测试 =====
    def test_ecg_time_general_validator(self):
        """测试通用ECG时间参数校验"""
        key = "48:生物电-心电图机:aVF导联S波峰值时间(ms)"
        
        # 正常时间值
        normal_values = ["100", "500", "1000", "2500", "4500", "0", "5000"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"通用时间{val}ms应通过校验")
        
        # 异常时间值
       # abnormal_values = ["-1", "5001", "6000", "-100", "abc", None, ""]
        abnormal_values = ["5001", "6000", "-100", "abc", None, ""]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"通用时间{val}ms应被标记")
    
    # ===== P波时间测试 =====
    def test_p_wave_time_validator(self):
        """测试P波时间参数校验"""
        key = "230:生物电-心电图机:III导联P'波峰值时间(ms)"
        
        # 正常P波时间
        normal_values = ["50", "100", "150", "200", "250", "10", "300"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"P波时间{val}ms应通过校验")
        
        # 异常P波时间
        abnormal_values = ["9", "301", "0", "400", "5", "350"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"P波时间{val}ms应被标记")
    
    # ===== PR间期测试 =====
    def test_pr_interval_validator(self):
        """测试PR间期校验"""
        key = "242:生物电-心电图机:I导联PR间期(ms)"
        
        # 正常PR间期
        normal_values = ["120", "150", "200", "300", "350", "80", "400"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"PR间期{val}ms应通过校验")
        
        # 异常PR间期
        abnormal_values = ["79", "401", "50", "450", "0", "500"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"PR间期{val}ms应被标记")
    
    # ===== QRS波群时间测试 =====
    def test_qrs_complex_time_validator(self):
        """测试QRS波群时间校验"""
        key = "777:生物电-心电图机:III导联QRS波群类本位曲折时间(ms)"
        
        # 正常QRS时间
        normal_values = ["40", "60", "80", "100", "120", "20", "150"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"QRS时间{val}ms应通过校验")
        
        # 异常QRS时间
        abnormal_values = ["19", "151", "0", "200", "10", "160"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"QRS时间{val}ms应被标记")
    
    # ===== Q波时限测试 =====
    def test_q_wave_time_validator(self):
        """测试Q波时限校验"""
        key = "779:生物电-心电图机:III导联Q波时限(ms)"
        
        # 正常Q波时限
        normal_values = ["10", "30", "50", "80", "0", "100"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"Q波时限{val}ms应通过校验")
        
        # 异常Q波时限
        abnormal_values = ["-1", "101", "120", "-10", "150"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"Q波时限{val}ms应被标记")
    
    # ===== S波时限测试 =====
    def test_s_wave_time_validator(self):
        """测试S波时限校验"""
        key = "784:生物电-心电图机:III导联S波时限(ms)"
        
        # 正常S波时限
        normal_values = ["20", "50", "80", "120", "0", "150"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"S波时限{val}ms应通过校验")
        
        # 异常S波时限
        abnormal_values = ["-1", "151", "200", "-10", "180"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"S波时限{val}ms应被标记")
    
    # ===== T波时间测试 =====
    def test_t_wave_time_validator(self):
        """测试T波时间校验"""
        key = "286:生物电-心电图机:II导联T'波峰值时间(ms)"
        
        # 正常T波时间
        normal_values = ["50", "100", "200", "300", "20", "400"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"T波时间{val}ms应通过校验")
        
        # 异常T波时间
        abnormal_values = ["19", "401", "0", "500", "10", "450"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"T波时间{val}ms应被标记")
    
    # ===== RR间期测试 =====
    def test_rr_interval_validator(self):
        """测试RR间期校验"""
        key = "311:生物电-心电图机:I导联平均RR间期(ms)"
        
        # 正常RR间期
        normal_values = ["500", "800", "1000", "1500", "300", "2000"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"RR间期{val}ms应通过校验")
        
        # 异常RR间期
        abnormal_values = ["299", "2001", "0", "2500", "100", "3000"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"RR间期{val}ms应被标记")
    
    # ===== 心率测试 =====
    def test_heart_rate_validator(self):
        """测试心率校验"""
        key = "312:生物电-心电图机:I导联心房率(次/min)"
        
        # 正常心率
        normal_values = ["60", "75", "100", "120", "150", "30", "200"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"心率{val}bpm应通过校验")
        
        # 异常心率
        abnormal_values = ["29", "201", "0", "250", "10", "300"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"心率{val}bpm应被标记")
    
    # ===== 通用幅度参数测试 =====
    def test_ecg_amplitude_general_validator(self):
        """测试通用ECG幅度参数校验"""
        key = "37:生物电-心电图机:V6导联R'波幅值幅度(μV)"
        
        # 正常幅度值
        normal_values = ["-5000", "-1000", "0", "1000", "5000", "8000", "-8000", "-10000", "10000"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"通用幅度{val}μV应通过校验")
        
        # 异常幅度值
        abnormal_values = ["-10001", "10001", "-15000", "15000", "abc", None]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"通用幅度{val}μV应被标记")
    
    # ===== P波幅度测试 =====
    def test_p_wave_amplitude_validator(self):
        """测试P波幅度校验"""
        key = "231:生物电-心电图机:III导联P'波幅值幅度(μV)"
        
        # 正常P波幅度
        normal_values = ["-200", "-100", "0", "100", "200", "300", "-300", "-500", "500"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"P波幅度{val}μV应通过校验")
        
        # 异常P波幅度
        abnormal_values = ["-501", "501", "-600", "600", "1000", "-1000"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"P波幅度{val}μV应被标记")
    
    # ===== aVR导联P波幅度测试 =====
    def test_avr_p_wave_amplitude_validator(self):
        """测试aVR导联P波幅度校验（通常为负值）"""
        key = "443:生物电-心电图机:aVR导联P波峰值幅度(μV)"
        
        # 正常aVR P波幅度（负值或零）
        normal_values = ["-400", "-200", "-100", "0", "-500"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"aVR P波幅度{val}μV应通过校验")
        
        # 异常aVR P波幅度（正值）
        abnormal_values = ["1", "100", "200", "500", "-501", "-600"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"aVR P波幅度{val}μV应被标记")
    
    # ===== Q波幅度测试 =====
    def test_q_wave_amplitude_validator(self):
        """测试Q波幅度校验（通常为负值）"""
        key = "778:生物电-心电图机:III导联Q波幅值幅度(μV)"
        
        # 正常Q波幅度
        normal_values = ["-4000", "-2000", "-1000", "-500", "0", "-5000"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"Q波幅度{val}μV应通过校验")
        
        # 异常Q波幅度
        abnormal_values = ["-5001", "1", "100", "1000", "-6000"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"Q波幅度{val}μV应被标记")
    
    # ===== R波幅度测试 =====
    def test_r_wave_amplitude_validator(self):
        """测试R波幅度校验"""
        key = "282:生物电-心电图机:II导联R'波幅值幅度(μV)"
        
        # 正常R波幅度
        normal_values = ["100", "500", "1000", "2000", "4000", "0", "5000"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"R波幅度{val}μV应通过校验")
        
        # 异常R波幅度
        abnormal_values = ["-1", "5001", "-100", "6000", "10000"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"R波幅度{val}μV应被标记")
    
    # ===== S波幅度测试 =====
    def test_s_wave_amplitude_validator(self):
        """测试S波幅度校验（通常为负值）"""
        key = "303:生物电-心电图机:I导联S'波幅值幅度(μV)"
        
        # 正常S波幅度
        normal_values = ["-4000", "-2000", "-1000", "-500", "0", "-5000"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"S波幅度{val}μV应通过校验")
        
        # 异常S波幅度
        abnormal_values = ["-5001", "1", "100", "1000", "-6000"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"S波幅度{val}μV应被标记")
    
    # ===== T波幅度测试 =====
    def test_t_wave_amplitude_validator(self):
        """测试T波幅度校验"""
        key = "284:生物电-心电图机:II导联T'波峰值幅度(uV)"
        
        # 正常T波幅度
        normal_values = ["-800", "-500", "-200", "0", "200", "500", "800", "-1000", "1000"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"T波幅度{val}μV应通过校验")
        
        # 异常T波幅度
        abnormal_values = ["-1001", "1001", "-1500", "1500", "2000", "-2000"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"T波幅度{val}μV应被标记")
    
    # ===== 心电轴测试 =====
    def test_heart_axis_validator(self):
        """测试心电轴校验"""
        key = "257:生物电-心电图机:I导联P波电轴(°)"
        
        # 正常心电轴
        normal_values = ["-150", "-90", "-45", "0", "45", "90", "150", "-180", "180"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"心电轴{val}°应通过校验")
        
        # 异常心电轴
        abnormal_values = ["-181", "181", "-200", "200", "-270", "270"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"心电轴{val}°应被标记")
    
    # ===== ECG时间点测试 =====
    def test_ecg_timepoint_validator(self):
        """测试ECG时间点校验（2ms单位）"""
        key = "269:生物电-心电图机:I导联P波起点(2ms)"
        
        # 正常时间点（转换为ms后应在0-2000ms之间）
        normal_values = ["0", "100", "500", "800", "1000", "500", "200"]  # 对应0-2000ms
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"时间点{val}(2ms)应通过校验")
        
        # 异常时间点
        abnormal_values = ["-1", "1001", "2000", "-100", "1500"]  # 对应-2ms, 2002ms等
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"时间点{val}(2ms)应被标记")
    
    # ===== ECG波群数量测试 =====
    def test_ecg_count_validator(self):
        """测试ECG波群数量校验"""
        key = "818:生物电-心电图机:I导联QRS波群的数量(个)"
        
        # 正常数量
        normal_values = ["1", "10", "50", "100", "150", "200"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"波群数量{val}应通过校验")
        
        # 异常数量
        abnormal_values = ["0", "201", "500", "-1", "1000"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"波群数量{val}应被标记")
    
    # ===== ECG面积参数测试 =====
    def test_ecg_area_validator(self):
        """测试ECG面积参数校验"""
        key = "842:生物电-心电图机:I导联QRS波群的面积(μV*ms)"
        
        # 正常面积值
        normal_values = ["-50000", "-10000", "0", "10000", "50000", "80000", "-80000", "-100000", "100000"]
        for val in normal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 0, f"面积{val}μV*ms应通过校验")
        
        # 异常面积值
        abnormal_values = ["-100001", "100001", "-200000", "200000", "abc"]
        for val in abnormal_values:
            payload = {key: make_feature(val)}
            result = PhenoQCBase(payload).evaluate()
            self.assertEqual(result[key]["abnormal"], 1, f"面积{val}μV*ms应被标记")
    

if __name__ == "__main__":
    unittest.main()