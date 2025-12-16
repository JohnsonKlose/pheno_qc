"""Validators for Molecular Metabolome - Elements features."""


def register(registry, prefix_registry):
    """Register validators for elements features.
    
    Total features: 31
    Element features are concentration values in μg/L or mg/L.
    """
    registry["5228:分子代谢-分子代谢-Elements:107_Ag(μg/L)"] = _validate_concentration
    registry["5229:分子代谢-分子代谢-Elements:11_B(μg/L)"] = _validate_concentration
    registry["5230:分子代谢-分子代谢-Elements:123_Sb(μg/L)"] = _validate_concentration
    registry["5231:分子代谢-分子代谢-Elements:127_I(μg/L)"] = _validate_concentration
    registry["5232:分子代谢-分子代谢-Elements:133_Cs(μg/L)"] = _validate_concentration
    registry["5233:分子代谢-分子代谢-Elements:137_Ba(μg/L)"] = _validate_concentration
    registry["5234:分子代谢-分子代谢-Elements:202_Hg(μg/L)"] = _validate_concentration
    registry["5235:分子代谢-分子代谢-Elements:205_Tl(μg/L)"] = _validate_concentration
    registry["5236:分子代谢-分子代谢-Elements:23_Na(mg/L)"] = _validate_concentration
    registry["5237:分子代谢-分子代谢-Elements:24_Mg(mg/L)"] = _validate_concentration
    registry["5238:分子代谢-分子代谢-Elements:28_Si(μg/L)"] = _validate_concentration
    registry["5239:分子代谢-分子代谢-Elements:31_P(mg/L)"] = _validate_concentration
    registry["5240:分子代谢-分子代谢-Elements:34_S(mg/L)"] = _validate_concentration
    registry["5241:分子代谢-分子代谢-Elements:35_Cl(mg/L)"] = _validate_concentration
    registry["5242:分子代谢-分子代谢-Elements:39_K(mg/L)"] = _validate_concentration
    registry["5243:分子代谢-分子代谢-Elements:44_Ca(mg/L)"] = _validate_concentration
    registry["5244:分子代谢-分子代谢-Elements:51_V(μg/L)"] = _validate_concentration
    registry["5245:分子代谢-分子代谢-Elements:55_Mn(μg/L)"] = _validate_concentration
    registry["5246:分子代谢-分子代谢-Elements:56_Fe(μg/L)"] = _validate_concentration
    registry["5247:分子代谢-分子代谢-Elements:59_Co(μg/L)"] = _validate_concentration
    registry["5248:分子代谢-分子代谢-Elements:60_Ni(μg/L)"] = _validate_concentration
    registry["5249:分子代谢-分子代谢-Elements:63_Cu(μg/L)"] = _validate_concentration
    registry["5250:分子代谢-分子代谢-Elements:66_Zn(μg/L)"] = _validate_concentration
    registry["5251:分子代谢-分子代谢-Elements:72_Ge(μg/L)"] = _validate_concentration
    registry["5252:分子代谢-分子代谢-Elements:75_As(μg/L)"] = _validate_concentration
    registry["5253:分子代谢-分子代谢-Elements:78_Se(μg/L)"] = _validate_concentration
    registry["5254:分子代谢-分子代谢-Elements:79_Br(μg/L)"] = _validate_concentration
    registry["5255:分子代谢-分子代谢-Elements:7_Li(μg/L)"] = _validate_concentration
    registry["5256:分子代谢-分子代谢-Elements:85_Rb(μg/L)"] = _validate_concentration
    registry["5257:分子代谢-分子代谢-Elements:88_Sr(μg/L)"] = _validate_concentration
    registry["5258:分子代谢-分子代谢-Elements:95_Mo(μg/L)"] = _validate_concentration


def _validate_concentration(feature_key, final_value, payload) -> bool:
    """
    Validate concentration values for element features.
    
    Rules:
    - Must be numeric (int or float)
    - Must be non-negative (>= 0)
    - Reasonable upper limit: 10000 mg/L (accommodates both μg/L and mg/L units)
    - Accepts both string numbers and numeric types
    
    Note: Features use mixed units (μg/L for trace elements, mg/L for major elements).
    The validator treats all as raw numeric values since conversion is unit-dependent.
    """
    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False
    
    # Concentration must be non-negative and within reasonable range
    # 10000 mg/L accommodates major elements like Na, S, Cl
    return 0 <= value <= 10000
