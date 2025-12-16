# 新特征 QC 开发指南

本文档说明如何在现有框架下，为新的特征（单个或一类前缀）编写 QC 校验脚本，并让 `PhenoQCBase` 自动加载生效。

## 框架概览
- 入口类：`pheno_qc_base.PhenoQCBase`，负责读取原始特征 JSON，提取 `value_trace.final.value`，调用校验器并输出压缩格式（`feature_name/description/final_value/abnormal/method_name`）。
- 校验注册表来源：`validators` 包中每个模块的 `register(registry, prefix_registry)`。
  - `registry`：精确特征 key 映射到校验函数。
  - `prefix_registry`：前缀命中时使用的校验函数，按注册顺序匹配。
- 校验函数签名：`fn(feature_key, final_value, feature_payload) -> bool`；返回 `True` 表示合规（abnormal=0），`False` 表示异常（abnormal=1）。

## 开发步骤
1) **创建模块文件**
   - 在 `validators/` 下新建文件（例如 `validators/lab_blood.py`）。
   - 该模块必须实现 `register(registry, prefix_registry)`，后续步骤都在这里完成。

2) **编写校验函数**
   - 统一签名：`def my_validator(feature_key, final_value, payload) -> bool:`
   - `final_value` 已由基类从 `value_trace.final.value` 提取；完整原始数据在 `payload`。
   - 仅返回布尔值，返回其他类型会抛异常。

3) **在 register 中挂载规则**
   - 精确匹配：`registry["特征ID"] = my_validator`
   - 前缀匹配：`prefix_registry.append(("前缀字符串", my_validator))`，按 append 顺序从上到下匹配。
   - 推荐模板：
     ```python
     def register(registry, prefix_registry):
         registry["feature_x"] = my_validator
         prefix_registry.append(("prefix_y", my_validator))
     ```
   - 规则优先级：精确匹配 > 前缀匹配 > `default_check`（默认放行，可子类覆盖）。

4) **本地验证**
   - 在交互式或脚本中执行：
     ```python
     from pheno_qc_base import PhenoQCBase

     qc = PhenoQCBase(test_payload_dict)
     result = qc.evaluate()
     ```
   - 检查 `abnormal` 标记是否符合预期（正常=0，异常=1）。

## 最小示例
参考 `validators/questionnaire_one.py`

添加上述文件后，无需修改其他代码，`PhenoQCBase` 会在运行时自动发现并加载校验器。

## 设计建议
- **类型宽容**：可接受字符串数字，避免因类型差异误判；非数字时应返回 `False`。
- **边界保护**：对明显不合常理的极端值设上/下限，便于标记异常。
- **可读性**：在模块顶部写一句话说明该类特征；函数名简洁表达规则。
- **顺序敏感**：前缀匹配按 append 顺序检查，先注册严格规则，再注册兜底规则。