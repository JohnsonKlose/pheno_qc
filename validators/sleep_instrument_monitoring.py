"""Validators for sleep instrument monitoring features."""


def register(registry, prefix_registry):
    registry["37147:睡眠-睡眠仪器和监控中心:REM睡眠潜伏期(min)"] = is_between_0_and_1000
    registry["37148:睡眠-睡眠仪器和监控中心:睡眠分期表-REM期-潜伏期(min)(min)"] =  _validate_hundred_scale_score
    registry["37149:睡眠-睡眠仪器和监控中心:SpO2概况-清醒期平均SpO2(%)"] = _validate_hundred_scale_score
    registry["37150:睡眠-睡眠仪器和监控中心:SpO2概况-睡眠期平均SpO2(%)"] = _validate_hundred_scale_score
    registry["37151:睡眠-睡眠仪器和监控中心:入睡后清醒时间(WASO)(min)"] = _validate_hundred_scale_score
    registry["37152:睡眠-睡眠仪器和监控中心:呼吸努力相关觉醒次数"] = _validate_hundred_scale_score
    registry["37153:睡眠-睡眠仪器和监控中心:微觉醒事件-PLM相关微觉醒-指数-Non-REM"] = _validate_hundred_scale_score
    registry["37154:睡眠-睡眠仪器和监控中心:微觉醒事件-PLM相关微觉醒-指数-REM"] = _validate_hundred_scale_score
    registry["37155:睡眠-睡眠仪器和监控中心:微觉醒事件-PLM相关微觉醒-指数-Sleep"] = _validate_hundred_scale_score
    registry["37156:睡眠-睡眠仪器和监控中心:微觉醒事件-PLM相关微觉醒-计数-Non-REM"] = _validate_hundred_scale_score
    registry["37157:睡眠-睡眠仪器和监控中心:微觉醒事件-PLM相关微觉醒-计数-Sleep"] = _validate_hundred_scale_score
    registry["37158:睡眠-睡眠仪器和监控中心:微觉醒事件-PLM相关微觉醒-计数-REM"] = _validate_hundred_scale_score
    registry["37159:睡眠-睡眠仪器和监控中心:微觉醒事件-Total-指数-Sleep"] = _validate_hundred_scale_score
    registry["37160:睡眠-睡眠仪器和监控中心:微觉醒事件-自发性微觉醒-指数-Non-REM"] = _validate_hundred_scale_score
    registry["37161:睡眠-睡眠仪器和监控中心:微觉醒事件-自发性微觉醒-指数-Sleep"] = _validate_hundred_scale_score
    registry["37162:睡眠-睡眠仪器和监控中心:微觉醒事件-自发性微觉醒-指数-REM"] = _validate_hundred_scale_score
    registry["37163:睡眠-睡眠仪器和监控中心:微觉醒事件-自发性微觉醒-计数-Non-REM"] = _validate_hundred_scale_score
    registry["37164:睡眠-睡眠仪器和监控中心:微觉醒事件-自发性微觉醒-计数-Sleep"] = _validate_hundred_scale_score
    registry["37165:睡眠-睡眠仪器和监控中心:微觉醒事件-自发性微觉醒-计数-REM"] = _validate_hundred_scale_score
    registry["37166:睡眠-睡眠仪器和监控中心:微觉醒事件-足动相关微觉醒-指数-REM"] = _validate_hundred_scale_score
    registry["37167:睡眠-睡眠仪器和监控中心:微觉醒事件-足动相关微觉醒-计数-Non-REM"] = _validate_hundred_scale_score
    registry["37168:睡眠-睡眠仪器和监控中心:微觉醒事件-足动相关微觉醒-计数-Sleep"] = _validate_hundred_scale_score
    registry["37169:睡眠-睡眠仪器和监控中心:微觉醒事件-足动相关微觉醒-指数-Non-REM"] = _validate_hundred_scale_score
    registry["37170:睡眠-睡眠仪器和监控中心:微觉醒事件-足动相关微觉醒-指数-Sleep"] = _validate_hundred_scale_score
    registry["37171:睡眠-睡眠仪器和监控中心:微觉醒事件-足动相关微觉醒-计数-REM"] = _validate_hundred_scale_score
    registry["37172:睡眠-睡眠仪器和监控中心:总卧床时间(TIB)(min)"] = is_between_0_and_1000
    registry["37173:睡眠-睡眠仪器和监控中心:总睡眠时间(TST)(min)"] = is_between_0_and_1000
    registry["37174:睡眠-睡眠仪器和监控中心:总睡眠期时间(TSP)(min)"] = is_between_0_and_1000
    registry["37175:睡眠-睡眠仪器和监控中心:睡眠分期表-N1期-持续时间(min)(min)"] = is_between_0_and_1000
    registry["37176:睡眠-睡眠仪器和监控中心:睡眠分期表-N1期-%睡眠时间(%)"] = _validate_hundred_scale_score
    registry["37177:睡眠-睡眠仪器和监控中心:睡眠分期表-N1期-潜伏期(min)(min)"] = is_between_0_and_1000
    registry["37178:睡眠-睡眠仪器和监控中心:睡眠分期表-N2期-%睡眠时间(%)"] = _validate_hundred_scale_score
    registry["37179:睡眠-睡眠仪器和监控中心:睡眠分期表-N2期-持续时间(min)(min)"] = is_between_0_and_1000
    registry["37180:睡眠-睡眠仪器和监控中心:睡眠分期表-N2期-潜伏期(min)(min)"] = is_between_0_and_1000
    registry["37181:睡眠-睡眠仪器和监控中心:睡眠分期表-N3期-%睡眠时间(%)"] = _validate_hundred_scale_score
    registry["37182:睡眠-睡眠仪器和监控中心:睡眠分期表-N3期-持续时间(min)(min)"] = is_between_0_and_1000
    registry["37183:睡眠-睡眠仪器和监控中心:睡眠分期表-N3期-潜伏期(min)(min)"] = is_between_0_and_1000
    registry["37184:睡眠-睡眠仪器和监控中心:睡眠分期表-REM期-持续时间(min)(min)"] = is_between_0_and_1000
    registry["37185:睡眠-睡眠仪器和监控中心:睡眠分期表-REM期-%睡眠时间(%)"] = _validate_hundred_scale_score
    registry["37186:睡眠-睡眠仪器和监控中心:睡眠分期转换次数"] = is_between_0_and_1000
    registry["37187:睡眠-睡眠仪器和监控中心:睡眠效率(TST/TRT)(%)"] = _validate_hundred_scale_score
    registry["37188:睡眠-睡眠仪器和监控中心:睡眠潜伏期(min)"] = is_between_0_and_1000
    registry["37189:睡眠-睡眠仪器和监控中心:肢体运动事件-LM指数-REM睡眠"] = is_between_0_and_1000
    registry["37190:睡眠-睡眠仪器和监控中心:肢体运动事件-LM指数-清醒期"] = is_between_0_and_1000
    registry["37191:睡眠-睡眠仪器和监控中心:肢体运动事件-LM次数-睡眠期"] = is_between_0_and_1000
    registry["37192:睡眠-睡眠仪器和监控中心:肢体运动事件-LM指数-睡眠期"] = is_between_0_and_1000
    registry["37193:睡眠-睡眠仪器和监控中心:肢体运动事件-LM指数-NREM睡眠"] = is_between_0_and_1000
    registry["37194:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM次数-睡眠期"] = is_between_0_and_1000
    registry["37195:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM次数-NREM睡眠"] = is_between_0_and_1000
    registry["37196:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM指数-睡眠期"] = is_between_0_and_1000
    registry["37197:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM指数-NREM睡眠"] = is_between_0_and_1000
    registry["37198:睡眠-睡眠仪器和监控中心:肢体运动事件-LM次数-NREM睡眠"] = is_between_0_and_1000
    registry["37199:睡眠-睡眠仪器和监控中心:肢体运动事件-LM次数-REM睡眠"] = is_between_0_and_1000
    registry["37200:睡眠-睡眠仪器和监控中心:肢体运动事件-LM次数-清醒期"] = is_between_0_and_1000
    registry["37201:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM发作指数-REM睡眠"] = is_between_0_and_1000
    registry["37202:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM发作指数-清醒期"] = is_between_0_and_1000
    registry["37203:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM发作指数-睡眠期"] = is_between_0_and_1000
    registry["37204:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM发作指数-NREM睡眠"] = is_between_0_and_1000
    registry["37205:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM发作次数-REM睡眠"] = is_between_0_and_1000
    registry["37206:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM发作次数-清醒期"] = is_between_0_and_1000
    registry["37207:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM发作次数-睡眠期"] = is_between_0_and_1000
    registry["37208:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM发作次数-NREM睡眠"] = is_between_0_and_1000
    registry["37209:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM指数-REM睡眠"] = is_between_0_and_1000
    registry["37210:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM指数-清醒期"] = is_between_0_and_1000
    registry["37211:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM次数-REM睡眠"] = is_between_0_and_1000
    registry["37212:睡眠-睡眠仪器和监控中心:肢体运动事件-PLM次数-清醒期"] = is_between_0_and_1000
    registry["37213:睡眠-睡眠仪器和监控中心:觉醒次数"] = is_between_0_and_1000
    registry["37214:睡眠-睡眠仪器和监控中心:微觉醒事件-Total-计数-Sleep"] = is_between_0_and_1000
    registry["37215:睡眠-睡眠仪器和监控中心:SpO2与睡眠体位-NREM仰卧-最低SpO2(%)"] = _validate_hundred_scale_score
    registry["37216:睡眠-睡眠仪器和监控中心:SpO2与睡眠体位-NREM非仰卧-最低SpO2(%)"] = _validate_hundred_scale_score
    registry["37217:睡眠-睡眠仪器和监控中心:SpO2与睡眠体位-REM仰卧-最低SpO2(%)"] = _validate_hundred_scale_score
    registry["37218:睡眠-睡眠仪器和监控中心:SpO2与睡眠体位-REM非仰卧-最低SpO2(%)"] = _validate_hundred_scale_score
    registry["37219:睡眠-睡眠仪器和监控中心:SpO2与睡眠体位-总睡眠期-最低SpO2(%)"] = _validate_hundred_scale_score
    registry["37220:睡眠-睡眠仪器和监控中心:SpO2概况-睡眠期最低SpO2(%)"] = _validate_hundred_scale_score
    registry["37221:睡眠-睡眠仪器和监控中心:SpO2概况-平均氧降(%)"] = _validate_hundred_scale_score
    registry["37222:睡眠-睡眠仪器和监控中心:呼吸事件-AHI"] = is_between_0_and_1000
    registry["37223:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-呼吸暂停+低通气_-NREM"] = is_between_0_and_1000
    registry["37224:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-AHI(/hr)-NREM(/hr)"] = is_between_0_and_1000
    registry["37225:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-AHI(/hr)-总睡眠期(/hr)"] = is_between_0_and_1000
    registry["37226:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-总计-NREM期次数"] = is_between_0_and_1000
    registry["37227:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-总计-REM期次数"] = is_between_0_and_1000
    registry["37228:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-总计-计数"] = is_between_0_and_1000
    registry["37229:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-总计-指数"] = is_between_0_and_1000
    registry["37230:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-低通气-NREM"] = is_between_0_and_1000
    registry["37231:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-低通气-总睡眠期"] = is_between_0_and_1000
    registry["37232:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-阻塞性-指数"] = is_between_0_and_1000
    registry["37233:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-阻塞性-计数"] = is_between_0_and_1000
    registry["37234:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-中枢性-REM期次数"] = is_between_0_and_1000
    registry["37235:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-中枢性-平均持续时间(秒)(秒)"] = is_between_0_and_1000
    registry["37236:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-中枢性-计数"] = is_between_0_and_1000
    registry["37237:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-中枢性-指数"] = is_between_0_and_1000
    registry["37238:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-中枢性-NREM期次数"] = is_between_0_and_1000
    registry["37239:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-总计-平均持续时间(秒)(秒)"] = is_between_0_and_1000
    registry["37240:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-总计-计数"] = is_between_0_and_1000
    registry["37241:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-总计-指数"] = is_between_0_and_1000
    registry["37242:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-总计-NREM期次数"] = is_between_0_and_1000
    registry["37243:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-呼吸暂停-NREM"] = is_between_0_and_1000
    registry["37244:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-呼吸暂停-总睡眠期"] = is_between_0_and_1000
    registry["37245:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-混合性-计数"] = is_between_0_and_1000
    registry["37246:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-混合性-指数"] = is_between_0_and_1000
    registry["37247:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-混合性-NREM期次数"] = is_between_0_and_1000
    registry["37248:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-混合性-REM期次数"] = is_between_0_and_1000
    registry["37249:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-混合性-平均持续时间(秒)(秒)"] = is_between_0_and_1000
    registry["37250:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-阻塞性-REM期次数"] = is_between_0_and_1000
    registry["37251:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-总计-REM期次数"] = is_between_0_and_1000
    registry["37252:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-阻塞性-平均持续时间(秒)(秒)"] = is_between_0_and_1000
    registry["37253:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-阻塞性-计数"] = is_between_0_and_1000
    registry["37254:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-阻塞性-指数"] = is_between_0_and_1000
    registry["37255:睡眠-睡眠仪器和监控中心:呼吸事件-呼吸暂停-阻塞性-NREM期次数"] = is_between_0_and_1000
    registry["37256:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-仰卧-中枢性(/hr)"] = is_between_0_and_1000
    registry["37257:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-仰卧-低通气(/hr)"] = is_between_0_and_1000
    registry["37258:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-仰卧-总指数(/hr)"] = is_between_0_and_1000
    registry["37259:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-仰卧-混合性(/hr)"] = is_between_0_and_1000
    registry["37260:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-仰卧-阻塞性(/hr)"] = is_between_0_and_1000
    registry["37261:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-俯卧位-中枢性(/hr)"] = is_between_0_and_1000
    registry["37262:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-俯卧位-低通气(/hr)"] = is_between_0_and_1000
    registry["37263:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-俯卧位-总指数(/hr)"] = is_between_0_and_1000
    registry["37264:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-俯卧位-混合性(/hr)"] = is_between_0_and_1000
    registry["37265:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-俯卧位-阻塞性(/hr)"] = is_between_0_and_1000
    registry["37266:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-右侧卧位-中枢性(/hr)"] = is_between_0_and_1000
    registry["37267:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-右侧卧位-低通气(/hr)"] = is_between_0_and_1000
    registry["37268:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-右侧卧位-总指数(/hr)"] = is_between_0_and_1000
    registry["37269:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-右侧卧位-混合性(/hr)"] = is_between_0_and_1000
    registry["37270:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-右侧卧位-阻塞性(/hr)"] = is_between_0_and_1000
    registry["37271:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-左侧卧位-中枢性(/hr)"] = is_between_0_and_1000
    registry["37272:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-左侧卧位-低通气(/hr)"] = is_between_0_and_1000
    registry["37273:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-左侧卧位-总指数(/hr)"] = is_between_0_and_1000
    registry["37274:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-左侧卧位-混合性(/hr)"] = is_between_0_and_1000
    registry["37275:睡眠-睡眠仪器和监控中心:呼吸事件与体位(/hr)-左侧卧位-阻塞性(/hr)"] = is_between_0_and_1000
    registry["37276:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-AHI(/hr)-REM(/hr)"] = is_between_0_and_1000
    registry["37277:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-低通气-REM"] = is_between_0_and_1000
    registry["37278:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-呼吸暂停+低通气_-REM"] = is_between_0_and_1000
    registry["37279:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-呼吸暂停+低通气_-总睡眠期"] = is_between_0_and_1000
    registry["37280:睡眠-睡眠仪器和监控中心:呼吸事件与睡眠分期-呼吸暂停-REM"] = is_between_0_and_1000
    registry["37281:睡眠-睡眠仪器和监控中心:呼吸紊乱指数"] = is_between_0_and_1000
    registry["37282:睡眠-睡眠仪器和监控中心:微觉醒事件-呼吸相关微觉醒-指数-REM"] = is_between_0_and_1000
    registry["37283:睡眠-睡眠仪器和监控中心:微觉醒事件-呼吸相关微觉醒-计数-Non-REM"] = is_between_0_and_1000
    registry["37284:睡眠-睡眠仪器和监控中心:微觉醒事件-呼吸相关微觉醒-计数-Sleep"] = is_between_0_and_1000
    registry["37285:睡眠-睡眠仪器和监控中心:微觉醒事件-呼吸相关微觉醒-指数-Non-REM"] = is_between_0_and_1000
    registry["37286:睡眠-睡眠仪器和监控中心:微觉醒事件-呼吸相关微觉醒-指数-Sleep"] = is_between_0_and_1000
    registry["37287:睡眠-睡眠仪器和监控中心:微觉醒事件-呼吸相关微觉醒-计数-REM"] = is_between_0_and_1000
    registry["37288:睡眠-睡眠仪器和监控中心:睡眠期血氧下降次数-血氧下降_≥_4%"] = is_between_0_and_1000
    registry["37289:睡眠-睡眠仪器和监控中心:睡眠期血氧下降指数-血氧下降_≥_3%"] = is_between_0_and_1000
    registry["37290:睡眠-睡眠仪器和监控中心:睡眠期血氧下降指数-血氧下降_≥_4%"] = is_between_0_and_1000
    registry["37291:睡眠-睡眠仪器和监控中心:睡眠期血氧下降次数-血氧下降_≥_3%"] = is_between_0_and_1000
    registry["37292:睡眠-睡眠仪器和监控中心:血氧饱和度水平-低于75%-持续时间"] = is_between_0_and_1000
    registry["37293:睡眠-睡眠仪器和监控中心:血氧饱和度水平-低于80%-持续时间"] = is_between_0_and_1000
    registry["37294:睡眠-睡眠仪器和监控中心:血氧饱和度水平-低于85%-持续时间"] = is_between_0_and_1000
    registry["37295:睡眠-睡眠仪器和监控中心:血氧饱和度水平-低于90%-持续时间"] = is_between_0_and_1000
    registry["37296:睡眠-睡眠仪器和监控中心:鼾声-REM期-指数"] = is_between_0_and_1000
    registry["37297:睡眠-睡眠仪器和监控中心:鼾声-REM期-次数"] = is_between_0_and_1000
    registry["37298:睡眠-睡眠仪器和监控中心:鼾声-总记录-次数"] = is_between_0_and_1000
    registry["37299:睡眠-睡眠仪器和监控中心:鼾声-睡眠期-次数"] = is_between_0_and_1000
    registry["37300:睡眠-睡眠仪器和监控中心:鼾声-NREM期-次数"] = is_between_0_and_1000
    registry["37301:睡眠-睡眠仪器和监控中心:鼾声-总记录-指数"] = is_between_0_and_1000
    registry["37302:睡眠-睡眠仪器和监控中心:鼾声-睡眠期-指数"] = is_between_0_and_1000
    registry["37303:睡眠-睡眠仪器和监控中心:鼾声-NREM期-指数"] = is_between_0_and_1000
    registry["37304:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-总计-平均持续时间(秒)(秒)"] = is_between_0_and_1000
    registry["37305:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-总计-最长持续时间(秒)(秒)"] = is_between_0_and_1000
    registry["37306:睡眠-睡眠仪器和监控中心:呼吸事件-低通气-阻塞性-平均持续时间(秒)(秒)"] = is_between_0_and_1000
    registry["37307:睡眠-睡眠仪器和监控中心:心率-呼吸事件相关平均心率(呼吸暂停/低通气)"] = is_between_0_and_1000

def is_between_0_and_1000(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 0-1000（含）之间，接受字符串数字或数值类型。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= num <= 1000

def _validate_hundred_scale_score(feature_key, final_value, payload) -> bool:
    """
    - 范围为0-100之间的浮点数或整数。
    """
    try:
        score = float(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= score <= 100