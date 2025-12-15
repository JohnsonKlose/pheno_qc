"""Validators for Molecular Metabolome - Amino Metabolites features."""


def register(registry, prefix_registry):
    """Register validators for amino metabolites features.
    
    Total features: 107
    All amino metabolite features are concentration values in μmol/L (micromoles per liter).
    """
    registry["4961:分子代谢-分子代谢-AminoMetabolites:(±)-Octopamine(μmol/L)"] = _validate_concentration
    registry["4962:分子代谢-分子代谢-AminoMetabolites:1,2-Diaminopropane(μmol/L)"] = _validate_concentration
    registry["4963:分子代谢-分子代谢-AminoMetabolites:1,3-Diaminopropane(μmol/L)"] = _validate_concentration
    registry["4964:分子代谢-分子代谢-AminoMetabolites:1-Methyl-L-histidine(μmol/L)"] = _validate_concentration
    registry["4965:分子代谢-分子代谢-AminoMetabolites:2,4-diaminobutanoic_acid(μmol/L)"] = _validate_concentration
    registry["4966:分子代谢-分子代谢-AminoMetabolites:2-Aminoisobutyric_acid(μmol/L)"] = _validate_concentration
    registry["4967:分子代谢-分子代谢-AminoMetabolites:3,3',5'-Triiodo-L-thyronine(μmol/L)"] = _validate_concentration
    registry["4968:分子代谢-分子代谢-AminoMetabolites:3,3',5-Triiodo-L-thyronine(μmol/L)"] = _validate_concentration
    registry["4969:分子代谢-分子代谢-AminoMetabolites:3,4-Dihydroxy-DL-phenylalanine(μmol/L)"] = _validate_concentration
    registry["4970:分子代谢-分子代谢-AminoMetabolites:3-Aminobenzoic_acid(μmol/L)"] = _validate_concentration
    registry["4971:分子代谢-分子代谢-AminoMetabolites:3-Methyl-L-histidine(μmol/L)"] = _validate_concentration
    registry["4972:分子代谢-分子代谢-AminoMetabolites:3-hydroxyanthranilic_acid(μmol/L)"] = _validate_concentration
    registry["4973:分子代谢-分子代谢-AminoMetabolites:4-Aminophenol(μmol/L)"] = _validate_concentration
    registry["4974:分子代谢-分子代谢-AminoMetabolites:4-Hydroxy-L-isoleucine(μmol/L)"] = _validate_concentration
    registry["4975:分子代谢-分子代谢-AminoMetabolites:4-Hydroxy-L-proline(μmol/L)"] = _validate_concentration
    registry["4976:分子代谢-分子代谢-AminoMetabolites:5-Aminovaleric_acid(μmol/L)"] = _validate_concentration
    registry["4977:分子代谢-分子代谢-AminoMetabolites:5-Hydroxy-L-tryptophan(μmol/L)"] = _validate_concentration
    registry["4978:分子代谢-分子代谢-AminoMetabolites:5-Hydroxydopamine(μmol/L)"] = _validate_concentration
    registry["4979:分子代谢-分子代谢-AminoMetabolites:6-Aminocaproic_acid(μmol/L)"] = _validate_concentration
    registry["4980:分子代谢-分子代谢-AminoMetabolites:Agmatine_sulfate(μmol/L)"] = _validate_concentration
    registry["4981:分子代谢-分子代谢-AminoMetabolites:Ala-Leu(μmol/L)"] = _validate_concentration
    registry["4982:分子代谢-分子代谢-AminoMetabolites:Ala-Trp(μmol/L)"] = _validate_concentration
    registry["4983:分子代谢-分子代谢-AminoMetabolites:Argininosuccinic_acid(μmol/L)"] = _validate_concentration
    registry["4984:分子代谢-分子代谢-AminoMetabolites:Asymmetric_dimethylarginine(μmol/L)"] = _validate_concentration
    registry["4985:分子代谢-分子代谢-AminoMetabolites:Cadaverine(μmol/L)"] = _validate_concentration
    registry["4986:分子代谢-分子代谢-AminoMetabolites:Cystathionine(μmol/L)"] = _validate_concentration
    registry["4987:分子代谢-分子代谢-AminoMetabolites:Cysteamine(μmol/L)"] = _validate_concentration
    registry["4988:分子代谢-分子代谢-AminoMetabolites:D-(-)-α-Phenylglycine(μmol/L)"] = _validate_concentration
    registry["4989:分子代谢-分子代谢-AminoMetabolites:D-Homoserine(μmol/L)"] = _validate_concentration
    registry["4990:分子代谢-分子代谢-AminoMetabolites:D-serine(μmol/L)"] = _validate_concentration
    registry["4991:分子代谢-分子代谢-AminoMetabolites:DL-2,6-Diaminopimelic_acid(μmol/L)"] = _validate_concentration
    registry["4992:分子代谢-分子代谢-AminoMetabolites:DL-3-Aminoisobutyric_acid(μmol/L)"] = _validate_concentration
    registry["4993:分子代谢-分子代谢-AminoMetabolites:DL-5-Hydroxylysine(μmol/L)"] = _validate_concentration
    registry["4994:分子代谢-分子代谢-AminoMetabolites:DL-Methionine_sulfone(μmol/L)"] = _validate_concentration
    registry["4995:分子代谢-分子代谢-AminoMetabolites:DL-Normetanephrine(μmol/L)"] = _validate_concentration
    registry["4996:分子代谢-分子代谢-AminoMetabolites:DL-lanthionine(μmol/L)"] = _validate_concentration
    registry["4997:分子代谢-分子代谢-AminoMetabolites:DL-methionine_sulfoxide(μmol/L)"] = _validate_concentration
    registry["4998:分子代谢-分子代谢-AminoMetabolites:Desipramine(μmol/L)"] = _validate_concentration
    registry["4999:分子代谢-分子代谢-AminoMetabolites:Djenkolic_Acid(μmol/L)"] = _validate_concentration
    registry["5000:分子代谢-分子代谢-AminoMetabolites:GSH(μmol/L)"] = _validate_concentration
    registry["5001:分子代谢-分子代谢-AminoMetabolites:Glycine(μmol/L)"] = _validate_concentration
    registry["5002:分子代谢-分子代谢-AminoMetabolites:Histamine(μmol/L)"] = _validate_concentration
    registry["5003:分子代谢-分子代谢-AminoMetabolites:Hypotaurine(μmol/L)"] = _validate_concentration
    registry["5004:分子代谢-分子代谢-AminoMetabolites:Isopentylamine(μmol/L)"] = _validate_concentration
    registry["5005:分子代谢-分子代谢-AminoMetabolites:L-2-Aminobutyric_acid(μmol/L)"] = _validate_concentration
    registry["5006:分子代谢-分子代谢-AminoMetabolites:L-Alanine(μmol/L)"] = _validate_concentration
    registry["5007:分子代谢-分子代谢-AminoMetabolites:L-Anserine(μmol/L)"] = _validate_concentration
    registry["5008:分子代谢-分子代谢-AminoMetabolites:L-Arginine(μmol/L)"] = _validate_concentration
    registry["5009:分子代谢-分子代谢-AminoMetabolites:L-Asparagine(μmol/L)"] = _validate_concentration
    registry["5010:分子代谢-分子代谢-AminoMetabolites:L-Aspartic_acid(μmol/L)"] = _validate_concentration
    registry["5011:分子代谢-分子代谢-AminoMetabolites:L-Carnosine(μmol/L)"] = _validate_concentration
    registry["5012:分子代谢-分子代谢-AminoMetabolites:L-Citrulline(μmol/L)"] = _validate_concentration
    registry["5013:分子代谢-分子代谢-AminoMetabolites:L-Cysteic_acid(μmol/L)"] = _validate_concentration
    registry["5014:分子代谢-分子代谢-AminoMetabolites:L-Cysteine(μmol/L)"] = _validate_concentration
    registry["5015:分子代谢-分子代谢-AminoMetabolites:L-Glutamic_acid(μmol/L)"] = _validate_concentration
    registry["5016:分子代谢-分子代谢-AminoMetabolites:L-Glutamine(μmol/L)"] = _validate_concentration
    registry["5017:分子代谢-分子代谢-AminoMetabolites:L-Histidine(μmol/L)"] = _validate_concentration
    registry["5018:分子代谢-分子代谢-AminoMetabolites:L-Homoarginine(μmol/L)"] = _validate_concentration
    registry["5019:分子代谢-分子代谢-AminoMetabolites:L-Homocitrulline(μmol/L)"] = _validate_concentration
    registry["5020:分子代谢-分子代谢-AminoMetabolites:L-Homocysteine(μmol/L)"] = _validate_concentration
    registry["5021:分子代谢-分子代谢-AminoMetabolites:L-Isoleucine(μmol/L)"] = _validate_concentration
    registry["5022:分子代谢-分子代谢-AminoMetabolites:L-Kynurenine(μmol/L)"] = _validate_concentration
    registry["5023:分子代谢-分子代谢-AminoMetabolites:L-Leucine(μmol/L)"] = _validate_concentration
    registry["5024:分子代谢-分子代谢-AminoMetabolites:L-Lysine(μmol/L)"] = _validate_concentration
    registry["5025:分子代谢-分子代谢-AminoMetabolites:L-Methionine(μmol/L)"] = _validate_concentration
    registry["5026:分子代谢-分子代谢-AminoMetabolites:L-Norvaline(μmol/L)"] = _validate_concentration
    registry["5027:分子代谢-分子代谢-AminoMetabolites:L-Ornithine(μmol/L)"] = _validate_concentration
    registry["5028:分子代谢-分子代谢-AminoMetabolites:L-Pipecolic_acid(μmol/L)"] = _validate_concentration
    registry["5029:分子代谢-分子代谢-AminoMetabolites:L-Proline(μmol/L)"] = _validate_concentration
    registry["5030:分子代谢-分子代谢-AminoMetabolites:L-Serine(μmol/L)"] = _validate_concentration
    registry["5031:分子代谢-分子代谢-AminoMetabolites:L-Threonine(μmol/L)"] = _validate_concentration
    registry["5032:分子代谢-分子代谢-AminoMetabolites:L-Thyroxine(μmol/L)"] = _validate_concentration
    registry["5033:分子代谢-分子代谢-AminoMetabolites:L-Tryptophan(μmol/L)"] = _validate_concentration
    registry["5034:分子代谢-分子代谢-AminoMetabolites:L-Tryptophanamide(μmol/L)"] = _validate_concentration
    registry["5035:分子代谢-分子代谢-AminoMetabolites:L-Tyrosine(μmol/L)"] = _validate_concentration
    registry["5036:分子代谢-分子代谢-AminoMetabolites:L-Valine(μmol/L)"] = _validate_concentration
    registry["5037:分子代谢-分子代谢-AminoMetabolites:Leu-Pro(μmol/L)"] = _validate_concentration
    registry["5038:分子代谢-分子代谢-AminoMetabolites:N-Methylphenethylamine(μmol/L)"] = _validate_concentration
    registry["5039:分子代谢-分子代谢-AminoMetabolites:N-methyltyramine(μmol/L)"] = _validate_concentration
    registry["5040:分子代谢-分子代谢-AminoMetabolites:Norepinephrine(μmol/L)"] = _validate_concentration
    registry["5041:分子代谢-分子代谢-AminoMetabolites:Nα-Acetyl-L-lysine(μmol/L)"] = _validate_concentration
    registry["5042:分子代谢-分子代谢-AminoMetabolites:Nε,Nε,Nε-Trimethyllysine(μmol/L)"] = _validate_concentration
    registry["5043:分子代谢-分子代谢-AminoMetabolites:O-Phospho-L-Serine(μmol/L)"] = _validate_concentration
    registry["5044:分子代谢-分子代谢-AminoMetabolites:O-Phospho-L-threonine(μmol/L)"] = _validate_concentration
    registry["5045:分子代谢-分子代谢-AminoMetabolites:O-Phospho-L-tyrosine(μmol/L)"] = _validate_concentration
    registry["5046:分子代谢-分子代谢-AminoMetabolites:O-Phosphorylethanolamine(μmol/L)"] = _validate_concentration
    registry["5047:分子代谢-分子代谢-AminoMetabolites:Phenethylamine(μmol/L)"] = _validate_concentration
    registry["5048:分子代谢-分子代谢-AminoMetabolites:Phenylalanine(μmol/L)"] = _validate_concentration
    registry["5049:分子代谢-分子代谢-AminoMetabolites:Putrescine(μmol/L)"] = _validate_concentration
    registry["5050:分子代谢-分子代谢-AminoMetabolites:S-(2-Aminoethyl)-L-cysteine(μmol/L)"] = _validate_concentration
    registry["5051:分子代谢-分子代谢-AminoMetabolites:S-(5'-Adenosyl)-L-homocysteine(μmol/L)"] = _validate_concentration
    registry["5052:分子代谢-分子代谢-AminoMetabolites:S-(5'-Adenosyl)-L-methionine(μmol/L)"] = _validate_concentration
    registry["5053:分子代谢-分子代谢-AminoMetabolites:S-Adenosylmethioninamine(μmol/L)"] = _validate_concentration
    registry["5054:分子代谢-分子代谢-AminoMetabolites:Saccharopine(μmol/L)"] = _validate_concentration
    registry["5055:分子代谢-分子代谢-AminoMetabolites:Sarcosine(μmol/L)"] = _validate_concentration
    registry["5056:分子代谢-分子代谢-AminoMetabolites:Serotonin(μmol/L)"] = _validate_concentration
    registry["5057:分子代谢-分子代谢-AminoMetabolites:Spermidine(μmol/L)"] = _validate_concentration
    registry["5058:分子代谢-分子代谢-AminoMetabolites:Spermine(μmol/L)"] = _validate_concentration
    registry["5059:分子代谢-分子代谢-AminoMetabolites:Taurine(μmol/L)"] = _validate_concentration
    registry["5060:分子代谢-分子代谢-AminoMetabolites:Tryptamine(μmol/L)"] = _validate_concentration
    registry["5061:分子代谢-分子代谢-AminoMetabolites:Tyramine(μmol/L)"] = _validate_concentration
    registry["5062:分子代谢-分子代谢-AminoMetabolites:metanephrine(μmol/L)"] = _validate_concentration
    registry["5063:分子代谢-分子代谢-AminoMetabolites:o-acetyl-L-serine(μmol/L)"] = _validate_concentration
    registry["5064:分子代谢-分子代谢-AminoMetabolites:synephrine(μmol/L)"] = _validate_concentration
    registry["5065:分子代谢-分子代谢-AminoMetabolites:β-alanine(μmol/L)"] = _validate_concentration
    registry["5066:分子代谢-分子代谢-AminoMetabolites:γ-Aminobutyric_acid(μmol/L)"] = _validate_concentration
    registry["5067:分子代谢-分子代谢-AminoMetabolites:γ-Glu-Cys(μmol/L)"] = _validate_concentration


def _validate_concentration(feature_key, final_value, payload) -> bool:
    """
    Validate concentration values for amino metabolites features.
    
    Rules:
    - Must be numeric (int or float)
    - Must be non-negative (>= 0)
    - Reasonable upper limit: 10000 μmol/L (to catch data entry errors)
    - Accepts both string numbers and numeric types
    """
    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False
    
    # Concentration must be non-negative and within reasonable range
    return 0 <= value <= 10000
