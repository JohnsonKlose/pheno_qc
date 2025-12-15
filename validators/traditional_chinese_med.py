"""Validators for The Four Diagnostic Methods of Traditional Chinese Medicine features."""


def register(registry, prefix_registry):
    registry["37487:中医表型-中医四诊:不耐寒"] = is_between_1_and_5
    registry["37488:中医表型-中医四诊:不耐寒"] = is_between_1_and_5
    registry["37489:中医表型-中医四诊:不耐寒"] = is_between_1_and_5
    registry["37490:中医表型-中医四诊:怕冷"] = is_between_1_and_5
    registry["37491:中医表型-中医四诊:怕冷"] = is_between_1_and_5
    registry["37492:中医表型-中医四诊:怕冷"] = is_between_1_and_5
    registry["37493:中医表型-中医四诊:手脚发凉"] = is_between_1_and_5
    registry["37494:中医表型-中医四诊:手脚发凉"] = is_between_1_and_5
    registry["37495:中医表型-中医四诊:手脚发凉"] = is_between_1_and_5
    registry["37496:中医表型-中医四诊:阴囊潮湿(男)"] = is_between_1_and_5
    registry["37497:中医表型-中医四诊:阴囊潮湿(男)"] = is_between_1_and_5
    registry["37498:中医表型-中医四诊:痤疮\疮疖"] = is_between_1_and_5
    registry["37499:中医表型-中医四诊:痤疮\疮疖"] = is_between_1_and_5
    registry["37500:中医表型-中医四诊:痤疮\疮疖"] = is_between_1_and_5
    registry["37501:中医表型-中医四诊:腹部肥满松软"] = is_between_1_and_5
    registry["37502:中医表型-中医四诊:腹部肥满松软"] = is_between_1_and_5
    registry["37503:中医表型-中医四诊:腹部肥满松软"] = is_between_1_and_5
    registry["37504:中医表型-中医四诊:面部\鼻部油腻感"] = is_between_1_and_5
    registry["37505:中医表型-中医四诊:面部\鼻部油腻感"] = is_between_1_and_5
    registry["37506:中医表型-中医四诊:面部\鼻部油腻感"] = is_between_1_and_5
    registry["37507:中医表型-中医四诊:面部\鼻部油腻感"] = is_between_1_and_5
    registry["37508:中医表型-中医四诊:额部油脂分泌过多"] = is_between_1_and_5
    registry["37509:中医表型-中医四诊:额部油脂分泌过多"] = is_between_1_and_5
    registry["37510:中医表型-中医四诊:额部油脂分泌过多"] = is_between_1_and_5
    registry["37511:中医表型-中医四诊:额部油脂分泌过多"] = is_between_1_and_5
    registry["37512:中医表型-中医四诊:黑眼圈"] = is_between_1_and_5
    registry["37513:中医表型-中医四诊:黑眼圈"] = is_between_1_and_5
    registry["37514:中医表型-中医四诊:黑眼圈"] = is_between_1_and_5
    registry["37515:中医表型-中医四诊:黑眼圈"] = is_between_1_and_5
    registry["37516:中医表型-中医四诊:上眼睑肿"] = is_between_1_and_5
    registry["37517:中医表型-中医四诊:上眼睑肿"] = is_between_1_and_5
    registry["37518:中医表型-中医四诊:上眼睑肿"] = is_between_1_and_5
    registry["37519:中医表型-中医四诊:不耐寒"] = is_between_1_and_5
    registry["37520:中医表型-中医四诊:两颧潮红或偏红"] = is_between_1_and_5
    registry["37521:中医表型-中医四诊:两颧潮红或偏红"] = is_between_1_and_5
    registry["37522:中医表型-中医四诊:两颧潮红或偏红"] = is_between_1_and_5
    registry["37523:中医表型-中医四诊:两颧部有细微红丝"] = is_between_1_and_5
    registry["37524:中医表型-中医四诊:两颧部有细微红丝"] = is_between_1_and_5
    registry["37525:中医表型-中医四诊:两颧部有细微红丝"] = is_between_1_and_5
    registry["37526:中医表型-中医四诊:体质"] = _is_not_empty
    registry["37527:中医表型-中医四诊:便秘\大便干燥"] = is_between_1_and_5
    registry["37528:中医表型-中医四诊:健忘"] = is_between_1_and_5
    registry["37529:中医表型-中医四诊:受凉或吃(喝)凉的东西后，腹泻(拉肚子)"] = is_between_1_and_5
    registry["37530:中医表型-中医四诊:受凉或吃(喝)凉的东西后，腹泻(拉肚子)"] = is_between_1_and_5
    registry["37531:中医表型-中医四诊:受凉或吃(喝)凉的东西后，腹泻(拉肚子)"] = is_between_1_and_5
    registry["37532:中医表型-中医四诊:受凉或吃(喝)凉的东西后，腹泻(拉肚子)"] = is_between_1_and_5
    registry["37533:中医表型-中医四诊:口唇的颜色红"] = is_between_1_and_5
    registry["37534:中医表型-中医四诊:口唇的颜色红"] = is_between_1_and_5
    registry["37535:中医表型-中医四诊:口唇的颜色红"] = is_between_1_and_5
    registry["37536:中医表型-中医四诊:口唇颜色偏黯"] = is_between_1_and_5
    registry["37537:中医表型-中医四诊:口唇颜色偏黯"] = is_between_1_and_5
    registry["37538:中医表型-中医四诊:口唇颜色偏黯"] = is_between_1_and_5
    registry["37539:中医表型-中医四诊:口唇颜色偏黯"] = is_between_1_and_5
    registry["37540:中医表型-中医四诊:口干咽燥"] = is_between_1_and_5
    registry["37541:中医表型-中医四诊:口干咽燥"] = is_between_1_and_5
    registry["37542:中医表型-中医四诊:口苦\嘴里有异味"] = is_between_1_and_5
    registry["37543:中医表型-中医四诊:口苦\嘴里有异味"] = is_between_1_and_5
    registry["37544:中医表型-中医四诊:口苦\嘴里有异味"] = is_between_1_and_5
    registry["37545:中医表型-中医四诊:吃(喝)凉的东西感到不舒服或怕吃(喝)凉东西"] = is_between_1_and_5
    registry["37546:中医表型-中医四诊:吃(喝)凉的东西感到不舒服或怕吃(喝)凉东西"] = is_between_1_and_5
    registry["37547:中医表型-中医四诊:吃(喝)凉的东西感到不舒服或怕吃(喝)凉东西"] = is_between_1_and_5
    registry["37548:中医表型-中医四诊:吃(喝)凉的东西感到不舒服或怕吃(喝)凉东西"] = is_between_1_and_5
    registry["37549:中医表型-中医四诊:咽喉部有异物感"] = is_between_1_and_5
    registry["37550:中医表型-中医四诊:咽喉部有异物感"] = is_between_1_and_5
    registry["37551:中医表型-中医四诊:咽喉部有异物感"] = is_between_1_and_5
    registry["37552:中医表型-中医四诊:喜欢安静、懒得说话"] = is_between_1_and_5
    registry["37553:中医表型-中医四诊:嘴黏"] = is_between_1_and_5
    registry["37554:中医表型-中医四诊:嘴黏"] = is_between_1_and_5
    registry["37555:中医表型-中医四诊:嘴黏"] = is_between_1_and_5
    registry["37556:中医表型-中医四诊:因季节变化、温度变化或异味等原因咳喘"] = is_between_1_and_5
    registry["37557:中医表型-中医四诊:因季节变化、温度变化或异味等原因咳喘"] = is_between_1_and_5
    registry["37558:中医表型-中医四诊:因季节变化、温度变化或异味等原因咳喘"] = is_between_1_and_5
    registry["37559:中医表型-中医四诊:因过敏出现紫癜"] = is_between_1_and_5
    registry["37560:中医表型-中医四诊:因过敏出现紫癜"] = is_between_1_and_5
    registry["37561:中医表型-中医四诊:声音无力"] = is_between_1_and_5
    registry["37562:中医表型-中医四诊:声音无力"] = is_between_1_and_5
    registry["37563:中医表型-中医四诊:声音无力"] = is_between_1_and_5
    registry["37564:中医表型-中医四诊:多愁善感、感情脆弱"] = is_between_1_and_5
    registry["37565:中医表型-中医四诊:大便黏滞不爽、解不尽"] = is_between_1_and_5
    registry["37566:中医表型-中医四诊:大便黏滞不爽、解不尽"] = is_between_1_and_5
    registry["37567:中医表型-中医四诊:失眠"] = is_between_1_and_5
    registry["37568:中医表型-中医四诊:头晕或站起时晕眩"] = is_between_1_and_5
    registry["37569:中医表型-中医四诊:头晕或站起时晕眩"] = is_between_1_and_5
    registry["37570:中医表型-中医四诊:容易害怕或受到惊吓"] = is_between_1_and_5
    registry["37571:中医表型-中医四诊:容易害怕或受到惊吓"] = is_between_1_and_5
    registry["37572:中医表型-中医四诊:容易感冒"] = is_between_1_and_5
    registry["37573:中医表型-中医四诊:容易感冒"] = is_between_1_and_5
    registry["37574:中医表型-中医四诊:容易感冒"] = is_between_1_and_5
    registry["37575:中医表型-中医四诊:小便时尿道发热、尿色浓"] = is_between_1_and_5
    registry["37576:中医表型-中医四诊:小便时尿道发热、尿色浓"] = is_between_1_and_5
    registry["37577:中医表型-中医四诊:小便时尿道发热、尿色浓"] = is_between_1_and_5
    registry["37578:中医表型-中医四诊:带下色黄(女)"] = is_between_1_and_5
    registry["37579:中医表型-中医四诊:带下色黄(女)"] = is_between_1_and_5
    registry["37580:中医表型-中医四诊:带下色黄(女)"] = is_between_1_and_5
    registry["37581:中医表型-中医四诊:平和质得分(分)"] = is_between_1_and_5
    registry["37582:中医表型-中医四诊:心慌"] = is_between_1_and_5
    registry["37583:中医表型-中医四诊:心慌"] = is_between_1_and_5
    registry["37584:中医表型-中医四诊:心慌"] = is_between_1_and_5
    registry["37585:中医表型-中医四诊:怕冷"] = is_between_1_and_5
    registry["37586:中医表型-中医四诊:手脚发凉"] = is_between_1_and_5
    registry["37587:中医表型-中医四诊:手脚心发热"] = is_between_1_and_5
    registry["37588:中医表型-中医四诊:手脚心发热"] = is_between_1_and_5
    registry["37589:中医表型-中医四诊:手脚心发热"] = is_between_1_and_5
    registry["37590:中医表型-中医四诊:无缘无故叹气"] = is_between_1_and_5
    registry["37591:中医表型-中医四诊:无缘无故叹气"] = is_between_1_and_5
    registry["37592:中医表型-中医四诊:气短"] = is_between_1_and_5
    registry["37593:中医表型-中医四诊:气短"] = is_between_1_and_5
    registry["37594:中医表型-中医四诊:气短"] = is_between_1_and_5
    registry["37595:中医表型-中医四诊:气虚质得分(分)"] = _is_not_empty
    registry["37596:中医表型-中医四诊:气郁质得分(分)"] = _is_not_empty
    registry["37597:中医表型-中医四诊:没有感冒也会打喷嚏"] = is_between_1_and_5
    registry["37598:中医表型-中医四诊:没有感冒也会打喷嚏"] = is_between_1_and_5
    registry["37599:中医表型-中医四诊:没有感冒也会打喷嚏"] = is_between_1_and_5
    registry["37600:中医表型-中医四诊:没有感冒也会打喷嚏"] = is_between_1_and_5
    registry["37601:中医表型-中医四诊:没有感冒也会鼻塞、流鼻涕"] = is_between_1_and_5
    registry["37602:中医表型-中医四诊:没有感冒也会鼻塞、流鼻涕"] = is_between_1_and_5
    registry["37603:中医表型-中医四诊:没有感冒也会鼻塞、流鼻涕"] = is_between_1_and_5
    registry["37604:中医表型-中医四诊:活动量稍大就容易出虚汗"] = is_between_1_and_5
    registry["37605:中医表型-中医四诊:湿热质得分(分)"] = _is_not_empty
    registry["37606:中医表型-中医四诊:特禀质得分(分)"] = _is_not_empty
    registry["37607:中医表型-中医四诊:痤疮\疮疖"] = is_between_1_and_5
    registry["37608:中医表型-中医四诊:痰多，咽喉部有痰"] = is_between_1_and_5
    registry["37609:中医表型-中医四诊:痰多，咽喉部有痰"] = is_between_1_and_5
    registry["37610:中医表型-中医四诊:痰多，咽喉部有痰"] = is_between_1_and_5
    registry["37611:中医表型-中医四诊:痰湿质得分(分)"] = _is_not_empty
    registry["37612:中医表型-中医四诊:皮肤一抓就红并出现抓痕"] = is_between_1_and_5
    registry["37613:中医表型-中医四诊:皮肤一抓就红并出现抓痕"] = is_between_1_and_5
    registry["37614:中医表型-中医四诊:皮肤一抓就红并出现抓痕"] = is_between_1_and_5
    registry["37615:中医表型-中医四诊:皮肤一抓就红并出现抓痕"] = is_between_1_and_5
    registry["37616:中医表型-中医四诊:皮肤青紫瘀斑"] = is_between_1_and_5
    registry["37617:中医表型-中医四诊:皮肤青紫瘀斑"] = is_between_1_and_5
    registry["37618:中医表型-中医四诊:皮肤青紫瘀斑"] = is_between_1_and_5
    registry["37619:中医表型-中医四诊:眼睛干涩"] = is_between_1_and_5
    registry["37620:中医表型-中医四诊:精神紧张"] = is_between_1_and_5
    registry["37621:中医表型-中医四诊:胁肋部\乳房胀痛"] = is_between_1_and_5
    registry["37622:中医表型-中医四诊:胁肋部\乳房胀痛"] = is_between_1_and_5
    registry["37623:中医表型-中医四诊:胁肋部\乳房胀痛"] = is_between_1_and_5
    registry["37624:中医表型-中医四诊:胃脘部、背部或腰膝部有冷感"] = is_between_1_and_5
    registry["37625:中医表型-中医四诊:胃脘部、背部或腰膝部有冷感"] = is_between_1_and_5
    registry["37626:中医表型-中医四诊:胃脘部、背部或腰膝部有冷感"] = is_between_1_and_5
    registry["37627:中医表型-中医四诊:胸闷\腹部胀满"] = is_between_1_and_5
    registry["37628:中医表型-中医四诊:胸闷\腹部胀满"] = is_between_1_and_5
    registry["37629:中医表型-中医四诊:胸闷\腹部胀满"] = is_between_1_and_5
    registry["37630:中医表型-中医四诊:腹部肥满松软"] = is_between_1_and_5
    registry["37631:中医表型-中医四诊:舌苔厚腻"] = is_between_1_and_5
    registry["37632:中医表型-中医四诊:舌苔厚腻"] = is_between_1_and_5
    registry["37633:中医表型-中医四诊:舌苔厚腻"] = is_between_1_and_5
    registry["37634:中医表型-中医四诊:荨麻疹(风团、风疹块、风疙瘩)"] = is_between_1_and_5
    registry["37635:中医表型-中医四诊:荨麻疹(风团、风疹块、风疙瘩)"] = is_between_1_and_5
    registry["37636:中医表型-中医四诊:荨麻疹(风团、风疹块、风疙瘩)"] = is_between_1_and_5
    registry["37637:中医表型-中医四诊:血瘀质得分(分)"] = _is_not_empty
    registry["37638:中医表型-中医四诊:身体、脸上发热"] = is_between_1_and_5
    registry["37639:中医表型-中医四诊:身体、脸上发热"] = is_between_1_and_5
    registry["37640:中医表型-中医四诊:身体、脸上发热"] = is_between_1_and_5
    registry["37641:中医表型-中医四诊:身体不轻松或不爽快"] = is_between_1_and_5
    registry["37642:中医表型-中医四诊:身体不轻松或不爽快"] = is_between_1_and_5
    registry["37643:中医表型-中医四诊:身体疼痛"] = is_between_1_and_5
    registry["37644:中医表型-中医四诊:身体疼痛"] = is_between_1_and_5
    registry["37645:中医表型-中医四诊:身体疼痛"] = is_between_1_and_5
    registry["37646:中医表型-中医四诊:过敏"] = is_between_1_and_5
    registry["37647:中医表型-中医四诊:过敏"] = is_between_1_and_5
    registry["37648:中医表型-中医四诊:过敏"] = is_between_1_and_5
    registry["37649:中医表型-中医四诊:适应外界自然和社会环境的变化"] = is_between_1_and_5
    registry["37650:中医表型-中医四诊:适应外界自然和社会环境的变化"] = is_between_1_and_5
    registry["37651:中医表型-中医四诊:适应外界自然和社会环境的变化"] = is_between_1_and_5
    registry["37652:中医表型-中医四诊:闷闷不乐"] = is_between_1_and_5
    registry["37653:中医表型-中医四诊:阳虚质得分(分)"] = _is_not_empty
    registry["37654:中医表型-中医四诊:阴囊潮湿(男)"] = is_between_1_and_5
    registry["37655:中医表型-中医四诊:阴虚质得分(分)"] = _is_not_empty
    registry["37656:中医表型-中医四诊:面色晦黯\容易出现褐斑"] = is_between_1_and_5
    registry["37657:中医表型-中医四诊:面色晦黯\容易出现褐斑"] = is_between_1_and_5
    registry["37658:中医表型-中医四诊:面色晦黯\容易出现褐斑"] = is_between_1_and_5
    registry["37659:中医表型-中医四诊:面部\鼻部油腻感"] = is_between_1_and_5
    registry["37660:中医表型-中医四诊:额部油脂分泌过多"] = is_between_1_and_5
    registry["37661:中医表型-中医四诊:黑眼圈"] = is_between_1_and_5
    registry["37662:中医表型-中医四诊:舌色"] = _is_not_empty
    registry["37663:中医表型-中医四诊:舌象-全舌-舌色(Lab值)_L"] = _validate_lab_value
    registry["37664:中医表型-中医四诊:舌象-全舌-舌色(Lab值)_a"] = _validate_lab_value
    registry["37665:中医表型-中医四诊:舌象-全舌-舌色(Lab值)_b"] = _validate_lab_value
    registry["37666:中医表型-中医四诊:舌象-全舌-苔色(Lab值)_L"] = _validate_lab_value
    registry["37667:中医表型-中医四诊:舌象-全舌-苔色(Lab值)_a"] = _validate_lab_value
    registry["37668:中医表型-中医四诊:舌象-全舌-苔色(Lab值)_b"] = _validate_lab_value
    registry["37669:中医表型-中医四诊:舌象-舌中-苔色(Lab值)_L"] = _validate_lab_value
    registry["37670:中医表型-中医四诊:舌象-舌中-苔色(Lab值)_a"] = _validate_lab_value
    registry["37671:中医表型-中医四诊:舌象-舌中-苔色(Lab值)_b"] = _validate_lab_value
    registry["37672:中医表型-中医四诊:舌象-舌尖-舌色(Lab值)_L"] = _validate_lab_value
    registry["37673:中医表型-中医四诊:舌象-舌尖-舌色(Lab值)_a"] = _validate_lab_value
    registry["37674:中医表型-中医四诊:舌象-舌尖-舌色(Lab值)_b"] = _validate_lab_value
    registry["37675:中医表型-中医四诊:舌象-舌根-苔色(Lab值)_L"] = _validate_lab_value
    registry["37676:中医表型-中医四诊:舌象-舌根-苔色(Lab值)_a"] = _validate_lab_value
    registry["37677:中医表型-中医四诊:舌象-舌根-苔色(Lab值)_b"] = _validate_lab_value
    registry["37678:中医表型-中医四诊:舌象-舌边(右)-舌色(Lab值)_L"] = _validate_lab_value
    registry["37679:中医表型-中医四诊:舌象-舌边(右)-舌色(Lab值)_a"] = _validate_lab_value
    registry["37680:中医表型-中医四诊:舌象-舌边(右)-舌色(Lab值)_b"] = _validate_lab_value
    registry["37681:中医表型-中医四诊:舌象-舌边(左)-舌色(Lab值)_L"] = _validate_lab_value
    registry["37682:中医表型-中医四诊:舌象-舌边(左)-舌色(Lab值)_a"] = _validate_lab_value
    registry["37683:中医表型-中医四诊:舌象-舌边(左)-舌色(Lab值)_b"] = _validate_lab_value
    registry["37684:中医表型-中医四诊:苔色"] = _is_not_empty
    registry["37685:中医表型-中医四诊:苔色"] = _is_not_empty
    registry["37686:中医表型-中医四诊:苔色"] = _is_not_empty
    registry["37687:中医表型-中医四诊:苔色"] = _is_not_empty
    registry["37688:中医表型-中医四诊:苔质"] = _is_not_empty
    registry["37689:中医表型-中医四诊:苔质"] = _is_not_empty
    registry["37690:中医表型-中医四诊:苔质"] = _is_not_empty
    registry["37691:中医表型-中医四诊:面象-唇色-面色(Lab值)_L"] = _validate_lab_value
    registry["37692:中医表型-中医四诊:面象-唇色-面色(Lab值)_a"] = _validate_lab_value
    registry["37693:中医表型-中医四诊:面象-唇色-面色(Lab值)_b"] = _validate_lab_value
    registry["37694:中医表型-中医四诊:面象-眼眶-面色(Lab值)_L"] = _validate_lab_value
    registry["37695:中医表型-中医四诊:面象-眼眶-面色(Lab值)_a"] = _validate_lab_value
    registry["37696:中医表型-中医四诊:面象-眼眶-面色(Lab值)_b"] = _validate_lab_value
    registry["37697:中医表型-中医四诊:面象-脸颊(右)-面色(Lab值)_L"] = _validate_lab_value
    registry["37698:中医表型-中医四诊:面象-脸颊(右)-面色(Lab值)_a"] = _validate_lab_value
    registry["37699:中医表型-中医四诊:面象-脸颊(右)-面色(Lab值)_b"] = _validate_lab_value
    registry["37700:中医表型-中医四诊:面象-脸颊(左)-面色(Lab值)_L"] = _validate_lab_value
    registry["37701:中医表型-中医四诊:面象-脸颊(左)-面色(Lab值)_a"] = _validate_lab_value
    registry["37702:中医表型-中医四诊:面象-脸颊(左)-面色(Lab值)_b"] = _validate_lab_value
    registry["37703:中医表型-中医四诊:面象-面部总体-面色(Lab值)_L"] = _validate_lab_value
    registry["37704:中医表型-中医四诊:面象-面部总体-面色(Lab值)_a"] = _validate_lab_value
    registry["37705:中医表型-中医四诊:面象-面部总体-面色(Lab值)_b"] = _validate_lab_value
    registry["37706:中医表型-中医四诊:面象-额头-面色(Lab值)_L"] = _validate_lab_value
    registry["37707:中医表型-中医四诊:面象-额头-面色(Lab值)_a"] = _validate_lab_value
    registry["37708:中医表型-中医四诊:面象-额头-面色(Lab值)_b"] = _validate_lab_value
    registry["37709:中医表型-中医四诊:面象-鼻-面色(Lab值)_L"] = _validate_lab_value
    registry["37710:中医表型-中医四诊:面象-鼻-面色(Lab值)_a"] = _validate_lab_value
    registry["37711:中医表型-中医四诊:面象-鼻-面色(Lab值)_b"] = _validate_lab_value
    registry["37712:中医表型-中医四诊:便秘\大便干燥"] = is_between_1_and_5
    registry["37713:中医表型-中医四诊:便秘\大便干燥"] = is_between_1_and_5
    registry["37714:中医表型-中医四诊:便秘\大便干燥"] = is_between_1_and_5
    registry["37715:中医表型-中医四诊:健忘"] = is_between_1_and_5
    registry["37716:中医表型-中医四诊:健忘"] = is_between_1_and_5
    registry["37717:中医表型-中医四诊:健忘"] = is_between_1_and_5
    registry["37718:中医表型-中医四诊:口干咽燥"] = is_between_1_and_5
    registry["37719:中医表型-中医四诊:口干咽燥"] = is_between_1_and_5
    registry["37720:中医表型-中医四诊:喜欢安静、懒得说话"] = is_between_1_and_5
    registry["37721:中医表型-中医四诊:喜欢安静、懒得说话"] = is_between_1_and_5
    registry["37722:中医表型-中医四诊:喜欢安静、懒得说话"] = is_between_1_and_5
    registry["37723:中医表型-中医四诊:多愁善感、感情脆弱"] = is_between_1_and_5
    registry["37724:中医表型-中医四诊:多愁善感、感情脆弱"] = is_between_1_and_5
    registry["37725:中医表型-中医四诊:多愁善感、感情脆弱"] = is_between_1_and_5
    registry["37726:中医表型-中医四诊:大便黏滞不爽、解不尽"] = is_between_1_and_5
    registry["37727:中医表型-中医四诊:大便黏滞不爽、解不尽"] = is_between_1_and_5
    registry["37728:中医表型-中医四诊:失眠"] = is_between_1_and_5
    registry["37729:中医表型-中医四诊:失眠"] = is_between_1_and_5
    registry["37730:中医表型-中医四诊:头晕或站起时晕眩"] = is_between_1_and_5
    registry["37731:中医表型-中医四诊:头晕或站起时晕眩"] = is_between_1_and_5
    registry["37732:中医表型-中医四诊:容易害怕或受到惊吓"] = is_between_1_and_5
    registry["37733:中医表型-中医四诊:无缘无故叹气"] = is_between_1_and_5
    registry["37734:中医表型-中医四诊:易疲乏"] = is_between_1_and_5
    registry["37735:中医表型-中医四诊:易疲乏"] = is_between_1_and_5
    registry["37736:中医表型-中医四诊:易疲乏"] = is_between_1_and_5
    registry["37737:中医表型-中医四诊:活动量稍大就容易出虚汗"] = is_between_1_and_5
    registry["37738:中医表型-中医四诊:活动量稍大就容易出虚汗"] = is_between_1_and_5
    registry["37739:中医表型-中医四诊:活动量稍大就容易出虚汗"] = is_between_1_and_5
    registry["37740:中医表型-中医四诊:皮肤或口唇干燥"] = is_between_1_and_5
    registry["37741:中医表型-中医四诊:皮肤或口唇干燥"] = is_between_1_and_5
    registry["37742:中医表型-中医四诊:皮肤或口唇干燥"] = is_between_1_and_5
    registry["37743:中医表型-中医四诊:眼睛干涩"] = is_between_1_and_5
    registry["37744:中医表型-中医四诊:眼睛干涩"] = is_between_1_and_5
    registry["37745:中医表型-中医四诊:眼睛干涩"] = is_between_1_and_5
    registry["37746:中医表型-中医四诊:精力充沛"] = is_between_1_and_5
    registry["37747:中医表型-中医四诊:精力充沛"] = is_between_1_and_5
    registry["37748:中医表型-中医四诊:精神紧张"] = is_between_1_and_5
    registry["37749:中医表型-中医四诊:精神紧张"] = is_between_1_and_5
    registry["37750:中医表型-中医四诊:精神紧张"] = is_between_1_and_5
    registry["37751:中医表型-中医四诊:腹部肥满松软"] = is_between_1_and_5
    registry["37752:中医表型-中医四诊:身体不轻松或不爽快"] = is_between_1_and_5
    registry["37753:中医表型-中医四诊:闷闷不乐"] = is_between_1_and_5
    registry["37754:中医表型-中医四诊:闷闷不乐"] = is_between_1_and_5
    registry["37755:中医表型-中医四诊:Aa(收缩期面积)(左手)"] = _is_not_empty
    registry["37756:中医表型-中医四诊:As(收缩期总面积)(左手)"] = _is_not_empty
    registry["37757:中医表型-中医四诊:Ab(舒张期面积)(左手)"] = _is_not_empty
    registry["37758:中医表型-中医四诊:At(脉图总面积)(左手)"] = _is_not_empty
    registry["37759:中医表型-中医四诊:Ad(舒张期总面积)(左手)"] = _is_not_empty
    registry["37760:中医表型-中医四诊:W(主波上1/3处宽度)(左手)"] = _is_not_empty
    registry["37761:中医表型-中医四诊:W/t(主波上(1/3)处宽度/脉搏周期)(左手)"] = _is_not_empty
    registry["37762:中医表型-中医四诊:alpha(上升角)(左手)"] = _is_not_empty
    registry["37763:中医表型-中医四诊:h1/t1(主波幅度/升支时间)(左手)(mm/s)"] = _is_not_empty
    registry["37764:中医表型-中医四诊:h3(重搏前波幅度)(左手)(mm)"] = _is_not_empty
    registry["37765:中医表型-中医四诊:h3/h1(重搏前波幅度/主波幅度)(左手)"] = _is_not_empty
    registry["37766:中医表型-中医四诊:h4(降中峡幅度)(左手)(mm)"] = _is_not_empty
    registry["37767:中医表型-中医四诊:h4/h1(降中峡幅度/主波幅度)(左手)"] = _is_not_empty
    registry["37768:中医表型-中医四诊:h5(重搏波幅度)(左手)(mm)"] = _is_not_empty
    registry["37769:中医表型-中医四诊:h5/h1(重搏波幅度/主波幅度)(左手)"] = _is_not_empty
    registry["37770:中医表型-中医四诊:t(脉波周期)(左手)(s)"] = _is_not_empty
    registry["37771:中医表型-中医四诊:t1(脉波升支时间)(左手)(s)"] = _is_not_empty
    registry["37772:中医表型-中医四诊:t2(左手)"] = _is_not_empty
    registry["37773:中医表型-中医四诊:t4(心缩时间)(左手)(s)"] = _is_not_empty
    registry["37774:中医表型-中医四诊:t5(缓降时间)(左手)(s)"] = _is_not_empty
    registry["37775:中医表型-中医四诊:压力值(左手)"] = _is_not_empty
    registry["37776:中医表型-中医四诊:紧张度(左手)"] = _is_not_empty
    registry["37777:中医表型-中医四诊:紧张度(左手)"] = _is_not_empty
    registry["37778:中医表型-中医四诊:脉位(左手)"] = _is_not_empty
    registry["37779:中医表型-中医四诊:脉位(左手)"] = _is_not_empty
    registry["37780:中医表型-中医四诊:脉位(左手)"] = _is_not_empty
    registry["37781:中医表型-中医四诊:脉位(左手)"] = _is_not_empty
    registry["37782:中医表型-中医四诊:脉力(左手)"] = _is_not_empty
    registry["37783:中医表型-中医四诊:脉力(左手)"] = _is_not_empty
    registry["37784:中医表型-中医四诊:脉率(左手)(次/分)"] = _is_not_empty
    registry["37785:中医表型-中医四诊:脉象-滑涩度(左手)"] = _is_not_empty
    registry["37786:中医表型-中医四诊:theta(主波角)(左手)"] = _is_not_empty
    registry["37787:中医表型-中医四诊:脉象-脉名提示(左手)"] = _is_not_empty
    registry["37788:中医表型-中医四诊:脉象类型(左手)"] = _is_not_empty
    registry["37789:中医表型-中医四诊:脉象-脉名提示(左手)"] = _is_not_empty
    registry["37790:中医表型-中医四诊:脉象类型(左手)"] = _is_not_empty
    registry["37791:中医表型-中医四诊:虚实度(左手)"] = _is_not_empty
    registry["37792:中医表型-中医四诊:h1(主波波峰幅度)(左手)(mm)"] = _is_not_empty
    registry["37793:中医表型-中医四诊:局部特征-裂纹、齿痕、点刺、瘀斑"] = _is_not_empty
    registry["37794:中医表型-中医四诊:局部特征-裂纹、齿痕、点刺、瘀斑"] = _is_not_empty
    registry["37795:中医表型-中医四诊:局部特征-裂纹、齿痕、点刺、瘀斑"] = _is_not_empty
    registry["37796:中医表型-中医四诊:局部特征-裂纹、齿痕、点刺、瘀斑"] = _is_not_empty
    registry["37797:中医表型-中医四诊:舌形"] = _is_not_empty
    registry["37798:中医表型-中医四诊:舌形"] = _is_not_empty
    registry["37799:中医表型-中医四诊:舌形"] = _is_not_empty
    registry["37800:中医表型-中医四诊:舌形"] = _is_not_empty
    registry["37801:中医表型-中医四诊:带下色黄(女)"] = is_between_1_and_5
    registry["37802:中医表型-中医四诊:阴囊潮湿(男)"] = is_between_1_and_5


def _validate_EES_total_score(feature_key, final_value, payload) -> bool:
    """
    规则：Epworth嗜睡量表总分，取整数且在 0-24 之间。
    - 允许字符串数字或数值类型。
    - 其他情况判异常。
    """
    try:
        score = int(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= score <= 24

def is_between_0_and_21(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 0-21（含）之间，接受字符串数字或数值类型。
    用于匹兹堡睡眠质量指数总分验证。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= num <= 21

def is_between_1_and_5(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 1-5（含）之间，接受字符串数字或数值类型。
    用于中医四诊部分问题。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 1 <= num <= 5

def is_between_0_and_63(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 0-63（含）之间，接受字符串数字或数值类型。
    用于贝克抑郁量表指数总分验证。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= num <= 63

def is_between_0_and_3(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 0-3（含）之间，接受字符串数字或数值类型。
    贝克抑郁量表部分题目使用。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= num <= 3

def _is_not_empty(feature_key, final_value, payload) -> bool:
    """
    判断输入是否非空。
    - 适用于字符串类型，去除首尾空格后非空即通过。
    - 其他类型判异常。
    """
    if isinstance(final_value, str):
        return bool(final_value.strip())
    return False

def _validate_age(feature_key, final_value, payload) -> bool:
    """
    规则：年龄型数值，取整数且在 0-120 岁之间。
    - 允许字符串数字或数值类型。
    - 其他情况判异常。
    """
    try:
        age = int(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= age <= 120


def is_yes_no(feature_key, final_value, payload) -> bool:
    """
    判断输入是否为“是”或“否”，用于通用二分类问卷题。
    - 接受中文“是/否”（含去除首尾空格）
    - 宽松接受英文 yes/no（不区分大小写）
    """
    if isinstance(final_value, str):
        normalized = final_value.strip().lower()
        return normalized in {"是", "否", "yes", "no"}
    return False


def _validate_weekly_coffee_ml(feature_key, final_value, payload) -> bool:
    """
    规则：平均每周咖啡量（毫升），接受非负实数，设定上限 0-50000 ml 以滤除明显异常。
    - 允许字符串数字或数值类型。
    """
    try:
        vol = float(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= vol <= 50000


def is_between_1_and_9(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 1-9（含）之间，接受字符串数字或数值类型。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 1 <= num <= 9

def is_between_0_and_4(feature_key, final_value, payload) -> bool:
    """
    判断数值是否在 0-4（含）之间，接受字符串数字或数值类型。
    匹兹堡睡眠质量指数部分题目使用。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return 0 <= num <= 4

def is_natural_number(feature_key, final_value, payload) -> bool:
    """
    判断是否为自然数（0,1,2,...），接受字符串数字或数值类型。
    """
    try:
        num = int(final_value)
    except (TypeError, ValueError):
        return False
    return num >= 0


def _validate_lab_value(feature_key, final_value, payload) -> bool:
    """验证 Lab 颜色空间值：L ∈ [0,100]，a/b ∈ [-128,127]。"""
    if feature_key.endswith("_L"):
        lower, upper = 0.0, 100.0
    elif feature_key.endswith("_a") or feature_key.endswith("_b"):
        lower, upper = -128.0, 127.0
    else:
        return False

    try:
        value = float(final_value)
    except (TypeError, ValueError):
        return False

    return lower <= value <= upper
