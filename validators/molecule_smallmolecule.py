"""Validators for Molecular Metabolome - Small Molecule features."""


def register(registry, prefix_registry):
    """Register validators for small molecule features.

    Total features: 53
    Small molecule features include:
    - Concentration values in μmol/L or mmol/L (converted)
    - Chromatography peak area measurements (unitless)
    """
    registry["6932:分子代谢-分子代谢-smallMolecule:2_ABA"] = _validate_concentration
    registry["6933:分子代谢-分子代谢-smallMolecule:2_HBA"] = _validate_concentration
    registry["6934:分子代谢-分子代谢-smallMolecule:2_KG"] = _validate_concentration
    registry["6935:分子代谢-分子代谢-smallMolecule:3_HBA"] = _validate_concentration
    registry["6936:分子代谢-分子代谢-smallMolecule:AAA"] = _validate_concentration
    registry["6937:分子代谢-分子代谢-smallMolecule:AcOH"] = _validate_concentration
    registry["6938:分子代谢-分子代谢-smallMolecule:Acaa"] = _validate_concentration
    registry["6939:分子代谢-分子代谢-smallMolecule:Acto"] = _validate_concentration
    registry["6940:分子代谢-分子代谢-smallMolecule:Ala"] = _validate_concentration
    registry["6941:分子代谢-分子代谢-smallMolecule:Asp"] = _validate_concentration
    registry["6942:分子代谢-分子代谢-smallMolecule:BCAA"] = _validate_concentration
    registry["6943:分子代谢-分子代谢-smallMolecule:Ca"] = _validate_concentration
    registry["6944:分子代谢-分子代谢-smallMolecule:Chol"] = _validate_concentration
    registry["6945:分子代谢-分子代谢-smallMolecule:Citrate"] = _validate_concentration
    registry["6946:分子代谢-分子代谢-smallMolecule:Cra"] = _validate_concentration
    registry["6947:分子代谢-分子代谢-smallMolecule:Cre"] = _validate_concentration
    registry["6948:分子代谢-分子代谢-smallMolecule:DHT"] = _validate_concentration
    registry["6949:分子代谢-分子代谢-smallMolecule:DMG"] = _validate_concentration
    registry["6950:分子代谢-分子代谢-smallMolecule:DMSF"] = _validate_concentration
    registry["6951:分子代谢-分子代谢-smallMolecule:EtOH"] = _validate_concentration
    registry["6952:分子代谢-分子代谢-smallMolecule:FA"] = _validate_concentration
    registry["6953:分子代谢-分子代谢-smallMolecule:FisherR"] = _validate_concentration
    registry["6954:分子代谢-分子代谢-smallMolecule:GAL"] = _validate_concentration
    registry["6955:分子代谢-分子代谢-smallMolecule:GLC"] = _validate_concentration
    registry["6956:分子代谢-分子代谢-smallMolecule:Gln"] = _validate_concentration
    registry["6957:分子代谢-分子代谢-smallMolecule:GlnA"] = _validate_concentration
    registry["6958:分子代谢-分子代谢-smallMolecule:Glu"] = _validate_concentration
    registry["6959:分子代谢-分子代谢-smallMolecule:GluA"] = _validate_concentration
    registry["6960:分子代谢-分子代谢-smallMolecule:Gly"] = _validate_concentration
    registry["6961:分子代谢-分子代谢-smallMolecule:Glycol"] = _validate_concentration
    registry["6962:分子代谢-分子代谢-smallMolecule:His"] = _validate_concentration
    registry["6963:分子代谢-分子代谢-smallMolecule:Ile"] = _validate_concentration
    registry["6964:分子代谢-分子代谢-smallMolecule:KEDTA"] = _validate_concentration
    registry["6965:分子代谢-分子代谢-smallMolecule:LactPyR"] = _validate_concentration
    registry["6966:分子代谢-分子代谢-smallMolecule:Lactate"] = _validate_concentration
    registry["6967:分子代谢-分子代谢-smallMolecule:Leu"] = _validate_concentration
    registry["6968:分子代谢-分子代谢-smallMolecule:LeuIleR"] = _validate_concentration
    registry["6969:分子代谢-分子代谢-smallMolecule:Lys"] = _validate_concentration
    registry["6970:分子代谢-分子代谢-smallMolecule:Met"] = _validate_concentration
    registry["6971:分子代谢-分子代谢-smallMolecule:Mg"] = _validate_concentration
    registry["6972:分子代谢-分子代谢-smallMolecule:NAG1"] = _validate_concentration
    registry["6973:分子代谢-分子代谢-smallMolecule:NAG12R"] = _validate_concentration
    registry["6974:分子代谢-分子代谢-smallMolecule:NAG2"] = _validate_concentration
    registry["6975:分子代谢-分子代谢-smallMolecule:Oni"] = _validate_concentration
    registry["6976:分子代谢-分子代谢-smallMolecule:Phe"] = _validate_concentration
    registry["6977:分子代谢-分子代谢-smallMolecule:Pro"] = _validate_concentration
    registry["6978:分子代谢-分子代谢-smallMolecule:Pyr"] = _validate_concentration
    registry["6979:分子代谢-分子代谢-smallMolecule:Sarc"] = _validate_concentration
    registry["6980:分子代谢-分子代谢-smallMolecule:Suc"] = _validate_concentration
    registry["6981:分子代谢-分子代谢-smallMolecule:TMAO"] = _validate_concentration
    registry["6982:分子代谢-分子代谢-smallMolecule:Thr"] = _validate_concentration
    registry["6983:分子代谢-分子代谢-smallMolecule:Tyr"] = _validate_concentration
    registry["6984:分子代谢-分子代谢-smallMolecule:Val"] = _validate_concentration


def _validate_concentration(feature_key, final_value, payload) -> bool:
    """
    Validate values for small molecule features.

    Rules:
    - Must be numeric (int or float)
    - Must be non-negative (>= 0)
    - Reasonable upper limit: 100000 (accommodates both concentrations and peak areas)
    - Accepts both string numbers and numeric types

    Note: This validator handles both concentration measurements (typically <100 μmol/L)
    and chromatography peak area measurements (typically 50,000-70,000 arbitrary units).
    """
    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False
    
    # Concentration must be non-negative and within reasonable range
    return 0 <= value <= 100000
