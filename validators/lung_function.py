"""lung functions features."""

def register(registry, prefix_registry):
    registry["4945:功能表型-肺功能:BF(实测值)(1/min)"] = is_between_1_and_1000
    registry["4946:功能表型-肺功能:ERV(实测值)(L)"] = is_between_1_and_1000
    registry["4947:功能表型-肺功能:FEV_1(实测值)(L)"] = is_between_1_and_1000
    registry["4948:功能表型-肺功能:FEV_1*30(实测值)(L/min)"] = is_between_1_and_1000
    registry["4949:功能表型-肺功能:IC(实测值)(L)"] = is_between_1_and_1000
    registry["4950:功能表型-肺功能:VC_MAX(实测值)(L)"] = is_between_1_and_1000
    registry["4951:功能表型-肺功能:FVC(实测值)(L)"] = is_between_1_and_1000
    registry["4952:功能表型-肺功能:VT(实测值)(L)"] = is_between_1_and_1000
    registry["4953:功能表型-肺功能:MEF_25(实测值)(L/s)"] = is_between_1_and_1000
    registry["4954:功能表型-肺功能:MVV(实测值)(L/min)"] = is_between_1_and_1000
    registry["4955:功能表型-肺功能:PEF(实测值)(L/s)"] = is_between_1_and_1000
    registry["4956:功能表型-肺功能:FET(实测值)(s)"] = is_between_1_and_1000
    registry["4957:功能表型-肺功能:FEV_1_%_FVC(实测值)(%)"] = is_between_1_and_1000
    registry["4958:功能表型-肺功能:MEF_50(实测值)(L/s)"] = is_between_1_and_1000
    registry["4959:功能表型-肺功能:MMEF_75/25(实测值)(L/s)"] = is_between_1_and_1000
    registry["4960:功能表型-肺功能:MEF_75(实测值)(L/s)"] = is_between_1_and_1000

def is_between_1_and_1000(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 1-1000（含）之间，接受字符串数字或数值类型。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 1 <= num <= 1000