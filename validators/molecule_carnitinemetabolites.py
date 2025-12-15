"""Validators for Molecular Metabolome - Carnitine Metabolites features."""


def register(registry, prefix_registry):
    """Register validators for carnitine metabolites features.
    
    Total features: 132
    All carnitine metabolite features are concentration values in nM (nanomoles per liter).
    """
    registry["5096:分子代谢-分子代谢-CarnitineMetabolites:3-dehydroxycarnitine(nM)"] = _validate_concentration
    registry["5097:分子代谢-分子代谢-CarnitineMetabolites:C0(nM)"] = _validate_concentration
    registry["5098:分子代谢-分子代谢-CarnitineMetabolites:C1-Phe(nM)"] = _validate_concentration
    registry["5099:分子代谢-分子代谢-CarnitineMetabolites:C10-OH-iso1(nM)"] = _validate_concentration
    registry["5100:分子代谢-分子代谢-CarnitineMetabolites:C10-OH-iso2(nM)"] = _validate_concentration
    registry["5101:分子代谢-分子代谢-CarnitineMetabolites:C10-OH-iso3(nM)"] = _validate_concentration
    registry["5102:分子代谢-分子代谢-CarnitineMetabolites:C10-iso3(nM)"] = _validate_concentration
    registry["5103:分子代谢-分子代谢-CarnitineMetabolites:C10:1-OH-iso8(nM)"] = _validate_concentration
    registry["5104:分子代谢-分子代谢-CarnitineMetabolites:C10:1-iso3(nM)"] = _validate_concentration
    registry["5105:分子代谢-分子代谢-CarnitineMetabolites:C10:1-iso4(nM)"] = _validate_concentration
    registry["5106:分子代谢-分子代谢-CarnitineMetabolites:C10:1-iso5(nM)"] = _validate_concentration
    registry["5107:分子代谢-分子代谢-CarnitineMetabolites:C10:2-iso3(nM)"] = _validate_concentration
    registry["5108:分子代谢-分子代谢-CarnitineMetabolites:C10:2-iso4(nM)"] = _validate_concentration
    registry["5109:分子代谢-分子代谢-CarnitineMetabolites:C10:2-iso5(nM)"] = _validate_concentration
    registry["5110:分子代谢-分子代谢-CarnitineMetabolites:C10:2-iso6(nM)"] = _validate_concentration
    registry["5111:分子代谢-分子代谢-CarnitineMetabolites:C10:3-OH-iso7(nM)"] = _validate_concentration
    registry["5112:分子代谢-分子代谢-CarnitineMetabolites:C10:3-iso1(nM)"] = _validate_concentration
    registry["5113:分子代谢-分子代谢-CarnitineMetabolites:C10:3-iso3(nM)"] = _validate_concentration
    registry["5114:分子代谢-分子代谢-CarnitineMetabolites:C11-iso3(nM)"] = _validate_concentration
    registry["5115:分子代谢-分子代谢-CarnitineMetabolites:C11:1-iso1(nM)"] = _validate_concentration
    registry["5116:分子代谢-分子代谢-CarnitineMetabolites:C12-iso2(nM)"] = _validate_concentration
    registry["5117:分子代谢-分子代谢-CarnitineMetabolites:C12:1-OH-iso7(nM)"] = _validate_concentration
    registry["5118:分子代谢-分子代谢-CarnitineMetabolites:C12:1-iso3(nM)"] = _validate_concentration
    registry["5119:分子代谢-分子代谢-CarnitineMetabolites:C12:1-iso4(nM)"] = _validate_concentration
    registry["5120:分子代谢-分子代谢-CarnitineMetabolites:C12:1-iso5(nM)"] = _validate_concentration
    registry["5121:分子代谢-分子代谢-CarnitineMetabolites:C12:2-iso2(nM)"] = _validate_concentration
    registry["5122:分子代谢-分子代谢-CarnitineMetabolites:C12:2-iso4(nM)"] = _validate_concentration
    registry["5123:分子代谢-分子代谢-CarnitineMetabolites:C12:2-iso5(nM)"] = _validate_concentration
    registry["5124:分子代谢-分子代谢-CarnitineMetabolites:C12:3-iso1(nM)"] = _validate_concentration
    registry["5125:分子代谢-分子代谢-CarnitineMetabolites:C12:3-iso2(nM)"] = _validate_concentration
    registry["5126:分子代谢-分子代谢-CarnitineMetabolites:C12:4-iso1(nM)"] = _validate_concentration
    registry["5127:分子代谢-分子代谢-CarnitineMetabolites:C13-iso1(nM)"] = _validate_concentration
    registry["5128:分子代谢-分子代谢-CarnitineMetabolites:C13-iso2(nM)"] = _validate_concentration
    registry["5129:分子代谢-分子代谢-CarnitineMetabolites:C14(nM)"] = _validate_concentration
    registry["5130:分子代谢-分子代谢-CarnitineMetabolites:C14-OH(nM)"] = _validate_concentration
    registry["5131:分子代谢-分子代谢-CarnitineMetabolites:C14:1-OH-iso6(nM)"] = _validate_concentration
    registry["5132:分子代谢-分子代谢-CarnitineMetabolites:C14:1-OH-iso7(nM)"] = _validate_concentration
    registry["5133:分子代谢-分子代谢-CarnitineMetabolites:C14:1-iso1(nM)"] = _validate_concentration
    registry["5134:分子代谢-分子代谢-CarnitineMetabolites:C14:1-iso2(nM)"] = _validate_concentration
    registry["5135:分子代谢-分子代谢-CarnitineMetabolites:C14:1-iso3(nM)"] = _validate_concentration
    registry["5136:分子代谢-分子代谢-CarnitineMetabolites:C14:2-OH-iso3(nM)"] = _validate_concentration
    registry["5137:分子代谢-分子代谢-CarnitineMetabolites:C14:2-iso3(nM)"] = _validate_concentration
    registry["5138:分子代谢-分子代谢-CarnitineMetabolites:C14:2-iso4(nM)"] = _validate_concentration
    registry["5139:分子代谢-分子代谢-CarnitineMetabolites:C14:2-iso5(nM)"] = _validate_concentration
    registry["5140:分子代谢-分子代谢-CarnitineMetabolites:C14:3-OH-iso5(nM)"] = _validate_concentration
    registry["5141:分子代谢-分子代谢-CarnitineMetabolites:C14:3-iso1(nM)"] = _validate_concentration
    registry["5142:分子代谢-分子代谢-CarnitineMetabolites:C14:3-iso4(nM)"] = _validate_concentration
    registry["5143:分子代谢-分子代谢-CarnitineMetabolites:C15-iso1(nM)"] = _validate_concentration
    registry["5144:分子代谢-分子代谢-CarnitineMetabolites:C15-iso2(nM)"] = _validate_concentration
    registry["5145:分子代谢-分子代谢-CarnitineMetabolites:C16(nM)"] = _validate_concentration
    registry["5146:分子代谢-分子代谢-CarnitineMetabolites:C16-DC-iso3(nM)"] = _validate_concentration
    registry["5147:分子代谢-分子代谢-CarnitineMetabolites:C16-OH(nM)"] = _validate_concentration
    registry["5148:分子代谢-分子代谢-CarnitineMetabolites:C16:1-OH(nM)"] = _validate_concentration
    registry["5149:分子代谢-分子代谢-CarnitineMetabolites:C16:1-iso1(nM)"] = _validate_concentration
    registry["5150:分子代谢-分子代谢-CarnitineMetabolites:C16:1-iso2(nM)"] = _validate_concentration
    registry["5151:分子代谢-分子代谢-CarnitineMetabolites:C16:2(nM)"] = _validate_concentration
    registry["5152:分子代谢-分子代谢-CarnitineMetabolites:C16:3-iso1(nM)"] = _validate_concentration
    registry["5153:分子代谢-分子代谢-CarnitineMetabolites:C16:3-iso2(nM)"] = _validate_concentration
    registry["5154:分子代谢-分子代谢-CarnitineMetabolites:C16:3-iso3(nM)"] = _validate_concentration
    registry["5155:分子代谢-分子代谢-CarnitineMetabolites:C18(nM)"] = _validate_concentration
    registry["5156:分子代谢-分子代谢-CarnitineMetabolites:C18-DC(nM)"] = _validate_concentration
    registry["5157:分子代谢-分子代谢-CarnitineMetabolites:C18-OH(nM)"] = _validate_concentration
    registry["5158:分子代谢-分子代谢-CarnitineMetabolites:C18:1(nM)"] = _validate_concentration
    registry["5159:分子代谢-分子代谢-CarnitineMetabolites:C18:1-OH(nM)"] = _validate_concentration
    registry["5160:分子代谢-分子代谢-CarnitineMetabolites:C18:2(nM)"] = _validate_concentration
    registry["5161:分子代谢-分子代谢-CarnitineMetabolites:C18:3(nM)"] = _validate_concentration
    registry["5162:分子代谢-分子代谢-CarnitineMetabolites:C18:3-OH-iso2(nM)"] = _validate_concentration
    registry["5163:分子代谢-分子代谢-CarnitineMetabolites:C20-iso2(nM)"] = _validate_concentration
    registry["5164:分子代谢-分子代谢-CarnitineMetabolites:C20:1(nM)"] = _validate_concentration
    registry["5165:分子代谢-分子代谢-CarnitineMetabolites:C20:2(nM)"] = _validate_concentration
    registry["5166:分子代谢-分子代谢-CarnitineMetabolites:C20:3-iso1(nM)"] = _validate_concentration
    registry["5167:分子代谢-分子代谢-CarnitineMetabolites:C20:4(nM)"] = _validate_concentration
    registry["5168:分子代谢-分子代谢-CarnitineMetabolites:C22-iso1(nM)"] = _validate_concentration
    registry["5169:分子代谢-分子代谢-CarnitineMetabolites:C22:1(nM)"] = _validate_concentration
    registry["5170:分子代谢-分子代谢-CarnitineMetabolites:C24(nM)"] = _validate_concentration
    registry["5171:分子代谢-分子代谢-CarnitineMetabolites:C26(nM)"] = _validate_concentration
    registry["5172:分子代谢-分子代谢-CarnitineMetabolites:C26:1(nM)"] = _validate_concentration
    registry["5173:分子代谢-分子代谢-CarnitineMetabolites:C26:2(nM)"] = _validate_concentration
    registry["5174:分子代谢-分子代谢-CarnitineMetabolites:C3-DC(nM)"] = _validate_concentration
    registry["5175:分子代谢-分子代谢-CarnitineMetabolites:C4-DC-iso1(nM)"] = _validate_concentration
    registry["5176:分子代谢-分子代谢-CarnitineMetabolites:C4-DC-iso2(nM)"] = _validate_concentration
    registry["5177:分子代谢-分子代谢-CarnitineMetabolites:C4-DC-iso3(nM)"] = _validate_concentration
    registry["5178:分子代谢-分子代谢-CarnitineMetabolites:C4-OH(nM)"] = _validate_concentration
    registry["5179:分子代谢-分子代谢-CarnitineMetabolites:C4-iso1(nM)"] = _validate_concentration
    registry["5180:分子代谢-分子代谢-CarnitineMetabolites:C4-iso2(nM)"] = _validate_concentration
    registry["5181:分子代谢-分子代谢-CarnitineMetabolites:C5-DC(nM)"] = _validate_concentration
    registry["5182:分子代谢-分子代谢-CarnitineMetabolites:C5-OH-iso2(nM)"] = _validate_concentration
    registry["5183:分子代谢-分子代谢-CarnitineMetabolites:C5-iso2(nM)"] = _validate_concentration
    registry["5184:分子代谢-分子代谢-CarnitineMetabolites:C5-iso3(nM)"] = _validate_concentration
    registry["5185:分子代谢-分子代谢-CarnitineMetabolites:C5-iso4(nM)"] = _validate_concentration
    registry["5186:分子代谢-分子代谢-CarnitineMetabolites:C5:1-OH-iso1(nM)"] = _validate_concentration
    registry["5187:分子代谢-分子代谢-CarnitineMetabolites:C5:1-iso1(nM)"] = _validate_concentration
    registry["5188:分子代谢-分子代谢-CarnitineMetabolites:C6-DC-iso1(nM)"] = _validate_concentration
    registry["5189:分子代谢-分子代谢-CarnitineMetabolites:C6-DC-iso2(nM)"] = _validate_concentration
    registry["5190:分子代谢-分子代谢-CarnitineMetabolites:C6-OH-iso1(nM)"] = _validate_concentration
    registry["5191:分子代谢-分子代谢-CarnitineMetabolites:C6-OH-iso2(nM)"] = _validate_concentration
    registry["5192:分子代谢-分子代谢-CarnitineMetabolites:C6-iso5(nM)"] = _validate_concentration
    registry["5193:分子代谢-分子代谢-CarnitineMetabolites:C6:1-DC-iso1(nM)"] = _validate_concentration
    registry["5194:分子代谢-分子代谢-CarnitineMetabolites:C6:1-iso1(nM)"] = _validate_concentration
    registry["5195:分子代谢-分子代谢-CarnitineMetabolites:C6:1-iso2(nM)"] = _validate_concentration
    registry["5196:分子代谢-分子代谢-CarnitineMetabolites:C6:1-iso3(nM)"] = _validate_concentration
    registry["5197:分子代谢-分子代谢-CarnitineMetabolites:C6:1-iso4(nM)"] = _validate_concentration
    registry["5198:分子代谢-分子代谢-CarnitineMetabolites:C6:2-DC(nM)"] = _validate_concentration
    registry["5199:分子代谢-分子代谢-CarnitineMetabolites:C7-DC-iso1(nM)"] = _validate_concentration
    registry["5200:分子代谢-分子代谢-CarnitineMetabolites:C7-iso1(nM)"] = _validate_concentration
    registry["5201:分子代谢-分子代谢-CarnitineMetabolites:C7-iso2(nM)"] = _validate_concentration
    registry["5202:分子代谢-分子代谢-CarnitineMetabolites:C7-iso3(nM)"] = _validate_concentration
    registry["5203:分子代谢-分子代谢-CarnitineMetabolites:C7-iso4(nM)"] = _validate_concentration
    registry["5204:分子代谢-分子代谢-CarnitineMetabolites:C7:1-iso1(nM)"] = _validate_concentration
    registry["5205:分子代谢-分子代谢-CarnitineMetabolites:C7:1-iso3(nM)"] = _validate_concentration
    registry["5206:分子代谢-分子代谢-CarnitineMetabolites:C8-DC-iso2(nM)"] = _validate_concentration
    registry["5207:分子代谢-分子代谢-CarnitineMetabolites:C8-OH-iso2(nM)"] = _validate_concentration
    registry["5208:分子代谢-分子代谢-CarnitineMetabolites:C8-OH-iso3(nM)"] = _validate_concentration
    registry["5209:分子代谢-分子代谢-CarnitineMetabolites:C8-iso3(nM)"] = _validate_concentration
    registry["5210:分子代谢-分子代谢-CarnitineMetabolites:C8:1-OH-iso11(nM)"] = _validate_concentration
    registry["5211:分子代谢-分子代谢-CarnitineMetabolites:C8:1-OH-iso12(nM)"] = _validate_concentration
    registry["5212:分子代谢-分子代谢-CarnitineMetabolites:C8:1-OH-iso14(nM)"] = _validate_concentration
    registry["5213:分子代谢-分子代谢-CarnitineMetabolites:C8:1-iso2(nM)"] = _validate_concentration
    registry["5214:分子代谢-分子代谢-CarnitineMetabolites:C8:1-iso3(nM)"] = _validate_concentration
    registry["5215:分子代谢-分子代谢-CarnitineMetabolites:C8:1-iso5(nM)"] = _validate_concentration
    registry["5216:分子代谢-分子代谢-CarnitineMetabolites:C8:2-DC-iso1(nM)"] = _validate_concentration
    registry["5217:分子代谢-分子代谢-CarnitineMetabolites:C8:2-iso2(nM)"] = _validate_concentration
    registry["5218:分子代谢-分子代谢-CarnitineMetabolites:C8:2-iso3(nM)"] = _validate_concentration
    registry["5219:分子代谢-分子代谢-CarnitineMetabolites:C8:4-OH-iso1(nM)"] = _validate_concentration
    registry["5220:分子代谢-分子代谢-CarnitineMetabolites:C8:4-OH-iso2(nM)"] = _validate_concentration
    registry["5221:分子代谢-分子代谢-CarnitineMetabolites:C9-iso1(nM)"] = _validate_concentration
    registry["5222:分子代谢-分子代谢-CarnitineMetabolites:C9-iso2(nM)"] = _validate_concentration
    registry["5223:分子代谢-分子代谢-CarnitineMetabolites:C9:1-iso1(nM)"] = _validate_concentration
    registry["5224:分子代谢-分子代谢-CarnitineMetabolites:C9:1-iso2(nM)"] = _validate_concentration
    registry["5225:分子代谢-分子代谢-CarnitineMetabolites:L-Acetylcarnitine(nM)"] = _validate_concentration
    registry["5226:分子代谢-分子代谢-CarnitineMetabolites:N-containing-CAC-05(nM)"] = _validate_concentration
    registry["5227:分子代谢-分子代谢-CarnitineMetabolites:Propionylcarnitine(nM)"] = _validate_concentration


def _validate_concentration(feature_key, final_value, payload) -> bool:
    """
    Validate concentration values for carnitine metabolites features.
    
    Rules:
    - Must be numeric (int or float)
    - Must be non-negative (>= 0)
    - Reasonable upper limit: 1000000 nM (to catch data entry errors)
    - Accepts both string numbers and numeric types
    """
    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False
    
    # Concentration must be non-negative and within reasonable range
    return 0 <= value <= 1000000
