"""Validators for Molecular Metabolome - Bile Acids Serum features."""


def register(registry, prefix_registry):
    """Register validators for bile acids serum features.
    
    Total features: 28
    All bile acids serum features are concentration values in nM (nanomoles per liter).
    """
    registry["5068:分子代谢-分子代谢-BileAcidsSerum:12-Ketodeoxycholic_acid(nM)"] = _validate_concentration
    registry["5069:分子代谢-分子代谢-BileAcidsSerum:3,7-Dihydroxy-5-cholestenoic_acid(nM)"] = _validate_concentration
    registry["5070:分子代谢-分子代谢-BileAcidsSerum:3-ketolithocholic_acid(nM)"] = _validate_concentration
    registry["5071:分子代谢-分子代谢-BileAcidsSerum:Allocholic_acid(nM)"] = _validate_concentration
    registry["5072:分子代谢-分子代谢-BileAcidsSerum:Beta-muricholic_acid(nM)"] = _validate_concentration
    registry["5073:分子代谢-分子代谢-BileAcidsSerum:Chenodeoxycholic_acid(nM)"] = _validate_concentration
    registry["5074:分子代谢-分子代谢-BileAcidsSerum:Cholic_acid(nM)"] = _validate_concentration
    registry["5075:分子代谢-分子代谢-BileAcidsSerum:Coprocholic_acid(nM)"] = _validate_concentration
    registry["5076:分子代谢-分子代谢-BileAcidsSerum:Deoxycholic_acid(nM)"] = _validate_concentration
    registry["5077:分子代谢-分子代谢-BileAcidsSerum:Glycochenodeoxycholic_acid(nM)"] = _validate_concentration
    registry["5078:分子代谢-分子代谢-BileAcidsSerum:Glycocholic_acid(nM)"] = _validate_concentration
    registry["5079:分子代谢-分子代谢-BileAcidsSerum:Glycodeoxycholic_acid(nM)"] = _validate_concentration
    registry["5080:分子代谢-分子代谢-BileAcidsSerum:Glycohyocholic_acid(nM)"] = _validate_concentration
    registry["5081:分子代谢-分子代谢-BileAcidsSerum:Glycolithocholic_acid(nM)"] = _validate_concentration
    registry["5082:分子代谢-分子代谢-BileAcidsSerum:Glycoursodeoxycholic_acid(nM)"] = _validate_concentration
    registry["5083:分子代谢-分子代谢-BileAcidsSerum:Hyocholic_acid(nM)"] = _validate_concentration
    registry["5084:分子代谢-分子代谢-BileAcidsSerum:Isolithocholic_acid(nM)"] = _validate_concentration
    registry["5085:分子代谢-分子代谢-BileAcidsSerum:Lithocholic_acid(nM)"] = _validate_concentration
    registry["5086:分子代谢-分子代谢-BileAcidsSerum:Nor-Deoxycholic_acid(nM)"] = _validate_concentration
    registry["5087:分子代谢-分子代谢-BileAcidsSerum:Nor-cholic_acid(nM)"] = _validate_concentration
    registry["5088:分子代谢-分子代谢-BileAcidsSerum:Nutriacholic_acid(nM)"] = _validate_concentration
    registry["5089:分子代谢-分子代谢-BileAcidsSerum:Taurochenodeoxycholic_acid(nM)"] = _validate_concentration
    registry["5090:分子代谢-分子代谢-BileAcidsSerum:Taurocholic_acid(nM)"] = _validate_concentration
    registry["5091:分子代谢-分子代谢-BileAcidsSerum:Taurodeoxycholic_acid(nM)"] = _validate_concentration
    registry["5092:分子代谢-分子代谢-BileAcidsSerum:Taurohyocholic_acid(nM)"] = _validate_concentration
    registry["5093:分子代谢-分子代谢-BileAcidsSerum:Taurolithocholic_acid(nM)"] = _validate_concentration
    registry["5094:分子代谢-分子代谢-BileAcidsSerum:Tauroursodeoxycholic_acid(nM)"] = _validate_concentration
    registry["5095:分子代谢-分子代谢-BileAcidsSerum:Ursodeoxycholic_acid(nM)"] = _validate_concentration


def _validate_concentration(feature_key, final_value, payload) -> bool:
    """
    Validate concentration values for bile acids serum features.
    
    Rules:
    - Must be numeric (int or float)
    - Must be non-negative (>= 0)
    - Reasonable upper limit: 100000 nM (to catch data entry errors)
    - Accepts both string numbers and numeric types
    """
    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False
    
    # Concentration must be non-negative and within reasonable range
    return 0 <= value <= 100000
