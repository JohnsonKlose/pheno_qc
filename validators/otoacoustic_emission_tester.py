'''Otoacoustic emission tester features'''
def register(registry, prefix_registry):
    registry["35839:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信号音"] = is_SNR
    registry["35840:感官-耳声发射测试仪:右耳0.5kHz耳声发射的信噪比"] =  is_SNR
    registry["35841:感官-耳声发射测试仪:右耳0.75kHz耳声发射的信号音"] = is_SNR
    registry["35842:感官-耳声发射测试仪:右耳0.75kHz耳声发射的信噪比"] = is_SNR
    registry["35843:感官-耳声发射测试仪:右耳1.5kHz耳声发射的信号音"] = is_SNR
    registry["35844:感官-耳声发射测试仪:右耳1.5kHz耳声发射的信噪比"] = is_SNR
    registry["35845:感官-耳声发射测试仪:右耳1kHz耳声发射的信号音"] = is_SNR
    registry["35846:感官-耳声发射测试仪:右耳1kHz耳声发射的信噪比"] = is_SNR
    registry["35847:感官-耳声发射测试仪:右耳2kHz耳声发射的信号音"] = is_SNR
    registry["35848:感官-耳声发射测试仪:右耳2kHz耳声发射的信噪比"] = is_SNR
    registry["35849:感官-耳声发射测试仪:左耳0.5kHz耳声发射的信号音"] = is_SNR
    registry["35850:感官-耳声发射测试仪:左耳0.5kHz耳声发射的信噪比"] = is_SNR
    registry["35851:感官-耳声发射测试仪:左耳0.75kHz耳声发射的信号音"] = is_SNR
    registry["35852:感官-耳声发射测试仪:左耳0.75kHz耳声发射的信噪比"] = is_SNR
    registry["35853:感官-耳声发射测试仪:左耳1.5kHz耳声发射的信号音"] = is_SNR
    registry["35854:感官-耳声发射测试仪:左耳1.5kHz耳声发射的信噪比"] = is_SNR
    registry["35855:感官-耳声发射测试仪:左耳1kHz耳声发射的信号音"] = is_SNR
    registry["35856:感官-耳声发射测试仪:左耳1kHz耳声发射的信噪比"] = is_SNR
    registry["35857:感官-耳声发射测试仪:左耳2kHz耳声发射的信号音"] = is_SNR
    registry["35858:感官-耳声发射测试仪:左耳2kHz耳声发射的信噪比"] = is_SNR
    registry["35919:感官-耳声发射测试仪:右耳3kHz耳声发射的信号音"] = is_SNR
    registry["35920:感官-耳声发射测试仪:右耳3kHz耳声发射的信噪比"] = is_SNR
    registry["35921:感官-耳声发射测试仪:右耳4kHz耳声发射的信号音"] = is_SNR
    registry["35922:感官-耳声发射测试仪:右耳4kHz耳声发射的信噪比"] = is_SNR
    registry["35923:感官-耳声发射测试仪:右耳6kHz耳声发射的信号音"] = is_SNR
    registry["35924:感官-耳声发射测试仪:右耳6kHz耳声发射的信噪比"] = is_SNR
    registry["35925:感官-耳声发射测试仪:右耳8kHz耳声发射的信号音"] = is_SNR
    registry["35926:感官-耳声发射测试仪:右耳8kHz耳声发射的信噪比"] = is_SNR
    registry["35927:感官-耳声发射测试仪:左耳3kHz耳声发射的信号音"] = is_SNR
    registry["35928:感官-耳声发射测试仪:左耳3kHz耳声发射的信噪比"] = is_SNR
    registry["35929:感官-耳声发射测试仪:左耳4kHz耳声发射的信号音"] = is_SNR
    registry["35930:感官-耳声发射测试仪:左耳4kHz耳声发射的信噪比"] = is_SNR
    registry["35931:感官-耳声发射测试仪:左耳6kHz耳声发射的信号音"] = is_SNR
    registry["35932:感官-耳声发射测试仪:左耳6kHz耳声发射的信噪比"] = is_SNR
    registry["35933:感官-耳声发射测试仪:左耳8kHz耳声发射的信号音"] = is_SNR
    registry["35934:感官-耳声发射测试仪:左耳8kHz耳声发射的信噪比"] = is_SNR

def is_SNR(feature_key, final_value, payload) -> bool:
    try:
        num = float(final_value)
    except (TypeError, ValueError):
        return False
    return -100 <= num <= +100