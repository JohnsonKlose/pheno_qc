"""Validators for Molecular Metabolome - Sterol Metabolites features."""


def register(registry, prefix_registry):
    """Register validators for sterol metabolites features.
    
    Total features: 26
    Sterol metabolite features are concentration values in μmol/L (micromoles per liter).
    """
    registry["6604:分子代谢-分子代谢-SterolMetabolites:11-Deoxycortisol(uM)"] = _validate_concentration
    registry["6605:分子代谢-分子代谢-SterolMetabolites:11-Hydroxyandrostenedione(uM)"] = _validate_concentration
    registry["6606:分子代谢-分子代谢-SterolMetabolites:16α_-Hydroxyestrone(uM)"] = _validate_concentration
    registry["6607:分子代谢-分子代谢-SterolMetabolites:22(R)-Hydroxycholesterol(uM)"] = _validate_concentration
    registry["6608:分子代谢-分子代谢-SterolMetabolites:22β-hydroxycholesterol&24-Hydroxycholesterol(uM)"] = _validate_concentration
    registry["6609:分子代谢-分子代谢-SterolMetabolites:27-Hydroxycholesterol(uM)"] = _validate_concentration
    registry["6610:分子代谢-分子代谢-SterolMetabolites:3β-Androstanediol(uM)"] = _validate_concentration
    registry["6611:分子代谢-分子代谢-SterolMetabolites:5β-Pregnanediol(uM)"] = _validate_concentration
    registry["6612:分子代谢-分子代谢-SterolMetabolites:7-Dehydrocholesterol(uM)"] = _validate_concentration
    registry["6613:分子代谢-分子代谢-SterolMetabolites:7α_-Hydroxycholesterol(uM)"] = _validate_concentration
    registry["6614:分子代谢-分子代谢-SterolMetabolites:Androstenediol(uM)"] = _validate_concentration
    registry["6615:分子代谢-分子代谢-SterolMetabolites:Androsterone(uM)"] = _validate_concentration
    registry["6616:分子代谢-分子代谢-SterolMetabolites:Campesterol(uM)"] = _validate_concentration
    registry["6617:分子代谢-分子代谢-SterolMetabolites:Cholesterol(uM)"] = _validate_concentration
    registry["6618:分子代谢-分子代谢-SterolMetabolites:Cholesterol_5α,6α-epoxide(uM)"] = _validate_concentration
    registry["6619:分子代谢-分子代谢-SterolMetabolites:Corticosterone(uM)"] = _validate_concentration
    registry["6620:分子代谢-分子代谢-SterolMetabolites:DESMOSTEROL(uM)"] = _validate_concentration
    registry["6621:分子代谢-分子代谢-SterolMetabolites:Dihydrocholesterol(uM)"] = _validate_concentration
    registry["6622:分子代谢-分子代谢-SterolMetabolites:Epiandrosterone(uM)"] = _validate_concentration
    registry["6623:分子代谢-分子代谢-SterolMetabolites:Lanosterol(uM)"] = _validate_concentration
    registry["6624:分子代谢-分子代谢-SterolMetabolites:Lathosterol(uM)"] = _validate_concentration
    registry["6625:分子代谢-分子代谢-SterolMetabolites:Pregnenolone(uM)"] = _validate_concentration
    registry["6626:分子代谢-分子代谢-SterolMetabolites:Testosterone(uM)"] = _validate_concentration
    registry["6627:分子代谢-分子代谢-SterolMetabolites:brassicasterol(uM)"] = _validate_concentration
    registry["6628:分子代谢-分子代谢-SterolMetabolites:β-Sitosterol(uM)"] = _validate_concentration
    registry["6629:分子代谢-分子代谢-SterolMetabolites:β-Stigmasterol(uM)"] = _validate_concentration


def _validate_concentration(feature_key, final_value, payload) -> bool:
    """
    Validate concentration values for sterol metabolites features.
    
    Rules:
    - Must be numeric (int or float)
    - Must be non-negative (>= 0)
    - Reasonable upper limit: 10000 μmol/L (to catch data entry errors)
    - Accepts both string numbers and numeric types
    
    Note: Upper limit accommodates cholesterol (highest sterol, Mean+3SD ~3,153 μmol/L)
    while catching obvious data entry errors.
    """
    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False
    
    # Concentration must be non-negative and within reasonable range
    return 0 <= value <= 10000
