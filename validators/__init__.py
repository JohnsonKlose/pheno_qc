"""
协同校验器包：
- 每个模块实现 register(registry, prefix_registry)。
- registry: 精确特征 key -> 校验函数；prefix_registry: [(前缀字符串, 校验函数), ...]
- 校验函数签名: fn(feature_key, final_value, feature_payload) -> bool

示例：
def register(registry, prefix_registry):
    registry["影像-核磁-liver:original_firstorder_Mean"] = my_exact_validator
    prefix_registry.append(("影像-核磁-liver:", my_prefix_validator))
"""