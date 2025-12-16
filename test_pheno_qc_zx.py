import unittest
from pheno_qc_base import PhenoQCBase

# 这是一个辅助函数，用来模拟系统传进来的数据结构
def make_feature(final_value):
    return {
        "value_trace": {"final": {"value": final_value}},
        # 其他字段测试时不重要，可以省略
    }

class MyQCBaseTests(unittest.TestCase):
    
    def test_numeric_validation(self):
        """测试数值型校验 (肌肉量等)"""
        # 注意：这里的 Key 必须是您 my_numeric_keys.txt 里存在的 ID
        key_valid = "157:生物电-身体体质成份分析仪:左上肢肌肉"
        
        payload = {
            # 正常情况：数字
            key_valid: make_feature(25.5),
            # 正常情况：数字字符串
            "Test_Num_Str": make_feature("25.5"), 
            # 异常情况：非数字字符串
            "Test_Num_Bad": make_feature("abc"),
            # 异常情况：NA
            "Test_Num_NA": make_feature("na")
        }
        
        # 这里的 hack 是为了测试方便，实际运行时不需要手动注册
        # 在测试脚本里，您可能需要手动把您的 Key 绑到 validator 上，或者确保系统能加载到您的 txt
        # 这里假设系统已经自动加载了您的 validators/my_qc.py
        
        # 如果是单元测试，通常需要手动模拟注册过程，或者用真实的 ID
        # 假设 157 在您的 txt 里：
        result = PhenoQCBase(payload).evaluate()

        # 25.5 应该是正常 (abnormal=0)
        self.assertEqual(result[key_valid]["abnormal"], 0)
        
        # 如果您在 txt 里加了 Test_Num_Bad，它应该是 1
        # 这里建议直接用真实 ID 测试真实逻辑
    
    def test_fingerprint_validation(self):
        """测试指纹校验"""
        key_finger = "36969:皮肤及附属器-手提箱式肤纹采集仪:右手指纹RLI-食"
        
        payload = {
            # 正常情况：在白名单里
            key_finger: make_feature("简斗"),
            # 异常情况：不在白名单
            "36969:ErrorCase": make_feature("随便写的"),
        }
        
        # 注意：必须确保 payload 里的 key 和您 txt 里的 key 一致
        # 这里我们假设 "36969:ErrorCase" 也在您的 factor txt 里，或者复用同一个 key 测试不同值
        
        # 复用同一个Key测试异常值：
        payload_bad = {
            key_finger: make_feature("未知类型") 
        }
        
        qc = PhenoQCBase(payload)
        res_good = qc.evaluate()
        # 简斗 -> 正常
        self.assertEqual(res_good[key_finger]["abnormal"], 0)
        
        qc_bad = PhenoQCBase(payload_bad)
        res_bad = qc_bad.evaluate()
        # 未知类型 -> 异常
        self.assertEqual(res_bad[key_finger]["abnormal"], 1)

if __name__ == "__main__":
    unittest.main()