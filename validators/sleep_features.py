"""Validators for sleep features."""


def register(registry, prefix_registry):
    registry["4678:睡眠-睡眠问卷:Epworth嗜睡量表总分"] = _validate_EES_total_score
    registry["4679:睡眠-睡眠问卷:一天中的什么时间是您的“巅峰期”呢"] = _is_not_empty # 不确定分类规则
    registry["4680:睡眠-睡眠问卷:一天中的什么时间是您的“巅峰期”呢"] = _is_not_empty # 不确定分类规则
    registry["4681:睡眠-睡眠问卷:一天中的什么时间是您的“巅峰期”呢"] = _is_not_empty # 不确定分类规则
    registry["4682:睡眠-睡眠问卷:一般而言，您在清晨容易起床吗"] = _is_not_empty # 不确定分类规则
    registry["4683:睡眠-睡眠问卷:一般而言，您在清晨容易起床吗"] = _is_not_empty # 不确定分类规则
    registry["4684:睡眠-睡眠问卷:一般而言，您在清晨容易起床吗"] = _is_not_empty # 不确定分类规则
    registry["4685:睡眠-睡眠问卷:不能停止或不能控制的担心"] = _is_not_empty # 不确定分类规则
    registry["4686:睡眠-睡眠问卷:不能放松"] = _is_not_empty # 不确定分类规则
    registry["4687:睡眠-睡眠问卷:不能放松"] = _is_not_empty # 不确定分类规则
    registry["4688:睡眠-睡眠问卷:人可分为“清晨”型和“夜晚”型,您认为您自己属于哪一种类型"] = _is_not_empty # 不确定分类规则
    registry["4689:睡眠-睡眠问卷:人可分为“清晨”型和“夜晚”型,您认为您自己属于哪一种类型"] = _is_not_empty # 不确定分类规则
    registry["4690:睡眠-睡眠问卷:作为乘客在汽车中坐1小时，中间不休息"] = _is_not_empty # 不确定分类规则
    registry["4691:睡眠-睡眠问卷:作为乘客在汽车中坐1小时，中间不休息"] = _is_not_empty # 不确定分类规则
    registry["4692:睡眠-睡眠问卷:作为乘客在汽车中坐1小时，中间不休息"] = _is_not_empty # 不确定分类规则
    registry["4693:睡眠-睡眠问卷:作为乘客在汽车中坐1小时，中间不休息"] = _is_not_empty # 不确定分类规则
    registry["4694:睡眠-睡眠问卷:你的失眠问题影响了你的生活质量，你觉得在别人眼中你的失眠情况如何"] = _is_not_empty # 不确定分类规则
    registry["4695:睡眠-睡眠问卷:你的失眠问题影响了你的生活质量，你觉得在别人眼中你的失眠情况如何"] = _is_not_empty # 不确定分类规则
    registry["4696:睡眠-睡眠问卷:假设因为值夜班,您不得不在清晨4-6点保持清醒,而第二天您没有任何事要处理。以下哪种选择最适合您"] = _is_not_empty # 不确定分类规则
    registry["4697:睡眠-睡眠问卷:假设因为值夜班,您不得不在清晨4-6点保持清醒,而第二天您没有任何事要处理。以下哪种选择最适合您"] = _is_not_empty # 不确定分类规则
    registry["4698:睡眠-睡眠问卷:假设因为值夜班,您不得不在清晨4-6点保持清醒,而第二天您没有任何事要处理。以下哪种选择最适合您"] = _is_not_empty # 不确定分类规则
    # 
    registry["4699:睡眠-睡眠问卷:假设因为某些原因,您将比平时迟几个小时去睡觉,但又不需要在第二天清晨的任何特定时间起床,您最可能出现以下哪种情况"] = _is_not_empty # 不确定分类规则
    registry["4700:睡眠-睡眠问卷:假设因为某些原因,您将比平时迟几个小时去睡觉,但又不需要在第二天清晨的任何特定时间起床,您最可能出现以下哪种情况"] = _is_not_empty # 不确定分类规则
    registry["4701:睡眠-睡眠问卷:假设因为某些原因,您将比平时迟几个小时去睡觉,但又不需要在第二天清晨的任何特定时间起床,您最可能出现以下哪种情况"] = _is_not_empty # 不确定分类规则
    registry["4702:睡眠-睡眠问卷:假设您不得不进行两小时繁重的体力活动,如果您能完全自由地计划白天的时间,而且仅需考虑您自己的生活习惯,您会选择以下哪一个时间"] = _is_not_empty # 不确定分类规则
    registry["4703:睡眠-睡眠问卷:假设您不得不进行两小时繁重的体力活动,如果您能完全自由地计划白天的时间,而且仅需考虑您自己的生活习惯,您会选择以下哪一个时间"] = _is_not_empty # 不确定分类规则
    registry["4704:睡眠-睡眠问卷:假设您不得不进行两小时繁重的体力活动,如果您能完全自由地计划白天的时间,而且仅需考虑您自己的生活习惯,您会选择以下哪一个时间"] = _is_not_empty # 不确定分类规则
    registry["4705:睡眠-睡眠问卷:假设您决定开始剧烈的体育锻炼,一个朋友建议您应一周进行两次运动,每次一小时,而且夜晚10-11点是最佳时间。如果仅需考虑您自己的生活习惯,您认为您的表现会怎么样"] = _is_not_empty # 不确定分类规则
    registry["4706:睡眠-睡眠问卷:假设您决定开始剧烈的体育锻炼,一个朋友建议您应一周进行两次运动,每次一小时,而且夜晚10-11点是最佳时间。如果仅需考虑您自己的生活习惯,您认为您的表现会怎么样"] = _is_not_empty # 不确定分类规则
    registry["4707:睡眠-睡眠问卷:假设您决定开始剧烈的体育锻炼,一个朋友建议您应一周进行两次运动,每次一小时,而且夜晚10-11点是最佳时间。如果仅需考虑您自己的生活习惯,您认为您的表现会怎么样"] = _is_not_empty # 不确定分类规则
    registry["4708:睡眠-睡眠问卷:假设您决定开始剧烈的体育锻炼,一个朋友建议您应一周进行两次运动,每次一小时,而且夜晚10-11点是最佳时间。如果仅需考虑您自己的生活习惯,您认为您的表现会怎么样"] = _is_not_empty # 不确定分类规则
    registry["4709:睡眠-睡眠问卷:假设您决定要做些运动，而朋友建议您每星期两次,每次一小时,且时间定在早上7-8点。若依您个人作息情况，您觉得自己的表现会如何"] = _is_not_empty # 不确定分类规则
    registry["4710:睡眠-睡眠问卷:假设您决定要做些运动，而朋友建议您每星期两次,每次一小时,且时间定在早上7-8点。若依您个人作息情况，您觉得自己的表现会如何"] = _is_not_empty # 不确定分类规则
    registry["4711:睡眠-睡眠问卷:假设您决定要做些运动，而朋友建议您每星期两次,每次一小时,且时间定在早上7-8点。若依您个人作息情况，您觉得自己的表现会如何"] = _is_not_empty # 不确定分类规则
    registry["4712:睡眠-睡眠问卷:做恶梦"] = _is_not_empty # 不确定分类规则
    registry["4713:睡眠-睡眠问卷:做恶梦"] = _is_not_empty # 不确定分类规则
    registry["4714:睡眠-睡眠问卷:入睡困难(30分钟内不能入睡)"] = _is_not_empty # 不确定分类规则
    registry["4715:睡眠-睡眠问卷:入睡困难(30分钟内不能入睡)"] = _is_not_empty # 不确定分类规则
    registry["4716:睡眠-睡眠问卷:入睡困难(30分钟内不能入睡)"] = _is_not_empty # 不确定分类规则
    registry["4717:睡眠-睡眠问卷:入睡困难(30分钟内不能入睡)"] = _is_not_empty # 不确定分类规则
    registry["4718:睡眠-睡眠问卷:入睡困难"] = _is_not_empty # 不确定分类规则
    registry["4719:睡眠-睡眠问卷:入睡困难"] = _is_not_empty # 不确定分类规则
    registry["4720:睡眠-睡眠问卷:其它影响睡眠的事情"] = _is_not_empty # 不确定分类规则
    registry["4721:睡眠-睡眠问卷:出汗(不是因暑热冒汗)"] = _is_not_empty # 不确定分类规则
    registry["4722:睡眠-睡眠问卷:出汗(不是因暑热冒汗)"] = _is_not_empty # 不确定分类规则
    registry["4723:睡眠-睡眠问卷:匹兹堡睡眠质量指数催眠药物"] = is_between_0_and_4
    registry["4724:睡眠-睡眠问卷:匹兹堡睡眠质量指数入睡时间"] = _is_not_empty 
    registry["4725:睡眠-睡眠问卷:匹兹堡睡眠质量指数总分"] = is_between_0_and_21
    registry["4726:睡眠-睡眠问卷:匹兹堡睡眠质量指数总睡眠时间"] = is_natural_number
    registry["4727:睡眠-睡眠问卷:匹兹堡睡眠质量指数日间功能障碍"] = is_natural_number
    registry["4728:睡眠-睡眠问卷:匹兹堡睡眠质量指数睡眠效率"] = is_natural_number
    registry["4729:睡眠-睡眠问卷:匹兹堡睡眠质量指数睡眠质量"] = is_natural_number
    registry["4730:睡眠-睡眠问卷:匹兹堡睡眠质量指数睡眠障碍"] =is_natural_number
    registry["4731:睡眠-睡眠问卷:午餐不喝酒，餐后安静地坐着"] = _is_not_empty # 不确定分类规则
    registry["4732:睡眠-睡眠问卷:午餐不喝酒，餐后安静地坐着"] = _is_not_empty # 不确定分类规则
    registry["4733:睡眠-睡眠问卷:午餐不喝酒，餐后安静地坐着"] = _is_not_empty # 不确定分类规则
    registry["4734:睡眠-睡眠问卷:午餐不喝酒，餐后安静地坐着"] = _is_not_empty # 不确定分类规则
    registry["4735:睡眠-睡眠问卷:咳嗽或鼾声高"] = _is_not_empty # 不确定分类规则
    registry["4736:睡眠-睡眠问卷:在公共场所坐着不动"] = _is_not_empty # 不确定分类规则
    registry["4737:睡眠-睡眠问卷:在公共场所坐着不动"] = _is_not_empty # 不确定分类规则
    registry["4738:睡眠-睡眠问卷:在公共场所坐着不动"] = _is_not_empty # 不确定分类规则
    registry["4739:睡眠-睡眠问卷:在环境许可时，下午躺下休息"] = _is_not_empty # 不确定分类规则
    registry["4740:睡眠-睡眠问卷:在环境许可时，下午躺下休息"] = _is_not_empty # 不确定分类规则
    registry["4741:睡眠-睡眠问卷:在环境许可时，下午躺下休息"] = _is_not_empty # 不确定分类规则
    registry["4742:睡眠-睡眠问卷:坐下与人谈话"] = _is_not_empty # 不确定分类规则
    registry["4743:睡眠-睡眠问卷:坐下与人谈话"] = _is_not_empty # 不确定分类规则
    registry["4744:睡眠-睡眠问卷:坐着阅读书刊"] = _is_not_empty # 不确定分类规则
    registry["4745:睡眠-睡眠问卷:坐着阅读书刊"] = _is_not_empty # 不确定分类规则
    registry["4746:睡眠-睡眠问卷:坐着阅读书刊"] = _is_not_empty # 不确定分类规则
    registry["4747:睡眠-睡眠问卷:夜尿次数(次)"] = is_natural_number
    registry["4748:睡眠-睡眠问卷:夜间去厕所"] = _is_not_empty # 不确定分类规则
    registry["4749:睡眠-睡眠问卷:夜间去厕所"] = _is_not_empty # 不确定分类规则
    registry["4750:睡眠-睡眠问卷:夜间去厕所"] = _is_not_empty # 不确定分类规则
    registry["4751:睡眠-睡眠问卷:夜间去厕所"] = _is_not_empty # 不确定分类规则
    registry["4752:睡眠-睡眠问卷:夜间易醒或早醒"] = _is_not_empty # 不确定分类规则
    registry["4753:睡眠-睡眠问卷:夜间易醒或早醒"] = _is_not_empty # 不确定分类规则
    registry["4754:睡眠-睡眠问卷:夜间易醒或早醒"] = _is_not_empty # 不确定分类规则
    registry["4755:睡眠-睡眠问卷:夜间易醒或早醒"] = _is_not_empty # 不确定分类规则
    registry["4756:睡眠-睡眠问卷:大概晚上几点您因为想睡觉而感到疲惫"] = _is_not_empty # 不确定分类规则
    registry["4757:睡眠-睡眠问卷:大概晚上几点您因为想睡觉而感到疲惫"] = _is_not_empty # 不确定分类规则
    registry["4758:睡眠-睡眠问卷:大概晚上几点您因为想睡觉而感到疲惫"] = _is_not_empty # 不确定分类规则
    registry["4759:睡眠-睡眠问卷:失眠严重指数总分"] = is_natural_number
    registry["4760:睡眠-睡眠问卷:头晕"] = _is_not_empty # 不确定分类规则
    registry["4761:睡眠-睡眠问卷:头晕"] = _is_not_empty # 不确定分类规则
    registry["4762:睡眠-睡眠问卷:如果您不得不在清晨的某个时刻起床,您依赖闹钟的程度如何"] = _is_not_empty # 不确定分类规则
    registry["4763:睡眠-睡眠问卷:如果您不得不在清晨的某个时刻起床,您依赖闹钟的程度如何"] = _is_not_empty # 不确定分类规则
    registry["4764:睡眠-睡眠问卷:如果您不得不在清晨的某个时刻起床,您依赖闹钟的程度如何"] = _is_not_empty # 不确定分类规则
    registry["4765:睡眠-睡眠问卷:如果您在晚上11点去睡觉，身体感觉疲惫的程度是如何"] = _is_not_empty # 不确定分类规则
    registry["4766:睡眠-睡眠问卷:如果您在晚上11点去睡觉，身体感觉疲惫的程度是如何"] = _is_not_empty # 不确定分类规则
    registry["4767:睡眠-睡眠问卷:如果您在晚上11点去睡觉，身体感觉疲惫的程度是如何"] = _is_not_empty # 不确定分类规则
    registry["4768:睡眠-睡眠问卷:如果您能选择自己的工作时间,设想您每天工作5个小时(包括小休时间),这项工作是很有趣的,并会依据工作结果来付酬金,您会选择以下哪五个连续钟头呢"] = _is_not_empty # 不确定分类规则
    registry["4769:睡眠-睡眠问卷:如果您能选择自己的工作时间,设想您每天工作5个小时(包括小休时间),这项工作是很有趣的,并会依据工作结果来付酬金,您会选择以下哪五个连续钟头呢"] = _is_not_empty # 不确定分类规则
    registry["4770:睡眠-睡眠问卷:如果您能选择自己的工作时间,设想您每天工作5个小时(包括小休时间),这项工作是很有趣的,并会依据工作结果来付酬金,您会选择以下哪五个连续钟头呢"] = _is_not_empty # 不确定分类规则
    registry["4771:睡眠-睡眠问卷:如果第二天您没有任何计划或行程,那您上床睡觉的时间会比平时晚吗"] = _is_not_empty # 不确定分类规则
    registry["4772:睡眠-睡眠问卷:如果第二天您没有任何计划或行程,那您上床睡觉的时间会比平时晚吗"] = _is_not_empty # 不确定分类规则
    registry["4773:睡眠-睡眠问卷:如果第二天您没有任何计划或行程,那您上床睡觉的时间会比平时晚吗"] = _is_not_empty # 不确定分类规则
    registry["4774:睡眠-睡眠问卷:害怕什么可怕的事情发生"] = _is_not_empty # 不确定分类规则
    registry["4775:睡眠-睡眠问卷:害怕会发生"] = _is_not_empty # 不确定分类规则
    registry["4776:睡眠-睡眠问卷:害怕会发生"] = _is_not_empty # 不确定分类规则
    registry["4777:睡眠-睡眠问卷:害怕失控"] = _is_not_empty # 不确定分类规则
    registry["4778:睡眠-睡眠问卷:害怕失控"] = _is_not_empty # 不确定分类规则
    registry["4779:睡眠-睡眠问卷:对您目前的睡眠模式满意/不满意程度如何"] = _is_not_empty # 不确定分类规则
    registry["4780:睡眠-睡眠问卷:对您目前的睡眠模式满意/不满意程度如何"] = _is_not_empty # 不确定分类规则
    registry["4781:睡眠-睡眠问卷:对您目前的睡眠模式满意/不满意程度如何"] = _is_not_empty # 不确定分类规则
    registry["4782:睡眠-睡眠问卷:就您个人的经验，在假日中几点上床睡觉感觉最好"] = _is_not_empty # 不确定分类规则
    registry["4783:睡眠-睡眠问卷:就您个人的经验，在假日中几点上床睡觉感觉最好"] = _is_not_empty # 不确定分类规则
    registry["4784:睡眠-睡眠问卷:就您个人的经验，在假日中几点上床睡觉感觉最好"] = _is_not_empty # 不确定分类规则
    registry["4785:睡眠-睡眠问卷:就您个人的经验，在假日中几点起床感觉最好"] = _is_not_empty # 不确定分类规则
    registry["4786:睡眠-睡眠问卷:就您个人的经验，在假日中几点起床感觉最好"] = _is_not_empty # 不确定分类规则
    registry["4787:睡眠-睡眠问卷:就您个人的经验，在假日中几点起床感觉最好"] = _is_not_empty # 不确定分类规则
    registry["4788:睡眠-睡眠问卷:广泛性焦虑障碍量表总分"] = is_natural_number
    registry["4789:睡眠-睡眠问卷:当我感到疲劳时．我就什么事都不想做了"] = _is_not_empty # 不确定分类规则
    registry["4790:睡眠-睡眠问卷:很难放松"] = _is_not_empty # 不确定分类规则
    registry["4791:睡眠-睡眠问卷:心悸"] = _is_not_empty # 不确定分类规则
    registry["4792:睡眠-睡眠问卷:心悸"] = _is_not_empty # 不确定分类规则
    registry["4793:睡眠-睡眠问卷:心神不定"] = _is_not_empty # 不确定分类规则
    registry["4794:睡眠-睡眠问卷:心神不定"] = _is_not_empty # 不确定分类规则
    registry["4795:睡眠-睡眠问卷:恐慌"] = _is_not_empty # 不确定分类规则
    registry["4796:睡眠-睡眠问卷:恐慌"] = _is_not_empty # 不确定分类规则
    registry["4797:睡眠-睡眠问卷:您再次入睡是否困难"] = _is_not_empty # 不确定分类规则
    registry["4798:睡眠-睡眠问卷:您再次入睡是否困难"] = _is_not_empty # 不确定分类规则
    registry["4799:睡眠-睡眠问卷:您在睡眠过程中是否有醒转"] = _is_not_empty # 不确定分类规则
    registry["4800:睡眠-睡眠问卷:您在睡眠过程中是否有醒转"] = _is_not_empty # 不确定分类规则
    registry["4801:睡眠-睡眠问卷:您如何评价您今天早上的注意力情况"] = _is_not_empty # 不确定分类规则
    registry["4802:睡眠-睡眠问卷:您如何评价您今天早上的注意力情况"] = _is_not_empty # 不确定分类规则
    registry["4803:睡眠-睡眠问卷:您如何评价您今天早上的注意力情况"] = _is_not_empty # 不确定分类规则
    registry["4804:睡眠-睡眠问卷:您如何评价您今天早上的清醒程度"] = _is_not_empty # 不确定分类规则
    registry["4805:睡眠-睡眠问卷:您如何评价您今天早上的清醒程度"] = _is_not_empty # 不确定分类规则
    registry["4806:睡眠-睡眠问卷:您如何评价您今天早上的清醒程度"] = _is_not_empty # 不确定分类规则
    registry["4807:睡眠-睡眠问卷:您如何评价您昨晚的睡眠质量"] = _is_not_empty # 不确定分类规则
    registry["4808:睡眠-睡眠问卷:您如何评价您昨晚的睡眠质量"] = _is_not_empty # 不确定分类规则
    registry["4809:睡眠-睡眠问卷:您如何评价您昨晚的睡眠质量"] = _is_not_empty # 不确定分类规则
    registry["4810:睡眠-睡眠问卷:您对目前的睡眠问题的担心/痛苦程度如何"] = _is_not_empty # 不确定分类规则
    registry["4811:睡眠-睡眠问卷:您对目前的睡眠问题的担心/痛苦程度如何"] = _is_not_empty # 不确定分类规则
    registry["4812:睡眠-睡眠问卷:您累计醒转的时间是(分钟)(分钟)"] = _is_not_empty # 不确定分类规则
    registry["4813:睡眠-睡眠问卷:您累计醒转的时间是(小时)(小时)"] = _is_not_empty # 不确定分类规则
    registry["4814:睡眠-睡眠问卷:您觉得昨晚的睡眠时间是否足够"] = _is_not_empty # 不确定分类规则
    registry["4815:睡眠-睡眠问卷:您觉得昨晚的睡眠时间是否足够"] = _is_not_empty # 不确定分类规则
    registry["4816:睡眠-睡眠问卷:您认为您的失眠在多大程度上影响了你的日常功能"] = _is_not_empty # 不确定分类规则
    registry["4817:睡眠-睡眠问卷:您认为您的失眠在多大程度上影响了你的日常功能"] = _is_not_empty # 不确定分类规则
    registry["4818:睡眠-睡眠问卷:您认为您的失眠在多大程度上影响了你的日常功能"] = _is_not_empty # 不确定分类规则
    registry["4819:睡眠-睡眠问卷:您醒过几次(次)"] = _is_not_empty # 不确定分类规则
    registry["4820:睡眠-睡眠问卷:感到发热"] = _is_not_empty # 不确定分类规则
    registry["4821:睡眠-睡眠问卷:感到发热"] = _is_not_empty # 不确定分类规则
    registry["4822:睡眠-睡眠问卷:感到惊吓"] = _is_not_empty # 不确定分类规则
    registry["4823:睡眠-睡眠问卷:感到惊吓"] = _is_not_empty # 不确定分类规则
    registry["4824:睡眠-睡眠问卷:感觉冷"] = _is_not_empty # 不确定分类规则
    registry["4825:睡眠-睡眠问卷:感觉冷"] = _is_not_empty # 不确定分类规则
    registry["4826:睡眠-睡眠问卷:感觉热"] = _is_not_empty # 不确定分类规则
    registry["4827:睡眠-睡眠问卷:感觉热"] = _is_not_empty # 不确定分类规则
    registry["4828:睡眠-睡眠问卷:我很容易疲劳"] = _is_not_empty # 不确定分类规则
    registry["4829:睡眠-睡眠问卷:担心很多事情"] = _is_not_empty # 不确定分类规则
    registry["4830:睡眠-睡眠问卷:早醒"] = _is_not_empty # 不确定分类规则
    registry["4831:睡眠-睡眠问卷:早醒"] = _is_not_empty # 不确定分类规则
    registry["4832:睡眠-睡眠问卷:早醒"] = _is_not_empty # 不确定分类规则
    registry["4833:睡眠-睡眠问卷:易被激怒"] = _is_not_empty # 不确定分类规则
    registry["4835:睡眠-睡眠问卷:昨晚的睡眠质量能否代表平日"] = _is_not_empty # 不确定分类规则
    registry["4834:睡眠-睡眠问卷:昨晚的睡眠质量能否代表平日"] = _is_not_empty # 不确定分类规则
    registry["4836:睡眠-睡眠问卷:晨起床是否口渴"] = _is_not_empty # 不确定分类规则
    registry["4837:睡眠-睡眠问卷:晨起床是否口渴"] = _is_not_empty # 不确定分类规则
    registry["4838:睡眠-睡眠问卷:晨起床是否疲惫"] = _is_not_empty # 不确定分类规则
    registry["4839:睡眠-睡眠问卷:晨起床是否疲惫"] = _is_not_empty # 不确定分类规则
    registry["4840:睡眠-睡眠问卷:消化不良或腹部不适"] = _is_not_empty # 不确定分类规则
    registry["4841:睡眠-睡眠问卷:消化不良或腹部不适"] = _is_not_empty # 不确定分类规则
    registry["4842:睡眠-睡眠问卷:清晨型和夜晚型自评量表总分"] = is_natural_number
    registry["4843:睡眠-睡眠问卷:清晨起床后的半小时内,您觉得自己的清醒程度如何"] = _is_not_empty # 不确定分类规则
    registry["4844:睡眠-睡眠问卷:清晨起床后的半小时内,您觉得自己的清醒程度如何"] = _is_not_empty # 不确定分类规则
    registry["4845:睡眠-睡眠问卷:清晨起床后的半小时内,您觉得自己的清醒程度如何"] = _is_not_empty # 不确定分类规则
    registry["4846:睡眠-睡眠问卷:清晨起床后的半小时内,您觉得自己的精神如何"] = _is_not_empty # 不确定分类规则
    registry["4847:睡眠-睡眠问卷:清晨起床后的半小时内,您觉得自己的精神如何"] = _is_not_empty # 不确定分类规则
    registry["4848:睡眠-睡眠问卷:清晨起床后的半小时内,您觉得自己的食欲如何"] = _is_not_empty # 不确定分类规则
    registry["4849:睡眠-睡眠问卷:清晨起床后的半小时内,您觉得自己的食欲如何"] = _is_not_empty # 不确定分类规则
    registry["4850:睡眠-睡眠问卷:疲劳严重度量表总分"] = is_natural_number
    registry["4851:睡眠-睡眠问卷:疲劳使我不能保持体能"] = _is_not_empty # 不确定分类规则
    registry["4852:睡眠-睡眠问卷:疲劳带来频繁的不适"] = _is_not_empty # 不确定分类规则
    registry["4853:睡眠-睡眠问卷:疲劳影响了我的工作、家庭，社会活动"] = _is_not_empty # 不确定分类规则
    registry["4854:睡眠-睡眠问卷:疲劳影响我从事某些工作"] = _is_not_empty # 不确定分类规则
    registry["4855:睡眠-睡眠问卷:疲劳影响我的体能"] = _is_not_empty # 不确定分类规则
    registry["4856:睡眠-睡眠问卷:疲劳是最影响我活动能力的症状之一"] = _is_not_empty # 不确定分类规则
    registry["4857:睡眠-睡眠问卷:疲劳，坐不住"] = _is_not_empty # 不确定分类规则
    registry["4858:睡眠-睡眠问卷:疼痛不适"] = _is_not_empty # 不确定分类规则
    registry["4859:睡眠-睡眠问卷:看电视"] = _is_not_empty # 不确定分类规则
    registry["4860:睡眠-睡眠问卷:看电视"] = _is_not_empty # 不确定分类规则
    registry["4861:睡眠-睡眠问卷:看电视"] = _is_not_empty # 不确定分类规则
    registry["4862:睡眠-睡眠问卷:睡眠维持困难"] = _is_not_empty # 不确定分类规则
    registry["4863:睡眠-睡眠问卷:睡眠维持困难"] = _is_not_empty # 不确定分类规则
    registry["4864:睡眠-睡眠问卷:窒息感"] = _is_not_empty # 不确定分类规则
    registry["4865:睡眠-睡眠问卷:紧张"] = _is_not_empty # 不确定分类规则
    registry["4866:睡眠-睡眠问卷:紧张"] = _is_not_empty # 不确定分类规则
    registry["4867:睡眠-睡眠问卷:紧张、焦虑或愤怒"] = _is_not_empty # 不确定分类规则
    registry["4868:睡眠-睡眠问卷:脱落电极"] = _is_not_empty # 不确定分类规则
    registry["4869:睡眠-睡眠问卷:脸发红"] = _is_not_empty # 不确定分类规则
    registry["4870:睡眠-睡眠问卷:脸发红"] = _is_not_empty # 不确定分类规则
    registry["4871:睡眠-睡眠问卷:腿部颤动"] = _is_not_empty # 不确定分类规则
    registry["4872:睡眠-睡眠问卷:腿部颤动"] = _is_not_empty # 不确定分类规则
    registry["4873:睡眠-睡眠问卷:若您知道将接受长达两个小时且极耗脑力的考试，而希望能有很好的表现。若依您个人作息情况，您会选择哪一个测验时间"] = _is_not_empty # 不确定分类规则
    registry["4874:睡眠-睡眠问卷:若您知道将接受长达两个小时且极耗脑力的考试，而希望能有很好的表现。若依您个人作息情况，您会选择哪一个测验时间"] = _is_not_empty # 不确定分类规则
    registry["4875:睡眠-睡眠问卷:若您知道将接受长达两个小时且极耗脑力的考试，而希望能有很好的表现。若依您个人作息情况，您会选择哪一个测验时间"] = _is_not_empty # 不确定分类规则
    registry["4876:睡眠-睡眠问卷:若您知道将接受长达两个小时且极耗脑力的考试，而希望能有很好的表现。若依您个人作息情况，您会选择哪一个测验时间"] = _is_not_empty # 不确定分类规则
    registry["4877:睡眠-睡眠问卷:贝克抑郁量表总分"] = is_between_0_and_3
    registry["4878:睡眠-睡眠问卷:贝克抑郁量表问题10"] = is_between_0_and_3
    registry["4879:睡眠-睡眠问卷:贝克抑郁量表问题11"] = is_between_0_and_3
    registry["4880:睡眠-睡眠问卷:贝克抑郁量表问题11"] = is_between_0_and_3
    registry["4881:睡眠-睡眠问卷:贝克抑郁量表问题12"] = is_between_0_and_3
    registry["4882:睡眠-睡眠问卷:贝克抑郁量表问题12"] = is_between_0_and_3
    registry["4883:睡眠-睡眠问卷:贝克抑郁量表问题13"] = is_between_0_and_3
    registry["4884:睡眠-睡眠问卷:贝克抑郁量表问题13"] = is_between_0_and_3
    registry["4885:睡眠-睡眠问卷:贝克抑郁量表问题14"] = is_between_0_and_3
    registry["4886:睡眠-睡眠问卷:贝克抑郁量表问题14"] = is_between_0_and_3
    registry["4887:睡眠-睡眠问卷:贝克抑郁量表问题14"] = is_between_0_and_3
    registry["4888:睡眠-睡眠问卷:贝克抑郁量表问题15"] = is_between_0_and_3
    registry["4889:睡眠-睡眠问卷:贝克抑郁量表问题15"] = is_between_0_and_3
    registry["4890:睡眠-睡眠问卷:贝克抑郁量表问题15"] = is_between_0_and_3
    registry["4891:睡眠-睡眠问卷:贝克抑郁量表问题16"] = is_between_0_and_3
    registry["4892:睡眠-睡眠问卷:贝克抑郁量表问题16"] = is_between_0_and_3
    registry["4893:睡眠-睡眠问卷:贝克抑郁量表问题17"] = is_between_0_and_3
    registry["4894:睡眠-睡眠问卷:贝克抑郁量表问题17"] = is_between_0_and_3
    registry["4895:睡眠-睡眠问卷:贝克抑郁量表问题18"] = is_between_0_and_3
    registry["4896:睡眠-睡眠问卷:贝克抑郁量表问题18"] = is_between_0_and_3
    registry["4897:睡眠-睡眠问卷:贝克抑郁量表问题1"] = is_between_0_and_3
    registry["4898:睡眠-睡眠问卷:贝克抑郁量表问题1"] = is_between_0_and_3
    registry["4899:睡眠-睡眠问卷:贝克抑郁量表问题20"] = is_between_0_and_3
    registry["4900:睡眠-睡眠问卷:贝克抑郁量表问题20"] = is_between_0_and_3
    registry["4901:睡眠-睡眠问卷:贝克抑郁量表问题21"] = is_between_0_and_3
    registry["4902:睡眠-睡眠问卷:贝克抑郁量表问题21"] = is_between_0_and_3
    registry["4903:睡眠-睡眠问卷:贝克抑郁量表问题2"] = is_between_0_and_3
    registry["4904:睡眠-睡眠问卷:贝克抑郁量表问题2"] = is_between_0_and_3
    registry["4905:睡眠-睡眠问卷:贝克抑郁量表问题3"] = is_between_0_and_3
    registry["4906:睡眠-睡眠问卷:贝克抑郁量表问题3"] = is_between_0_and_3
    registry["4907:睡眠-睡眠问卷:贝克抑郁量表问题3"] = is_between_0_and_3
    registry["4908:睡眠-睡眠问卷:贝克抑郁量表问题4"] = is_between_0_and_3
    registry["4909:睡眠-睡眠问卷:贝克抑郁量表问题4"] = is_between_0_and_3
    registry["4910:睡眠-睡眠问卷:贝克抑郁量表问题4"] = is_between_0_and_3
    registry["4911:睡眠-睡眠问卷:贝克抑郁量表问题5"] = is_between_0_and_3
    registry["4912:睡眠-睡眠问卷:贝克抑郁量表问题5"] = is_between_0_and_3
    registry["4913:睡眠-睡眠问卷:贝克抑郁量表问题6"] = is_between_0_and_3
    registry["4914:睡眠-睡眠问卷:贝克抑郁量表问题6"] = is_between_0_and_3
    registry["4915:睡眠-睡眠问卷:贝克抑郁量表问题7"] = is_between_0_and_3
    registry["4916:睡眠-睡眠问卷:贝克抑郁量表问题7"] = is_between_0_and_3
    registry["4917:睡眠-睡眠问卷:贝克抑郁量表问题8"] = is_between_0_and_3
    registry["4918:睡眠-睡眠问卷:贝克抑郁量表问题8"] = is_between_0_and_3
    registry["4919:睡眠-睡眠问卷:贝克抑郁量表问题9"] = is_between_0_and_3
    registry["4920:睡眠-睡眠问卷:贝克焦虑量表总分"] = is_between_0_and_63
    registry["4921:睡眠-睡眠问卷:近1个月，从上床到入睡通常需要多少分钟(分钟)"] = is_natural_number
    registry["4922:睡眠-睡眠问卷:近1个月，总的来说，您认为自己的睡眠质量"] = _is_not_empty # 不确定分类规则
    registry["4923:睡眠-睡眠问卷:近1个月，总的来说，您认为自己的睡眠质量"] = _is_not_empty # 不确定分类规则
    registry["4924:睡眠-睡眠问卷:近1个月，总的来说，您认为自己的睡眠质量"] = _is_not_empty # 不确定分类规则
    registry["4925:睡眠-睡眠问卷:近1个月，您做事情的精力不足吗"] = _is_not_empty # 不确定分类规则
    registry["4926:睡眠-睡眠问卷:近1个月，您做事情的精力不足吗"] = _is_not_empty # 不确定分类规则
    registry["4927:睡眠-睡眠问卷:近1个月，您做事情的精力不足吗"] = _is_not_empty # 不确定分类规则
    registry["4928:睡眠-睡眠问卷:近1个月，您常感到困倦吗"] = _is_not_empty # 不确定分类规则
    registry["4929:睡眠-睡眠问卷:近1个月，您常感到困倦吗"] = _is_not_empty # 不确定分类规则
    registry["4930:睡眠-睡眠问卷:近1个月，您常感到困倦吗"] = _is_not_empty # 不确定分类规则
    registry["4931:睡眠-睡眠问卷:近1个月，您常感到困倦吗"] = _is_not_empty # 不确定分类规则
    registry["4932:睡眠-睡眠问卷:近1个月，晚上上床睡觉通常几点钟"] = _is_not_empty # 不确定分类规则
    registry["4933:睡眠-睡眠问卷:近1个月，晚上上床睡觉通常几点钟"] = _is_not_empty # 不确定分类规则
    registry["4934:睡眠-睡眠问卷:近1个月，晚上上床睡觉通常几点钟"] = _is_not_empty # 不确定分类规则
    registry["4935:睡眠-睡眠问卷:近1个月，每夜通常实际睡眠多少小时"] = is_natural_number
    registry["4936:睡眠-睡眠问卷:近1个月，通常早上起床时间"] = _is_not_empty # 不确定分类规则
    registry["4937:睡眠-睡眠问卷:近1个月，通常早上起床时间"] = _is_not_empty # 不确定分类规则
    registry["4938:睡眠-睡眠问卷:近1个月，通常早上起床时间"] = _is_not_empty # 不确定分类规则
    registry["4939:睡眠-睡眠问卷:近1个月，通常早上起床时间"] = _is_not_empty # 不确定分类规则
    registry["4940:睡眠-睡眠问卷:遇堵车时停车数分钟"] = is_natural_number
    registry["4941:睡眠-睡眠问卷:遇堵车时停车数分钟"] = is_natural_number
    registry["4942:睡眠-睡眠问卷:锻炼让我感到疲劳"] = _is_not_empty # 不确定分类规则
    registry["4943:睡眠-睡眠问卷:麻木或刺痛"] = _is_not_empty # 不确定分类规则
    registry["4944:睡眠-睡眠问卷:麻木或刺痛"] = _is_not_empty # 不确定分类规则
    registry["4697:睡眠-睡眠问卷:假设因为值夜班,您不得不在清晨4-6点保持清醒,而第二天您没有任何事要处理。以下哪种选择最适合您"] = _is_not_empty # 不确定分类规则
    # 仅对可能有子字段/补充后缀的题号添加前缀规则，其余保持精确匹配。
    '''
    prefix_registry.append(
        ("3796:健康问卷调查-问卷-1:从多少岁起", _validate_age)
    )
    '''

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
