"""
这是输入的示例json数据，我希望对value_trace中的final的value进行校验，如果value符合规则，则abnormal为0，否则为1
{
    "影像-核磁-liver:original_firstorder_Mean": {
        "feature_key": "影像-核磁-liver:original_firstorder_Mean",
        "feature_name": "原始图像强度均值（Mean）是一阶灰度特征，表示ROI 内所有体素灰度值（信号强度）的算术平均值",
        "data_type": "numeric",
        "metadata": {
            "category_hierarchy": ["影像", "核磁-liver"],
            "description": "在 MRI 图像中，Mean 反映的是在当前序列和扫描参数下，ROI 内所有体素信号强度的平均水平，物理上可近似理解为该区域在所选加权条件下的“整体信号强度基线”：Mean 越高，说明这一块组织整体偏高信号（例如 T2WI 上水含量高、FLAIR 上水肿/炎症区，增强 T1WI 上对比剂富集区或高细胞密度区域等）；Mean 越低，则提示该区域整体偏低信号，可能与纤维化、瘢痕、缺血、含铁沉积或低水含量等成分相关。医学上，Mean 本身不区分内部是否异质，只表示“总体偏亮还是偏暗”，因此通常与方差、熵、百分位数等特征联合解读，用于描述病灶的整体信号水平及其随时间或治疗前后的变化，辅助判断病灶活动性、血供/强化程度和疗效。\n\n- 用于区分正常肝组织与脂肪变性、纤维化或肝硬化等病理状态；\n- 在肝脏肿瘤（如肝细胞癌）分割与分型的特征库中，提供基线强度信息，帮助机器学习模型预测恶性程度；\n- 与血清生物标志物或临床评分（如Child‑Pugh）结合，可用于评估肝功能储备或预后风险。\n\n该特征常作为 radiomics 特征集合的一部分，被用于构建诊断、分期或预后模型。其数值越高，通常提示该区域的信号强度整体偏强，可能与组织中脂肪含量降低或血流灌注增加有关；相反，数值降低则可能与脂肪浸润或瘢痕组织增多相关。该指标对扫描参数高度敏感，需在同一协议或经标准化处理后进行比较。",
            "unit": "无单位",
            "source_system": ["Organ imaging-MRI/CT@3", 
                "影像-核磁-liver:original_firstorder_RootMeanSquared"
            ]
        },
        "value_trace": {
            "raw_origin": {
                "value": "/cfff/data/test/1"
            },
            "intermediate": {
                "value": null
            },
            "final": {
                "value": "123123"
            }
        },
        "processing_context": {
            "method_name": "3D slicer（PyRadiomics 扩展）"
        }
    },
    "影像-核磁-liver:original_firstorder_RootMeanSquared": {
        "feature_key": "影像-核磁-liver:original_firstorder_RootMeanSquared",
        "feature_name": "原始图像强度均值（Mean）是一阶灰度特征，表示ROI 内所有体素灰度值（信号强度）的算术平均值",
        "data_type": "numeric",
        "metadata": {
            "category_hierarchy": ["影像", "核磁-liver"],
            "description": "在 MRI 图像中，Mean 反映的是在当前序列和扫描参数下，ROI 内所有体素信号强度的平均水平，物理上可近似理解为该区域在所选加权条件下的“整体信号强度基线”：Mean 越高，说明这一块组织整体偏高信号（例如 T2WI 上水含量高、FLAIR 上水肿/炎症区，增强 T1WI 上对比剂富集区或高细胞密度区域等）；Mean 越低，则提示该区域整体偏低信号，可能与纤维化、瘢痕、缺血、含铁沉积或低水含量等成分相关。医学上，Mean 本身不区分内部是否异质，只表示“总体偏亮还是偏暗”，因此通常与方差、熵、百分位数等特征联合解读，用于描述病灶的整体信号水平及其随时间或治疗前后的变化，辅助判断病灶活动性、血供/强化程度和疗效。\n\n- 用于区分正常肝组织与脂肪变性、纤维化或肝硬化等病理状态；\n- 在肝脏肿瘤（如肝细胞癌）分割与分型的特征库中，提供基线强度信息，帮助机器学习模型预测恶性程度；\n- 与血清生物标志物或临床评分（如Child‑Pugh）结合，可用于评估肝功能储备或预后风险。\n\n该特征常作为 radiomics 特征集合的一部分，被用于构建诊断、分期或预后模型。其数值越高，通常提示该区域的信号强度整体偏强，可能与组织中脂肪含量降低或血流灌注增加有关；相反，数值降低则可能与脂肪浸润或瘢痕组织增多相关。该指标对扫描参数高度敏感，需在同一协议或经标准化处理后进行比较。",
            "unit": "无单位",
            "source_system": ["Organ imaging-MRI/CT@3", 
                "影像-核磁-liver:original_firstorder_RootMeanSquared"
            ]
        },
        "value_trace": {
            "raw_origin": {
                "value": "/cfff/data/test/1"
            },
            "intermediate": {
                "value": null
            },
            "final": {
                "value": "123123"
            },
            "abnormal": 1
        },
        "processing_context": {
            "method_name": "3D slicer（PyRadiomics 扩展）"
        }
    }
}
输出的格式如下：
{
    "影像-核磁-liver:original_firstorder_Mean": {
        "feature_name": "原始图像强度均值（Mean）是一阶灰度特征，表示ROI 内所有体素灰度值（信号强度）的算术平均值",
        "description": "在 MRI 图像中，Mean 反映的是在当前序列和扫描参数下，ROI 内所有体素信号强度的平均水平，物理上可近似理解为该区域在所选加权条件下的“整体信号强度基线”：Mean 越高，说明这一块组织整体偏高信号（例如 T2WI 上水含量高、FLAIR 上水肿/炎症区，增强 T1WI 上对比剂富集区或高细胞密度区域等）；Mean 越低，则提示该区域整体偏低信号，可能与纤维化、瘢痕、缺血、含铁沉积或低水含量等成分相关。医学上，Mean 本身不区分内部是否异质，只表示“总体偏亮还是偏暗”，因此通常与方差、熵、百分位数等特征联合解读，用于描述病灶的整体信号水平及其随时间或治疗前后的变化，辅助判断病灶活动性、血供/强化程度和疗效。\n\n- 用于区分正常肝组织与脂肪变性、纤维化或肝硬化等病理状态；\n- 在肝脏肿瘤（如肝细胞癌）分割与分型的特征库中，提供基线强度信息，帮助机器学习模型预测恶性程度；\n- 与血清生物标志物或临床评分（如Child‑Pugh）结合，可用于评估肝功能储备或预后风险。\n\n该特征常作为 radiomics 特征集合的一部分，被用于构建诊断、分期或预后模型。其数值越高，通常提示该区域的信号强度整体偏强，可能与组织中脂肪含量降低或血流灌注增加有关；相反，数值降低则可能与脂肪浸润或瘢痕组织增多相关。该指标对扫描参数高度敏感，需在同一协议或经标准化处理后进行比较。",
        "final_value": "123123",
        "abnormal": 1,
        "method_name": "3D slicer（PyRadiomics 扩展）"
    },
    "影像-核磁-liver:original_firstorder_RootMeanSquared": {
        "feature_name": "原始图像强度均值（Mean）是一阶灰度特征，表示ROI 内所有体素灰度值（信号强度）的算术平均值",
        "description": "在 MRI 图像中，Mean 反映的是在当前序列和扫描参数下，ROI 内所有体素信号强度的平均水平，物理上可近似理解为该区域在所选加权条件下的“整体信号强度基线”：Mean 越高，说明这一块组织整体偏高信号（例如 T2WI 上水含量高、FLAIR 上水肿/炎症区，增强 T1WI 上对比剂富集区或高细胞密度区域等）；Mean 越低，则提示该区域整体偏低信号，可能与纤维化、瘢痕、缺血、含铁沉积或低水含量等成分相关。医学上，Mean 本身不区分内部是否异质，只表示“总体偏亮还是偏暗”，因此通常与方差、熵、百分位数等特征联合解读，用于描述病灶的整体信号水平及其随时间或治疗前后的变化，辅助判断病灶活动性、血供/强化程度和疗效。\n\n- 用于区分正常肝组织与脂肪变性、纤维化或肝硬化等病理状态；\n- 在肝脏肿瘤（如肝细胞癌）分割与分型的特征库中，提供基线强度信息，帮助机器学习模型预测恶性程度；\n- 与血清生物标志物或临床评分（如Child‑Pugh）结合，可用于评估肝功能储备或预后风险。\n\n该特征常作为 radiomics 特征集合的一部分，被用于构建诊断、分期或预后模型。其数值越高，通常提示该区域的信号强度整体偏强，可能与组织中脂肪含量降低或血流灌注增加有关；相反，数值降低则可能与脂肪浸润或瘢痕组织增多相关。该指标对扫描参数高度敏感，需在同一协议或经标准化处理后进行比较。",
        "final_value": "123123",
        "abnormal": 1,
        "method_name": "3D slicer（PyRadiomics 扩展）"
    }
}
"""

class PhenoQCBase:
    """
    Pheno QC base class.

    1. 传入示例中的原始 JSON 数据。
    2. 针对每个 feature，提取 value_trace.final.value。
    3. 调用注册的校验逻辑，将校验结果写入 abnormal（符合规则=0，不符合=1）。
    4. 返回示例里展示的压缩格式，只保留核心字段。
    """

    def __init__(self, data: dict):
        if not isinstance(data, dict):
            raise TypeError("data must be a dict keyed by feature id")
        self.data = data
        # 全局注册：validators 包中每个模块暴露 register(registry, prefix_registry)
        self.validators, self.prefix_validators = self._load_validators()

    def evaluate(self) -> dict:
        """Produce normalized QC output as shown in the header comment."""
        results = {}
        for feature_key, feature_payload in self.data.items():
            final_value = self._extract_final_value(feature_payload)
            abnormal = self._determine_abnormal(feature_key, final_value, feature_payload)

            results[feature_key] = {
                "feature_name": feature_payload.get("feature_name"),
                "description": feature_payload.get("metadata", {}).get("description"),
                "final_value": final_value,
                "abnormal": abnormal,
                "method_name": feature_payload.get("processing_context", {}).get("method_name"),
            }
        return results

    def _extract_final_value(self, feature_payload: dict):
        return (
            feature_payload
            .get("value_trace", {})
            .get("final", {})
            .get("value")
        )

    def _determine_abnormal(self, feature_key, final_value, feature_payload: dict) -> int:
        """
        从注册表中查找匹配的校验器，优先级：精确匹配 > 前缀匹配 > 默认实现。
        返回 bool 表示是否合规；非 bool 将抛出异常。
        """
        is_valid = self.check_final_value(feature_key, final_value, feature_payload)
        if isinstance(is_valid, bool):
            return 0 if is_valid else 1
        raise TypeError("check_final_value must return a boolean")

    def check_final_value(self, feature_key, final_value, feature_payload: dict) -> bool:
        """
        协同入口：默认从 validators 包的注册表获取校验函数。
        - 精确 key：validators 中 registry[feature_key]
        - 前缀匹配：prefix_validators 里按顺序第一个命中的 (prefix, fn)
        - 都没有时，走 fallback（可被子类覆盖）
        """
        if feature_key in self.validators:
            return self.validators[feature_key](feature_key, final_value, feature_payload)

        for prefix, fn in self.prefix_validators:
            if feature_key.startswith(prefix):
                return fn(feature_key, final_value, feature_payload)

        return self.default_check(feature_key, final_value, feature_payload)

    def default_check(self, feature_key, final_value, feature_payload: dict) -> bool:
        """
        默认策略：未匹配到任何校验器时一律判为不需要校验。
        可由子类覆盖（例如放宽为 True）。
        """
        return True

    def _load_validators(self):
        """
        动态加载 validators 包下的所有 register(registry, prefix_registry)。
        - registry: 精确 key -> fn
        - prefix_registry: 列表[(prefix, fn), ...]
        """
        try:
            import importlib
            import pkgutil
            import validators
        except ModuleNotFoundError:
            return {}, []

        registry = {}
        prefix_registry = []
        for module_info in pkgutil.iter_modules(validators.__path__):
            module = importlib.import_module(f"{validators.__name__}.{module_info.name}")
            register = getattr(module, "register", None)
            if callable(register):
                register(registry, prefix_registry)
        return registry, prefix_registry