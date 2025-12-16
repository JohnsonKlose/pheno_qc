"""Validators for ECG (Electrocardiogram) related features using index:pheno registration."""

def register(registry, prefix_registry):
    """
    注册 ECG 相关特征的校验函数。
    使用文件第一列的 index 和 pheno 列值作为键，格式为："index:pheno"。
    例如："32:生物电-心电图机:II导联R'波峰值时间(ms)"
    """
    
    # ==================== 时间类参数校验 ====================
    registry["32:生物电-心电图机:II导联R'波峰值时间(ms)"] = validate_ecg_time_general
    registry["33:生物电-心电图机:II导联R'波时限"] = validate_ecg_time_general
    registry["34:生物电-心电图机:V1导联T'波峰值时间(ms)"] = validate_ecg_time_general
    registry["35:生物电-心电图机:V1导联T'波时限(ms)"] = validate_ecg_time_general
    registry["36:生物电-心电图机:V6导联R'波峰值时间(ms)"] = validate_ecg_time_general
    registry["39:生物电-心电图机:V6导联R'波时限"] = validate_ecg_time_general
    registry["41:生物电-心电图机:V6导联S'波时限(ms)"] = validate_ecg_time_general
    registry["42:生物电-心电图机:V6导联S波峰值时间(ms)"] = validate_ecg_time_general
    registry["44:生物电-心电图机:aVF导联R'波峰值时间(ms)"] = validate_ecg_time_general
    registry["46:生物电-心电图机:aVF导联R'波时限"] = validate_ecg_time_general
    registry["48:生物电-心电图机:aVF导联S波峰值时间(ms)"] = validate_ecg_time_general
    registry["51:生物电-心电图机:aVL导联S'波时限(ms)"] = validate_ecg_time_general
    registry["52:生物电-心电图机:aVL导联S波峰值时间(ms)"] = validate_ecg_time_general
    registry["55:生物电-心电图机:aVR导联S'波时限(ms)"] = validate_ecg_time_general
    registry["56:生物电-心电图机:aVR导联S波峰值时间(ms)"] = validate_ecg_time_general
    
    # P波相关时间参数
    registry["230:生物电-心电图机:III导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["232:生物电-心电图机:III导联P'波时限(ms)"] = validate_p_wave_time
    registry["234:生物电-心电图机:III导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["235:生物电-心电图机:III导联P波时限(ms)"] = validate_p_wave_time
    registry["238:生物电-心电图机:II导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["240:生物电-心电图机:II导联P'波时限(ms)"] = validate_p_wave_time
    registry["255:生物电-心电图机:II导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["256:生物电-心电图机:II导联P波时限(ms)"] = validate_p_wave_time
    registry["288:生物电-心电图机:I导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["290:生物电-心电图机:I导联P'波时限(ms)"] = validate_p_wave_time
    registry["293:生物电-心电图机:I导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["294:生物电-心电图机:I导联P波时限(ms)"] = validate_p_wave_time
    registry["295:生物电-心电图机:aVR导联P波时限(ms)"] = validate_p_wave_time
    
    # PR间期
    registry["242:生物电-心电图机:I导联PR间期(ms)"] = validate_pr_interval
    registry["243:生物电-心电图机:II导联PR间期(ms)"] = validate_pr_interval
    registry["244:生物电-心电图机:III导联PR间期(ms)"] = validate_pr_interval
    registry["245:生物电-心电图机:aVR导联PR间期(ms)"] = validate_pr_interval
    registry["246:生物电-心电图机:aVL导联PR间期(ms)"] = validate_pr_interval
    registry["247:生物电-心电图机:aVF导联PR间期(ms)"] = validate_pr_interval
    registry["248:生物电-心电图机:V1导联PR间期(ms)"] = validate_pr_interval
    registry["249:生物电-心电图机:V2导联PR间期(ms)"] = validate_pr_interval
    registry["250:生物电-心电图机:V3导联PR间期(ms)"] = validate_pr_interval
    registry["251:生物电-心电图机:V4导联PR间期(ms)"] = validate_pr_interval
    registry["252:生物电-心电图机:V5导联PR间期(ms)"] = validate_pr_interval
    registry["253:生物电-心电图机:V6导联PR间期(ms)"] = validate_pr_interval
    
    # T波时间参数
    registry["286:生物电-心电图机:II导联T'波峰值时间(ms)"] = validate_t_wave_time
    registry["287:生物电-心电图机:II导联T'波时限(ms)"] = validate_t_wave_time
    registry["309:生物电-心电图机:I导联T'波峰值时间(ms)"] = validate_t_wave_time
    registry["310:生物电-心电图机:I导联T'波时限(ms)"] = validate_t_wave_time
    
    # RR间期
    registry["311:生物电-心电图机:I导联平均RR间期(ms)"] = validate_rr_interval
    registry["314:生物电-心电图机:II导联平均RR间期(ms)"] = validate_rr_interval
    registry["317:生物电-心电图机:III导联平均RR间期(ms)"] = validate_rr_interval
    registry["320:生物电-心电图机:aVR导联平均RR间期(ms)"] = validate_rr_interval
    registry["323:生物电-心电图机:aVL导联平均RR间期(ms)"] = validate_rr_interval
    registry["326:生物电-心电图机:aVF导联平均RR间期(ms)"] = validate_rr_interval
    registry["329:生物电-心电图机:V1导联平均RR间期(ms)"] = validate_rr_interval
    registry["332:生物电-心电图机:V2导联平均RR间期(ms)"] = validate_rr_interval
    registry["335:生物电-心电图机:V3导联平均RR间期(ms)"] = validate_rr_interval
    registry["338:生物电-心电图机:V4导联平均RR间期(ms)"] = validate_rr_interval
    registry["341:生物电-心电图机:V5导联平均RR间期(ms)"] = validate_rr_interval
    registry["344:生物电-心电图机:V6导联平均RR间期(ms)"] = validate_rr_interval
    
    # 心率
    registry["312:生物电-心电图机:I导联心房率(次/min)"] = validate_heart_rate
    registry["313:生物电-心电图机:I导联心室率(次/min)"] = validate_heart_rate
    registry["315:生物电-心电图机:II导联心房率(次/min)"] = validate_heart_rate
    registry["316:生物电-心电图机:II导联心室率(次/min)"] = validate_heart_rate
    registry["318:生物电-心电图机:III导联心房率(次/min)"] = validate_heart_rate
    registry["319:生物电-心电图机:III导联心室率(次/min)"] = validate_heart_rate
    registry["321:生物电-心电图机:aVR导联心房率(次/min)"] = validate_heart_rate
    registry["322:生物电-心电图机:aVR导联心室率(次/min)"] = validate_heart_rate
    registry["324:生物电-心电图机:aVL导联心房率(次/min)"] = validate_heart_rate
    registry["325:生物电-心电图机:aVL导联心室率(次/min)"] = validate_heart_rate
    registry["327:生物电-心电图机:aVF导联心房率(次/min)"] = validate_heart_rate
    registry["328:生物电-心电图机:aVF导联心室率(次/min)"] = validate_heart_rate
    registry["330:生物电-心电图机:V1导联心房率(次/min)"] = validate_heart_rate
    registry["331:生物电-心电图机:V1导联心室率(次/min)"] = validate_heart_rate
    registry["333:生物电-心电图机:V2导联心房率(次/min)"] = validate_heart_rate
    registry["334:生物电-心电图机:V2导联心室率(次/min)"] = validate_heart_rate
    registry["336:生物电-心电图机:V3导联心房率(次/min)"] = validate_heart_rate
    registry["337:生物电-心电图机:V3导联心室率(次/min)"] = validate_heart_rate
    registry["339:生物电-心电图机:V4导联心房率(次/min)"] = validate_heart_rate
    registry["340:生物电-心电图机:V4导联心室率(次/min)"] = validate_heart_rate
    registry["342:生物电-心电图机:V5导联心房率(次/min)"] = validate_heart_rate
    registry["343:生物电-心电图机:V5导联心室率(次/min)"] = validate_heart_rate
    registry["345:生物电-心电图机:V6导联心房率(次/min)"] = validate_heart_rate
    registry["346:生物电-心电图机:V6导联心室率(次/min)"] = validate_heart_rate
    
    # 其他导联P波时间
    registry["347:生物电-心电图机:V1导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["350:生物电-心电图机:V1导联P'波时限(ms)"] = validate_p_wave_time
    registry["352:生物电-心电图机:V1导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["354:生物电-心电图机:V1导联P波时限(ms)"] = validate_p_wave_time
    registry["357:生物电-心电图机:V2导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["360:生物电-心电图机:V2导联P'波时限(ms)"] = validate_p_wave_time
    registry["362:生物电-心电图机:V2导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["363:生物电-心电图机:V2导联P波时限(ms)"] = validate_p_wave_time
    registry["367:生物电-心电图机:V3导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["370:生物电-心电图机:V3导联P'波时限(ms)"] = validate_p_wave_time
    registry["372:生物电-心电图机:V3导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["373:生物电-心电图机:V3导联P波时限(ms)"] = validate_p_wave_time
    registry["376:生物电-心电图机:V4导联P'波时限(ms)"] = validate_p_wave_time
    registry["377:生物电-心电图机:V4导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["380:生物电-心电图机:V5导联P'波时限(ms)"] = validate_p_wave_time
    registry["381:生物电-心电图机:V5导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["384:生物电-心电图机:V4导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["393:生物电-心电图机:V4导联P波时限(ms)"] = validate_p_wave_time
    registry["397:生物电-心电图机:V5导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["398:生物电-心电图机:V5导联P波时限(ms)"] = validate_p_wave_time
    registry["400:生物电-心电图机:V6导联P'波时限(ms)"] = validate_p_wave_time
    registry["402:生物电-心电图机:V6导联P'波峰值时间(ms)"] = validate_p_wave_time
    registry["404:生物电-心电图机:V6导联P波峰值时间(ms)"] = validate_p_wave_time
    registry["405:生物电-心电图机:V6导联P波时限(ms)"] = validate_p_wave_time
    
    # 其他T波时间
    registry["407:生物电-心电图机:V6导联T'波峰值时间(ms)"] = validate_t_wave_time
    registry["409:生物电-心电图机:V6导联T'波时限(ms)"] = validate_t_wave_time
    registry["427:生物电-心电图机:aVF导联T'波峰值时间(ms)"] = validate_t_wave_time
    registry["428:生物电-心电图机:aVF导联T'波时限(ms)"] = validate_t_wave_time
    registry["449:生物电-心电图机:aVR导联T'波峰值时间(ms)"] = validate_t_wave_time
    registry["450:生物电-心电图机:aVR导联T'波时限(ms)"] = validate_t_wave_time
    
    # QRS波群时间
    registry["777:生物电-心电图机:III导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    registry["798:生物电-心电图机:II导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    registry["843:生物电-心电图机:I导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    registry["906:生物电-心电图机:V1导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    registry["934:生物电-心电图机:V2导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    registry["960:生物电-心电图机:V3导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    registry["986:生物电-心电图机:V4导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    registry["1019:生物电-心电图机:V5导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    registry["1021:生物电-心电图机:V6导联QRS波群类本位曲折时间(ms)"] = validate_qrs_complex_time
    
    # Q波时限
    registry["779:生物电-心电图机:III导联Q波时限(ms)"] = validate_q_wave_time
    registry["800:生物电-心电图机:II导联Q波时限(ms)"] = validate_q_wave_time
    registry["893:生物电-心电图机:I导联Q波时限(ms)"] = validate_q_wave_time
    registry["908:生物电-心电图机:V1导联Q波时限(ms)"] = validate_q_wave_time
    registry["937:生物电-心电图机:V2导联Q波时限(ms)"] = validate_q_wave_time
    registry["963:生物电-心电图机:V3导联Q波时限(ms)"] = validate_q_wave_time
    registry["989:生物电-心电图机:V4导联Q波时限(ms)"] = validate_q_wave_time
    registry["1010:生物电-心电图机:V5导联Q波时限(ms)"] = validate_q_wave_time
    registry["1033:生物电-心电图机:V6导联Q波时限(ms)"] = validate_q_wave_time
    
    # S波时限
    registry["784:生物电-心电图机:III导联S波时限(ms)"] = validate_s_wave_time
    registry["811:生物电-心电图机:II导联S波时限(ms)"] = validate_s_wave_time
    registry["901:生物电-心电图机:I导联S波时限(ms)"] = validate_s_wave_time
    registry["927:生物电-心电图机:V1导联S波时限(ms)"] = validate_s_wave_time
    registry["955:生物电-心电图机:V2导联S波时限(ms)"] = validate_s_wave_time
    registry["981:生物电-心电图机:V3导联S波时限(ms)"] = validate_s_wave_time
    registry["1002:生物电-心电图机:V4导联S波时限(ms)"] = validate_s_wave_time
    registry["1029:生物电-心电图机:V5导联S波时限(ms)"] = validate_s_wave_time
    registry["1038:生物电-心电图机:V6导联S波时限(ms)"] = validate_s_wave_time
    
    # ==================== 幅度类参数校验 ====================
    registry["37:生物电-心电图机:V6导联R'波幅值幅度(μV)"] = validate_ecg_amplitude_general
    registry["38:生物电-心电图机:V6导联R'波面积(μV*ms)"] = validate_ecg_amplitude_general
    registry["40:生物电-心电图机:V6导联S'波幅值幅度(μV)"] = validate_ecg_amplitude_general
    registry["43:生物电-心电图机:V6导联S'波面积(μV*ms)"] = validate_ecg_amplitude_general
    registry["45:生物电-心电图机:aVF导联R'波幅值幅度(μV)"] = validate_ecg_amplitude_general
    registry["47:生物电-心电图机:aVF导联R'波面积(μV*ms)"] = validate_ecg_amplitude_general
    registry["49:生物电-心电图机:aVL导联S'波幅值幅度(μV)"] = validate_ecg_amplitude_general
    registry["50:生物电-心电图机:aVL导联S'波面积(μV*ms)"] = validate_ecg_amplitude_general
    registry["53:生物电-心电图机:aVR导联S'波幅值幅度(μV)"] = validate_ecg_amplitude_general
    registry["54:生物电-心电图机:aVR导联S'波面积(μV*ms)"] = validate_ecg_amplitude_general
    
    # P波幅度
    registry["231:生物电-心电图机:III导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["233:生物电-心电图机:III导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["236:生物电-心电图机:III导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["237:生物电-心电图机:aVF导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["239:生物电-心电图机:II导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["241:生物电-心电图机:II导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["254:生物电-心电图机:II导联P波峰值幅度(μV)"] = validate_p_wave_amplitude
    registry["281:生物电-心电图机:II导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["289:生物电-心电图机:I导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["291:生物电-心电图机:I导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["292:生物电-心电图机:I导联P波峰值幅度(μV)"] = validate_p_wave_amplitude
    registry["296:生物电-心电图机:I导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["297:生物电-心电图机:I导联P波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["298:生物电-心电图机:I导联P波总面积(μV*ms)"] = validate_p_wave_amplitude
    
    # R波幅度
    registry["282:生物电-心电图机:II导联R'波幅值幅度(μV)"] = validate_r_wave_amplitude
    registry["283:生物电-心电图机:II导联R'波面积(μV*ms)"] = validate_r_wave_amplitude
    registry["300:生物电-心电图机:I导联R'波幅值幅度(μV)"] = validate_r_wave_amplitude
    registry["301:生物电-心电图机:I导联R'波面积(μV*ms)"] = validate_r_wave_amplitude
    
    # S波幅度
    registry["303:生物电-心电图机:I导联S'波幅值幅度(μV)"] = validate_s_wave_amplitude
    registry["306:生物电-心电图机:I导联S'波面积(μV*ms)"] = validate_s_wave_amplitude
    
    # T波幅度
    registry["284:生物电-心电图机:II导联T'波峰值幅度(uV)"] = validate_t_wave_amplitude
    registry["285:生物电-心电图机:II导联T'波面积(uV·ms)"] = validate_t_wave_amplitude
    registry["307:生物电-心电图机:I导联T'波峰值幅度(uV)"] = validate_t_wave_amplitude
    registry["308:生物电-心电图机:I导联T'波面积(uV·ms)"] = validate_t_wave_amplitude
    
    # 其他导联P波幅度
    registry["348:生物电-心电图机:V1导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["349:生物电-心电图机:V1导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["351:生物电-心电图机:V1导联P波峰值幅度(μV)"] = validate_p_wave_amplitude
    registry["353:生物电-心电图机:V1导联P波总面积(μV*ms)"] = validate_p_wave_amplitude
    registry["355:生物电-心电图机:V1导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["356:生物电-心电图机:V1导联P波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["358:生物电-心电图机:V2导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["359:生物电-心电图机:V2导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["361:生物电-心电图机:V2导联P波峰值幅度(μV)"] = validate_p_wave_amplitude
    registry["364:生物电-心电图机:V2导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["365:生物电-心电图机:V2导联P波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["366:生物电-心电图机:V2导联P波总面积(μV*ms)"] = validate_p_wave_amplitude
    registry["368:生物电-心电图机:V3导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["369:生物电-心电图机:V3导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["371:生物电-心电图机:V3导联P波峰值幅度(μV)"] = validate_p_wave_amplitude
    registry["374:生物电-心电图机:V3导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["375:生物电-心电图机:V4导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["378:生物电-心电图机:V4导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["379:生物电-心电图机:V5导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["382:生物电-心电图机:V5导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["383:生物电-心电图机:V4导联P波峰值幅度(μV)"] = validate_p_wave_amplitude
    registry["394:生物电-心电图机:V4导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["395:生物电-心电图机:V5导联P波峰值幅度(μV)"] = validate_p_wave_amplitude
    registry["396:生物电-心电图机:V6导联P波峰值幅度(μV)"] = validate_p_wave_amplitude
    registry["399:生物电-心电图机:V5导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    registry["401:生物电-心电图机:V6导联P'波幅值幅度(μV)"] = validate_p_wave_amplitude
    registry["403:生物电-心电图机:V6导联P'波面积(μV*ms)"] = validate_p_wave_amplitude
    registry["406:生物电-心电图机:V6导联P波起点幅度(μV)"] = validate_p_wave_amplitude
    
    # 其他T波幅度
    registry["408:生物电-心电图机:V6导联T'波峰值幅度(uV)"] = validate_t_wave_amplitude
    registry["410:生物电-心电图机:V6导联T'波面积(uV·ms)"] = validate_t_wave_amplitude
    registry["425:生物电-心电图机:aVF导联T'波峰值幅度(uV)"] = validate_t_wave_amplitude
    registry["426:生物电-心电图机:aVF导联T'波面积(uV·ms)"] = validate_t_wave_amplitude
    registry["448:生物电-心电图机:aVR导联T'波峰值幅度(uV)"] = validate_t_wave_amplitude
    registry["451:生物电-心电图机:aVR导联T'波面积(uV·ms)"] = validate_t_wave_amplitude
    registry["929:生物电-心电图机:V1导联T'波峰值幅度(uV)"] = validate_t_wave_amplitude
    registry["930:生物电-心电图机:V1导联T'波面积(uV·ms)"] = validate_t_wave_amplitude
    
    # aVR导联特殊校验（通常为负值）
    registry["443:生物电-心电图机:aVR导联P波峰值幅度(μV)"] = validate_aVR_p_wave_amplitude
    registry["445:生物电-心电图机:aVR导联P波起点幅度(μV)"] = validate_aVR_p_wave_amplitude
    registry["446:生物电-心电图机:aVR导联P波面积(μV*ms)"] = validate_aVR_p_wave_amplitude
    registry["447:生物电-心电图机:aVR导联P波总面积(μV*ms)"] = validate_aVR_p_wave_amplitude
    
    # Q波幅度
    registry["778:生物电-心电图机:III导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["781:生物电-心电图机:III导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    registry["799:生物电-心电图机:II导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["802:生物电-心电图机:II导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    registry["892:生物电-心电图机:I导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["895:生物电-心电图机:I导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    registry["907:生物电-心电图机:V1导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["910:生物电-心电图机:V1导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    registry["935:生物电-心电图机:V2导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["936:生物电-心电图机:V2导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    registry["961:生物电-心电图机:V3导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["962:生物电-心电图机:V3导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    registry["987:生物电-心电图机:V4导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["988:生物电-心电图机:V4导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    registry["1008:生物电-心电图机:V5导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["1009:生物电-心电图机:V5导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    registry["1031:生物电-心电图机:V6导联Q波幅值幅度(μV)"] = validate_q_wave_amplitude
    registry["1032:生物电-心电图机:V6导联Q波面积(μV*ms)"] = validate_q_wave_amplitude
    
    # S波幅度
    registry["783:生物电-心电图机:III导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["785:生物电-心电图机:III导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    registry["809:生物电-心电图机:II导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["812:生物电-心电图机:II导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    registry["899:生物电-心电图机:I导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["902:生物电-心电图机:I导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    registry["924:生物电-心电图机:V1导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["928:生物电-心电图机:V1导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    registry["953:生物电-心电图机:V2导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["956:生物电-心电图机:V2导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    registry["978:生物电-心电图机:V3导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["982:生物电-心电图机:V3导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    registry["1000:生物电-心电图机:V4导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["1003:生物电-心电图机:V4导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    registry["1027:生物电-心电图机:V5导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["1030:生物电-心电图机:V5导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    registry["1037:生物电-心电图机:V6导联S波峰值幅度(μV)"] = validate_s_wave_amplitude
    registry["1039:生物电-心电图机:V6导联S波面积(μV*ms)"] = validate_s_wave_amplitude
    
    # 最大R/S幅度
    registry["816:生物电-心电图机:II导联最大R幅度(μV)"] = validate_r_wave_amplitude
    registry["817:生物电-心电图机:II导联最大S幅度(μV)"] = validate_s_wave_amplitude
    registry["900:生物电-心电图机:I导联最大S幅度(μV)"] = validate_s_wave_amplitude
    registry["916:生物电-心电图机:V1导联最大R幅度(μV)"] = validate_r_wave_amplitude
    registry["925:生物电-心电图机:V1导联最大S幅度(μV)"] = validate_s_wave_amplitude
    registry["944:生物电-心电图机:V2导联最大R幅度(μV)"] = validate_r_wave_amplitude
    registry["954:生物电-心电图机:V2导联最大S幅度(μV)"] = validate_s_wave_amplitude
    registry["970:生物电-心电图机:V3导联最大R幅度(μV)"] = validate_r_wave_amplitude
    registry["979:生物电-心电图机:V3导联最大S幅度(μV)"] = validate_s_wave_amplitude
    registry["996:生物电-心电图机:V4导联最大R幅度(μV)"] = validate_r_wave_amplitude
    registry["1001:生物电-心电图机:V4导联最大S幅度(μV)"] = validate_s_wave_amplitude
    registry["1017:生物电-心电图机:V5导联最大R幅度(μV)"] = validate_r_wave_amplitude
    registry["1028:生物电-心电图机:V5导联最大S幅度(μV)"] = validate_s_wave_amplitude
    registry["1040:生物电-心电图机:V6导联QRS波群偏斜(μV)"] = validate_r_wave_amplitude
    
    # ==================== 电轴类参数校验 ====================
    registry["257:生物电-心电图机:I导联P波电轴(°)"] = validate_heart_axis
    registry["258:生物电-心电图机:II导联P波电轴(°)"] = validate_heart_axis
    registry["259:生物电-心电图机:III导联P波电轴(°)"] = validate_heart_axis
    registry["260:生物电-心电图机:aVR导联P波电轴(°)"] = validate_heart_axis
    registry["261:生物电-心电图机:aVL导联P波电轴(°)"] = validate_heart_axis
    registry["262:生物电-心电图机:aVF导联P波电轴(°)"] = validate_heart_axis
    registry["263:生物电-心电图机:V1导联P波电轴(°)"] = validate_heart_axis
    registry["264:生物电-心电图机:V2导联P波电轴(°)"] = validate_heart_axis
    registry["265:生物电-心电图机:V3导联P波电轴(°)"] = validate_heart_axis
    registry["266:生物电-心电图机:V4导联P波电轴(°)"] = validate_heart_axis
    registry["267:生物电-心电图机:V5导联P波电轴(°)"] = validate_heart_axis
    registry["268:生物电-心电图机:V6导联P波电轴(°)"] = validate_heart_axis
    
    # ==================== 起点/终点时间点校验 ====================
    registry["269:生物电-心电图机:I导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["270:生物电-心电图机:II导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["271:生物电-心电图机:III导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["272:生物电-心电图机:aVR导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["273:生物电-心电图机:aVL导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["274:生物电-心电图机:aVF导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["275:生物电-心电图机:V1导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["276:生物电-心电图机:V2导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["277:生物电-心电图机:V3导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["278:生物电-心电图机:V4导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["279:生物电-心电图机:V5导联P波起点(2ms)"] = validate_ecg_timepoint
    registry["280:生物电-心电图机:V6导联P波起点(2ms)"] = validate_ecg_timepoint
    
    registry["786:生物电-心电图机:I导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["787:生物电-心电图机:II导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["788:生物电-心电图机:III导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["789:生物电-心电图机:aVR导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["790:生物电-心电图机:aVL导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["791:生物电-心电图机:aVF导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["792:生物电-心电图机:V1导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["793:生物电-心电图机:V2导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["794:生物电-心电图机:V3导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["795:生物电-心电图机:V4导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["796:生物电-心电图机:V5导联P波终点(2ms)"] = validate_ecg_timepoint
    registry["797:生物电-心电图机:V6导联P波终点(2ms)"] = validate_ecg_timepoint
    
    registry["844:生物电-心电图机:I导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["846:生物电-心电图机:II导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["848:生物电-心电图机:III导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["850:生物电-心电图机:aVR导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["852:生物电-心电图机:aVL导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["854:生物电-心电图机:aVF导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["856:生物电-心电图机:V1导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["858:生物电-心电图机:V2导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["860:生物电-心电图机:V3导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["862:生物电-心电图机:V4导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["864:生物电-心电图机:V5导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    registry["866:生物电-心电图机:V6导联QRS波群终点(2ms)"] = validate_ecg_timepoint
    
    registry["845:生物电-心电图机:I导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["847:生物电-心电图机:II导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["849:生物电-心电图机:III导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["851:生物电-心电图机:aVR导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["853:生物电-心电图机:aVL导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["855:生物电-心电图机:aVF导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["857:生物电-心电图机:V1导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["859:生物电-心电图机:V2导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["861:生物电-心电图机:V3导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["863:生物电-心电图机:V4导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["865:生物电-心电图机:V5导联Q波终点(2ms)"] = validate_ecg_timepoint
    registry["867:生物电-心电图机:V6导联Q波终点(2ms)"] = validate_ecg_timepoint
    
    registry["868:生物电-心电图机:I导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["870:生物电-心电图机:II导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["872:生物电-心电图机:III导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["874:生物电-心电图机:aVR导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["876:生物电-心电图机:aVL导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["878:生物电-心电图机:aVF导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["880:生物电-心电图机:V1导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["882:生物电-心电图机:V2导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["884:生物电-心电图机:V3导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["886:生物电-心电图机:V4导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["888:生物电-心电图机:V5导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    registry["890:生物电-心电图机:V6导联QRS波群起点(2ms)"] = validate_ecg_timepoint
    
    registry["869:生物电-心电图机:I导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["871:生物电-心电图机:II导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["873:生物电-心电图机:III导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["875:生物电-心电图机:aVR导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["877:生物电-心电图机:aVL导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["879:生物电-心电图机:aVF导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["881:生物电-心电图机:V1导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["883:生物电-心电图机:V2导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["885:生物电-心电图机:V3导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["887:生物电-心电图机:V4导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["889:生物电-心电图机:V5导联Q波起点(2ms)"] = validate_ecg_timepoint
    registry["891:生物电-心电图机:V6导联Q波起点(2ms)"] = validate_ecg_timepoint
    
    # ==================== 数量类校验 ====================
    registry["818:生物电-心电图机:I导联QRS波群的数量(个)"] = validate_ecg_count
    registry["819:生物电-心电图机:I导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["820:生物电-心电图机:II导联QRS波群的数量(个)"] = validate_ecg_count
    registry["821:生物电-心电图机:II导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["822:生物电-心电图机:III导联QRS波群的数量(个)"] = validate_ecg_count
    registry["823:生物电-心电图机:III导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["824:生物电-心电图机:aVR导联QRS波群的数量(个)"] = validate_ecg_count
    registry["825:生物电-心电图机:aVR导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["826:生物电-心电图机:aVL导联QRS波群的数量(个)"] = validate_ecg_count
    registry["827:生物电-心电图机:aVL导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["828:生物电-心电图机:aVF导联QRS波群的数量(个)"] = validate_ecg_count
    registry["829:生物电-心电图机:aVF导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["830:生物电-心电图机:V1导联QRS波群的数量(个)"] = validate_ecg_count
    registry["831:生物电-心电图机:V1导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["832:生物电-心电图机:V2导联QRS波群的数量(个)"] = validate_ecg_count
    registry["833:生物电-心电图机:V2导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["834:生物电-心电图机:V3导联QRS波群的数量(个)"] = validate_ecg_count
    registry["835:生物电-心电图机:V3导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["836:生物电-心电图机:V4导联QRS波群的数量(个)"] = validate_ecg_count
    registry["837:生物电-心电图机:V4导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["838:生物电-心电图机:V5导联QRS波群的数量(个)"] = validate_ecg_count
    registry["839:生物电-心电图机:V5导联QRS波群时限(ms)"] = validate_ecg_time_general
    registry["840:生物电-心电图机:V6导联QRS波群的数量(个)"] = validate_ecg_count
    registry["841:生物电-心电图机:V6导联QRS波群时限(ms)"] = validate_ecg_time_general
    
    # ==================== 面积类校验 ====================
    registry["842:生物电-心电图机:I导联QRS波群的面积(μV*ms)"] = validate_ecg_area
    registry["905:生物电-心电图机:V1导联QRS波群的面积(μV*ms)"] = validate_ecg_area
    registry["933:生物电-心电图机:V2导联QRS波群的面积(μV*ms)"] = validate_ecg_area
    registry["959:生物电-心电图机:V3导联QRS波群的面积(μV*ms)"] = validate_ecg_area
    registry["985:生物电-心电图机:V4导联QRS波群的面积(μV*ms)"] = validate_ecg_area
    registry["1006:生物电-心电图机:V5导联QRS波群的面积(μV*ms)"] = validate_ecg_area
    registry["1007:生物电-心电图机:V6导联QRS波群的面积(μV*ms)"] = validate_ecg_area
    
    # ==================== 偏斜/平衡类校验 ====================
    registry["813:生物电-心电图机:II导联QRS波群偏斜(μV)"] = validate_ecg_amplitude_general
    registry["814:生物电-心电图机:II导联QRS波群平衡(μV)"] = validate_ecg_amplitude_general
    registry["903:生物电-心电图机:V1导联QRS波群偏斜(μV)"] = validate_ecg_amplitude_general
    registry["904:生物电-心电图机:V1导联QRS波群平衡(μV)"] = validate_ecg_amplitude_general
    registry["931:生物电-心电图机:V2导联QRS波群偏斜(μV)"] = validate_ecg_amplitude_general
    registry["932:生物电-心电图机:V2导联QRS波群平衡(μV)"] = validate_ecg_amplitude_general
    registry["957:生物电-心电图机:V3导联QRS波群偏斜(μV)"] = validate_ecg_amplitude_general
    registry["958:生物电-心电图机:V3导联QRS波群平衡(μV)"] = validate_ecg_amplitude_general
    registry["983:生物电-心电图机:V4导联QRS波群偏斜(μV)"] = validate_ecg_amplitude_general
    registry["984:生物电-心电图机:V4导联QRS波群平衡(μV)"] = validate_ecg_amplitude_general
    registry["1004:生物电-心电图机:V5导联QRS波群偏斜(μV)"] = validate_ecg_amplitude_general
    registry["1005:生物电-心电图机:V5导联QRS波群平衡(μV)"] = validate_ecg_amplitude_general
    registry["1041:生物电-心电图机:V6导联最大R幅度(μV)"] = validate_r_wave_amplitude


# ==============================
# 核心校验函数（保持不变）
# ==============================

def validate_ecg_time_general(feature_key, final_value, payload) -> bool:
    """
    通用 ECG 时间参数校验：0 ~ 5000 ms 之间。
    """
    try:
        val = float(final_value)
    except (ValueError, TypeError):
        return False
    return 0 <= val <= 5000


def validate_p_wave_time(feature_key, final_value, payload) -> bool:
    """
    P 波时间参数：10 ~ 300 ms 之间。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 10 <= val <= 300


def validate_pr_interval(feature_key, final_value, payload) -> bool:
    """
    PR 间期：80 ~ 400 ms 之间。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 80 <= val <= 400


def validate_qrs_complex_time(feature_key, final_value, payload) -> bool:
    """
    QRS 波群类本位曲折时间：20 ~ 150 ms。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 20 <= val <= 150


def validate_q_wave_time(feature_key, final_value, payload) -> bool:
    """
    Q 波时限：0 ~ 100 ms。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= val <= 100


def validate_s_wave_time(feature_key, final_value, payload) -> bool:
    """
    S 波时限：0 ~ 150 ms。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= val <= 150


def validate_t_wave_time(feature_key, final_value, payload) -> bool:
    """
    T 波时间参数：20 ~ 400 ms。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 20 <= val <= 400


def validate_rr_interval(feature_key, final_value, payload) -> bool:
    """
    RR 间期：300 ~ 2000 ms。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 300 <= val <= 2000


def validate_heart_rate(feature_key, final_value, payload) -> bool:
    """
    心率：30 ~ 200 bpm。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 30 <= val <= 200


def validate_ecg_amplitude_general(feature_key, final_value, payload) -> bool:
    """
    通用 ECG 幅度参数校验：-10000 ~ +10000 μV 之间。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return -10000 <= val <= 10000


def validate_p_wave_amplitude(feature_key, final_value, payload) -> bool:
    """
    P 波幅度：-500 ~ +500 μV 之间。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return -500 <= val <= 500


def validate_aVR_p_wave_amplitude(feature_key, final_value, payload) -> bool:
    """
    aVR 导联 P 波幅度：通常为负值，范围 -500 ~ 0 μV。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return -500 <= val <= 0


def validate_q_wave_amplitude(feature_key, final_value, payload) -> bool:
    """
    Q 波幅度：通常为负值，范围 -5000 ~ 0 μV。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return -5000 <= val <= 0


def validate_r_wave_amplitude(feature_key, final_value, payload) -> bool:
    """
    R 波幅度：0 ~ 5000 μV。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= val <= 5000


def validate_s_wave_amplitude(feature_key, final_value, payload) -> bool:
    """
    S 波幅度：通常为负值，范围 -5000 ~ 0 μV。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return -5000 <= val <= 0


def validate_t_wave_amplitude(feature_key, final_value, payload) -> bool:
    """
    T 波幅度：-1000 ~ +1000 μV。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return -1000 <= val <= 1000


def validate_heart_axis(feature_key, final_value, payload) -> bool:
    """
    心电轴：-180° ~ +180°。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return -180 <= val <= 180


def validate_ecg_timepoint(feature_key, final_value, payload) -> bool:
    """
    ECG 时间点（2ms单位）：0 ~ 2000 ms。
    """
    try:
        val = float(final_value) * 2  # 转换为 ms
    except (TypeError, ValueError):
        return False
    return 0 <= val <= 2000


def validate_ecg_count(feature_key, final_value, payload) -> bool:
    """
    ECG 波群数量：1 ~ 200 个。
    """
    try:
        val = int(final_value)
    except (TypeError, ValueError):
        return False
    return 1 <= val <= 200


def validate_ecg_area(feature_key, final_value, payload) -> bool:
    """
    ECG 面积参数：-100000 ~ +100000 μV*ms。
    """
    try:
        val = float(final_value)
    except (TypeError, ValueError):
        return False
    return -100000 <= val <= 100000