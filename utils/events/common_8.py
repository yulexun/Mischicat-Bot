from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "灵泉淬体",
    "山涧深处有一眼灵泉，泉水温润含灵。据说常泡可润泽筋骨、稳固根骨，不少体修来此淬体。",
    [
        _c("入灵泉浸泡", next_event={
            "desc": "你浸入灵泉，灵气丝丝渗入筋骨。需静心引导，方能化入根骨。",
            "choices": [
                _c("静心引导灵气入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 8}, flavor="灵气润泽根骨，你根基略固。根骨 +1，寿元 +8"),
                _c("静心引导灵气入骨", rewards={"lifespan": 5}, flavor="你略有所得，寿元微增。寿元 +5"),
                _c("长时间浸泡", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 40}, flavor="你以体魄承受泉压，体魄与修为皆进。体魄 +1，修为 +40"),
                _c("长时间浸泡", rewards={"cultivation": 25}, flavor="你泡了片刻，修为略增。修为 +25"),
            ]
        }),
        _c("只取一壶泉水离开", rewards={"spirit_stones": 30}, flavor="你取了一壶灵泉，可自用或出售。灵石 +30"),
        _c("离开", rewards={}, flavor="你未入泉，径自离开。"),
    ]
))

EVENTS.append(_e(
    "药浴淬骨",
    "坊市中有修士兜售「淬骨药浴」方子与药包，称连泡七日可固本培元、滋养根骨。价格不菲。",
    [
        _c("购买药包并连泡七日", next_event={
            "desc": "你按方泡浴，药力渗入筋骨。需以体魄化开药力，否则易淤积。",
            "choices": [
                _c("以体魄化开药力", condition=_cond("physique", 6), rewards={"bone": 1, "physique": 1, "lifespan": 10}, flavor="药力尽数化入根骨与体魄。根骨 +1，体魄 +1，寿元 +10"),
                _c("以体魄化开药力", rewards={"bone": 1, "lifespan": 6}, flavor="根骨得滋养，略有进益。根骨 +1，寿元 +6"),
                _c("只泡三日便停", rewards={"lifespan": 4}, flavor="你未坚持到底，仅略得补益。寿元 +4"),
            ]
        }),
        _c("只买方子，自采药草", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "bone": 1}, flavor="你自配药浴，悟性在辨药中有得，泡后根骨略固。悟性 +1，根骨 +1"),
        _c("不买，离开", rewards={}, flavor="你觉得不值，未购。"),
    ]
))

EVENTS.append(_e(
    "石乳润骨",
    "洞窟深处有钟乳滴落灵液，当地人称「石乳」，饮之可润泽筋骨。但石乳量少，且洞中有毒瘴。",
    [
        _c("入洞取石乳", next_event={
            "desc": "你屏息入洞，取得一小瓶石乳。服下后需引导灵气入骨。",
            "choices": [
                _c("服下并引导入骨", condition=_cond("bone", 5), rewards={"bone": 1, "cultivation": 50}, flavor="石乳润骨，根骨与修为皆进。根骨 +1，修为 +50"),
                _c("服下并引导入骨", rewards={"cultivation": 35}, flavor="你略有所得。修为 +35"),
                _c("留一半售出", rewards={"spirit_stones": 45}, flavor="你自服一半，售出一半。灵石 +45"),
            ]
        }),
        _c("不敢入洞", rewards={}, flavor="你畏毒瘴，未入洞。"),
    ]
))

EVENTS.append(_e(
    "地脉锻骨",
    "某处地脉裸露，地气上涌。体修常在此以地气锻骨，据说可夯实根基，但过程痛苦。",
    [
        _c("借地气锻骨", next_event={
            "desc": "你引地气入体，筋骨如遭碾压。需咬牙坚持，方能化地气为根骨之基。",
            "choices": [
                _c("咬牙坚持到底", condition=_cond("physique", 7), rewards={"bone": 1, "physique": 1, "cultivation": 45}, flavor="地气淬炼根骨与体魄，你根基更稳。根骨 +1，体魄 +1，修为 +45"),
                _c("咬牙坚持到底", rewards={"bone": 1, "cultivation": 30}, flavor="你撑过锻骨，根骨略固。根骨 +1，修为 +30"),
                _c("半途而废", rewards={"lifespan": -3}, flavor="你承受不住，提前退出，略损元气。寿元 -3"),
            ]
        }),
        _c("只在一旁观摩", rewards={"cultivation": 20}, flavor="你观他人锻骨，略有所悟。修为 +20"),
        _c("离开", rewards={}, flavor="你未尝试，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵果洗髓",
    "一名药农手中有一枚「洗髓果」，称可洗去体内杂质、略固根骨，但需连服三枚才显效，他只有一枚。",
    [
        _c("买下洗髓果并服下", next_event={
            "desc": "你服下洗髓果，腹中温热，杂质随汗排出。一枚虽不足洗髓，却可略养根骨。",
            "choices": [
                _c("静心炼化果力", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 12}, flavor="果力润泽根骨，你根基略固。根骨 +1，寿元 +12"),
                _c("静心炼化果力", rewards={"lifespan": 8}, flavor="你略有所得。寿元 +8"),
                _c("边炼化边赶路", rewards={"cultivation": 30}, flavor="果力未完全化入根骨，部分转为修为。修为 +30"),
            ]
        }),
        _c("问清何处还有洗髓果", rewards={"spirit_stones": 15}, flavor="药农指了条路，你顺路采到几株灵草售出。灵石 +15"),
        _c("不买", rewards={}, flavor="你未购洗髓果。"),
    ]
))

EVENTS.append(_e(
    "古修遗泽",
    "荒洞中发现一具坐化的古修士遗骸，遗骸旁有一瓶未开封的「固本丹」，瓶上刻「滋根骨、稳道基」。",
    [
        _c("恭敬行礼后取丹", next_event={
            "desc": "你取丹服下，药力温和，专走筋骨。需静心引导，方能固本。",
            "choices": [
                _c("静心引导药力入骨", condition=_cond("bone", 6), rewards={"bone": 1, "cultivation": 60}, flavor="固本丹滋养根骨，你根基更稳。根骨 +1，修为 +60"),
                _c("静心引导药力入骨", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("将遗骸安葬，只取半瓶", condition=_cond("bone", 5), rewards={"bone": 1, "reputation": 15}, flavor="你安葬古修后服下半瓶，根骨得滋，路人称你有德。根骨 +1，声望 +15"),
            ]
        }),
        _c("只行礼不取丹", rewards={"reputation": 10}, flavor="你未动遗物，恭敬离开。声望 +10"),
        _c("取丹售出", rewards={"spirit_stones": 80}, flavor="你将固本丹售出，得一笔灵石。灵石 +80"),
    ]
))

EVENTS.append(_e(
    "灵兽陪练",
    "一名体修牵着一头灵猿，道：「此猿力道刚猛，可作陪练。挨它捶打可锻体固骨，但需体魄够硬。」",
    [
        _c("请灵猿陪练", next_event={
            "desc": "灵猿拳拳到肉，你以体魄硬抗。若能撑过一炷香，筋骨可得锤炼。",
            "choices": [
                _c("撑满一炷香", condition=_cond("physique", 7), rewards={"bone": 1, "physique": 1}, flavor="你撑完全程，根骨与体魄皆在捶打中有所进益。根骨 +1，体魄 +1"),
                _c("撑满一炷香", rewards={"physique": 1, "cultivation": 35}, flavor="你勉强撑住，体魄略增。体魄 +1，修为 +35"),
                _c("半途认输", rewards={"lifespan": -2}, flavor="你扛不住，提前退出，略损元气。寿元 -2"),
            ]
        }),
        _c("不练，离开", rewards={}, flavor="你婉拒陪练，径自离开。"),
    ]
))

EVENTS.append(_e(
    "负重登山",
    "山脚下有体修设的「负重阶」——背负重石登千级石阶，登顶者可获一枚「锻骨丹」，专养根骨。",
    [
        _c("负重登阶", next_event={
            "desc": "你背石登阶，步步沉重。千阶过半，筋骨已酸麻。",
            "choices": [
                _c("坚持登顶", condition=_cond("physique", 6), rewards={"bone": 1, "physique": 1, "cultivation": 40}, flavor="你登顶服下锻骨丹，根骨与体魄皆进。根骨 +1，体魄 +1，修为 +40"),
                _c("坚持登顶", rewards={"bone": 1}, flavor="你勉强登顶，服丹后根骨略固。根骨 +1"),
                _c("中途放弃", rewards={"cultivation": 25}, flavor="你半途卸石，略得锻炼。修为 +25"),
            ]
        }),
        _c("不登阶", rewards={}, flavor="你未参与，径自离开。"),
    ]
))

EVENTS.append(_e(
    "瀑布冲身",
    "崖边有一挂灵瀑，水势凶猛。体修常立于瀑下以水势冲身，可锻体魄，但需根基扎实。",
    [
        _c("入瀑下冲身", next_event={
            "desc": "瀑水砸身，你咬牙站稳。需以体魄硬抗，方能借水势锻体。",
            "choices": [
                _c("坚持一炷香", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 50}, flavor="你撑过瀑冲，体魄与修为皆进。体魄 +1，修为 +50"),
                _c("坚持一炷香", rewards={"cultivation": 35}, flavor="你勉强撑住，修为略增。修为 +35"),
                _c("片刻即退", rewards={"lifespan": -2}, flavor="水势太猛，你提前退出，略损元气。寿元 -2"),
            ]
        }),
        _c("只在瀑边打坐", rewards={"cultivation": 25}, flavor="你未入瀑，只在旁吸纳水灵。修为 +25"),
        _c("离开", rewards={}, flavor="你未锻体，径自离开。"),
    ]
))

EVENTS.append(_e(
    "寒潭炼体",
    "深山寒潭冰冷刺骨，据说在潭中炼体可淬炼体魄、凝练气血。但若体魄不足，易伤经脉。",
    [
        _c("入寒潭炼体", next_event={
            "desc": "你浸入寒潭，寒气透骨。需以体魄与意志坚持，方能淬体。",
            "choices": [
                _c("坚持至浑身发热再出", condition=_cond("physique", 7), rewards={"physique": 1, "cultivation": 55}, flavor="你熬过极寒，气血反涌，体魄与修为皆进。体魄 +1，修为 +55"),
                _c("坚持至浑身发热再出", rewards={"cultivation": 40}, flavor="你撑过一阵，略有所得。修为 +40"),
                _c("很快上岸", rewards={"lifespan": -3}, flavor="寒气侵体，你速速上岸，略损元气。寿元 -3"),
            ]
        }),
        _c("不入潭", rewards={}, flavor="你畏寒未入，径自离开。"),
    ]
))

EVENTS.append(_e(
    "武修切磋",
    "路边一名武修拦住你，道：「道友可敢与某切磋几招？不用法力，只拼体魄与招式。」",
    [
        _c("答应切磋", next_event={
            "desc": "你们拳脚相交，不用灵力，只凭体魄与身法。数十招后，对方收势抱拳。",
            "choices": [
                _c("全力应战", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 12}, flavor="你与武修战平，体魄在切磋中有所精进。体魄 +1，声望 +12"),
                _c("全力应战", rewards={"cultivation": 45}, flavor="你略逊一筹，但从对方招式中有所悟。修为 +45"),
                _c("只守不攻", rewards={"cultivation": 25}, flavor="你以守为主，略得锻炼。修为 +25"),
            ]
        }),
        _c("婉拒", rewards={}, flavor="你拱手辞谢，继续赶路。"),
    ]
))

EVENTS.append(_e(
    "搬运灵材",
    "坊市有人招短工搬运灵矿与灵木，称「扛得动就有赏，扛得多赏得多」。是体力活，也是练体的机会。",
    [
        _c("应招搬运", next_event={
            "desc": "你扛着灵材往返数趟，浑身汗透。工钱按量结算。",
            "choices": [
                _c("多扛几趟", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 55}, flavor="你咬牙多扛了几趟，体魄在劳作中有所锻炼，工钱也多。体魄 +1，灵石 +55"),
                _c("多扛几趟", rewards={"spirit_stones": 40}, flavor="你完成定额，领到工钱。灵石 +40"),
                _c("适可而止", rewards={"spirit_stones": 28}, flavor="你搬了几趟便收手。灵石 +28"),
            ]
        }),
        _c("不干", rewards={}, flavor="你未应招，径自离开。"),
    ]
))

EVENTS.append(_e(
    "观想古图",
    "破庙中挂着一幅残破古图，图上绘有星象与符文。据说凝神观想可锤炼神识，但极易耗神。",
    [
        _c("凝神观想古图", next_event={
            "desc": "你盘坐对图，以神识探入图中。图中似有无数线条牵引神识，需稳住心神。",
            "choices": [
                _c("稳住心神，细细观想", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 50}, flavor="你从观想中有所得，神识与修为皆进。神识 +1，修为 +50"),
                _c("稳住心神，细细观想", rewards={"cultivation": 30}, flavor="你略有所得。修为 +30"),
                _c("观想过久，头晕目眩", rewards={"lifespan": -2}, flavor="你耗神过度，速速收功，略损元气。寿元 -2"),
            ]
        }),
        _c("只略看一眼", rewards={"cultivation": 15}, flavor="你未深观，略有所感。修为 +15"),
        _c("离开", rewards={}, flavor="你对古图无兴趣，径自离开。"),
    ]
))

EVENTS.append(_e(
    "听钟悟神",
    "山寺每日晨钟暮鼓，钟声悠远。有修士言，若在钟响时以神识随钟声远荡，可炼神识。",
    [
        _c("在钟响时以神识随钟", next_event={
            "desc": "钟声一响，你放神识随声而去。声远神疲，需在极限处收回，方能不伤神。",
            "choices": [
                _c("在极限处稳稳收回", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 45}, flavor="你炼神有度，神识与修为皆进。神识 +1，修为 +45"),
                _c("在极限处稳稳收回", rewards={"cultivation": 28}, flavor="你略有所得。修为 +28"),
                _c("收得略晚", rewards={"lifespan": -2}, flavor="你神识略损，需静养几日。寿元 -2"),
            ]
        }),
        _c("只静听不炼神", rewards={"cultivation": 20}, flavor="你静听钟声，心绪稍宁。修为 +20"),
        _c("离开", rewards={}, flavor="你未留步听钟。"),
    ]
))

EVENTS.append(_e(
    "夜观星象",
    "旷野无云，星河璀璨。有修士言，以神识遥感星辰，可扩神识之域，但极耗心神。",
    [
        _c("以神识遥感星辰", next_event={
            "desc": "你放神识向天，触之愈远愈虚。需在神识将散未散时收回，方能炼神。",
            "choices": [
                _c("在将散未散时收回", condition=_cond("soul", 7), rewards={"soul": 1, "cultivation": 55}, flavor="你炼神有得，神识与修为皆进。神识 +1，修为 +55"),
                _c("在将散未散时收回", rewards={"cultivation": 32}, flavor="你略有所得。修为 +32"),
                _c("收得略迟", rewards={"lifespan": -3}, flavor="你神识略伤，需静养。寿元 -3"),
            ]
        }),
        _c("只仰观不炼神", rewards={"cultivation": 18}, flavor="你观星片刻，心有所感。修为 +18"),
        _c("离开", rewards={}, flavor="你未观星，径自离开。"),
    ]
))

EVENTS.append(_e(
    "残碑悟道",
    "荒地上半截残碑，碑文已模糊，只余几笔道纹。有修士在此参悟，称能悟出一丝便算机缘。",
    [
        _c("在碑前参悟", next_event={
            "desc": "你观碑上道纹，似与天地运转暗合。需以悟性揣摩，方能有所得。",
            "choices": [
                _c("静心揣摩道纹", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 50}, flavor="你从道纹中悟出一丝理，悟性与修为皆进。悟性 +1，修为 +50"),
                _c("静心揣摩道纹", rewards={"cultivation": 30}, flavor="你略有所得。修为 +30"),
                _c("参悟过久头昏", rewards={"lifespan": -1}, flavor="你强悟无果，略损精神。寿元 -1"),
            ]
        }),
        _c("不参悟，离开", rewards={}, flavor="你对残碑无感，径自离开。"),
    ]
))

EVENTS.append(_e(
    "论道茶会",
    "茶棚中有几名修士围坐论道，谈的是「修行重根基还是重机缘」。你若参与，可各抒己见。",
    [
        _c("参与论道", next_event={
            "desc": "你加入论道，有人重根骨体魄，有人重悟性神识。轮到你时，你需言之有物。",
            "choices": [
                _c("以自身感悟作答", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "reputation": 12}, flavor="你的见解得众人认可，悟性与声望皆进。悟性 +1，声望 +12"),
                _c("以自身感悟作答", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("多听少说", rewards={"cultivation": 25}, flavor="你听众人之言，略有所悟。修为 +25"),
            ]
        }),
        _c("不参与，只喝茶", rewards={"lifespan": 3}, flavor="你喝了一盏灵茶，略得休息。寿元 +3"),
        _c("离开", rewards={}, flavor="你未入座，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵田帮工",
    "灵农正在收灵谷，人手不足。你若帮忙半日，可得一些灵谷或灵石作为酬谢。",
    [
        _c("帮忙收灵谷", rewards={"spirit_stones": 35, "cultivation": 20}, flavor="你忙了半日，得灵谷与少许感悟。灵石 +35，修为 +20"),
        _c("不帮", rewards={}, flavor="你未帮忙，径自离开。"),
    ]
))

EVENTS.append(_e(
    "路遇讲法",
    "路边有老修士在给几名晚辈讲法，讲的是基础吐纳。你若驻足旁听，或有所得。",
    [
        _c("驻足旁听", rewards={"cultivation": 30}, flavor="你听了一程，基础更稳。修为 +30"),
        _c("不听，离开", rewards={}, flavor="你未驻足，继续赶路。"),
    ]
))

EVENTS.append(_e(
    "灵蝶引路",
    "一只灵蝶在你身前飞舞，似在引路。你跟去后发现一株灵草，灵蝶落在草上后散去。",
    [
        _c("采下灵草", rewards={"spirit_stones": 40}, flavor="你采下灵草，可自用或出售。灵石 +40"),
        _c("不采，只观片刻", rewards={"cultivation": 25}, flavor="你未采灵草，观其生机略有所悟。修为 +25"),
        _c("不跟", rewards={}, flavor="你未随灵蝶，径自离开。"),
    ]
))

EVENTS.append(_e(
    "野果充饥",
    "途中饥渴，你摘了几枚野果充饥。野果微含灵气，食后略解疲乏。",
    [
        _c("食野果后打坐片刻", rewards={"lifespan": 4, "cultivation": 15}, flavor="你食果后略作调息。寿元 +4，修为 +15"),
        _c("食完便走", rewards={"lifespan": 2}, flavor="你食果解渴。寿元 +2"),
    ]
))

EVENTS.append(_e(
    "古井打水",
    "村口有一口古井，井水清冽。村民说此井与地脉相通，常饮可强身。",
    [
        _c("打一壶井水并饮下", rewards={"lifespan": 5}, flavor="你饮了井水，神清气爽。寿元 +5"),
        _c("只打水带走", rewards={"cultivation": 10}, flavor="你带了一壶井水路上喝，略得滋润。修为 +10"),
        _c("不取", rewards={}, flavor="你未取井水。"),
    ]
))

EVENTS.append(_e(
    "灵雀送枝",
    "一只灵雀将一根灵枝丢在你脚边，枝上挂着几颗小灵果。灵雀叫了几声便飞走。",
    [
        _c("收下灵枝与灵果", rewards={"spirit_stones": 25, "lifespan": 3}, flavor="你收下灵果，食之略补，灵枝可售。灵石 +25，寿元 +3"),
        _c("将灵枝放在显眼处", rewards={"reputation": 8}, flavor="你未取灵枝，留给后来者，路人称你有德。声望 +8"),
        _c("不理会", rewards={}, flavor="你未动灵枝，径自离开。"),
    ]
))

EVENTS.append(_e(
    "石碑刻字",
    "山道旁有一块无字石碑，据说在此刻下感悟者可留一缕念力，后人观之或有所得。",
    [
        _c("刻下一句感悟", rewards={"cultivation": 28}, flavor="你刻字时心有所感，略有所得。修为 +28"),
        _c("只观他人刻字", rewards={"cultivation": 15}, flavor="你观碑上刻字，略有所悟。修为 +15"),
        _c("离开", rewards={}, flavor="你未刻字，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵蜂采蜜",
    "林中有灵蜂巢，蜂巢旁有修士在收蜜。他道：「若道友能引开蜂群片刻，我分你一罐灵蜜。」",
    [
        _c("帮忙引蜂", next_event={
            "desc": "你以灵力或身法引开蜂群，修士趁机取蜜。事后他兑现承诺。",
            "choices": [
                _c("收下灵蜜", rewards={"lifespan": 10, "spirit_stones": 20}, flavor="你得一罐灵蜜，食之可延年。寿元 +10，灵石 +20"),
                _c("婉拒，只取少许", rewards={"reputation": 12, "lifespan": 5}, flavor="你只取一小口，修士赞你不贪。声望 +12，寿元 +5"),
            ]
        }),
        _c("不帮", rewards={}, flavor="你畏蜂未帮，径自离开。"),
    ]
))

EVENTS.append(_e(
    "旧书摊",
    "坊市角落有旧书摊，摊上多是残破功法与杂记。翻翻或能淘到有用的一两页。",
    [
        _c("翻找旧书", rewards={"cultivation": 35}, flavor="你翻到一页残诀，略有所悟。修为 +35"),
        _c("买下一本杂记", rewards={"spirit_stones": -10, "cultivation": 40}, flavor="你花十灵石买了一本杂记，其中有一则修炼心得。灵石 -10，修为 +40"),
        _c("不翻，离开", rewards={}, flavor="你对旧书无兴趣，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵泉洗脸",
    "溪边有一眼小灵泉，过路修士常在此洗脸净手。据说可提神醒脑。",
    [
        _c("以灵泉洗脸", rewards={"lifespan": 3, "cultivation": 12}, flavor="你洗面后神清气爽。寿元 +3，修为 +12"),
        _c("只取一捧饮下", rewards={"lifespan": 2}, flavor="你饮了一捧灵泉。寿元 +2"),
        _c("离开", rewards={}, flavor="你未用灵泉。"),
    ]
))

EVENTS.append(_e(
    "护送药商",
    "一名药商欲过山路，怕遇劫匪，愿付灵石请人同行护送。",
    [
        _c("答应护送", next_event={
            "desc": "你与药商同行，一路平安。药商按约付酬，另赠几株灵草。",
            "choices": [
                _c("收下酬谢", rewards={"spirit_stones": 50, "reputation": 10}, flavor="你护送到位，得酬劳与名声。灵石 +50，声望 +10"),
                _c("只收一半", rewards={"spirit_stones": 25, "reputation": 18}, flavor="你只收半酬，药商感激。灵石 +25，声望 +18"),
            ]
        }),
        _c("不护送", rewards={}, flavor="你婉拒，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵火取暖",
    "寒夜中你生起一堆灵火取暖。灵火以灵木为柴，余烬中有一丝火灵之气。",
    [
        _c("在火边打坐至天明", rewards={"cultivation": 30}, flavor="你借余火调息，略有所得。修为 +30"),
        _c("只取暖不修炼", rewards={"lifespan": 2}, flavor="你暖了身子便歇息。寿元 +2"),
    ]
))

EVENTS.append(_e(
    "指点后辈",
    "一名炼气期晚辈向你请教吐纳之法。你若略加指点，他必感激。",
    [
        _c("略加指点", rewards={"reputation": 15, "cultivation": 20}, flavor="你指点几句，晚辈感激，你在讲解中亦有所悟。声望 +15，修为 +20"),
        _c("婉拒", rewards={}, flavor="你推说有事，未指点。"),
    ]
))

EVENTS.append(_e(
    "灵雨接水",
    "天降灵雨，有修士以器皿接雨。灵雨含灵气，接之可饮可售。",
    [
        _c("以器皿接灵雨", rewards={"lifespan": 6, "spirit_stones": 15}, flavor="你接到一壶灵雨，自饮半壶，半壶售出。寿元 +6，灵石 +15"),
        _c("只在灵雨中站片刻", rewards={"cultivation": 22}, flavor="你淋了片刻灵雨，略有所感。修为 +22"),
        _c("避雨不接", rewards={}, flavor="你寻处避雨，未接灵雨。"),
    ]
))

EVENTS.append(_e(
    "石洞避风",
    "你在石洞中避风，洞壁上有前人刻的简易吐纳图。虽粗陋，却可照着练几息。",
    [
        _c("按图练几息", rewards={"cultivation": 25}, flavor="你按图吐纳，略有所得。修为 +25"),
        _c("只休息不练", rewards={"lifespan": 2}, flavor="你歇息片刻。寿元 +2"),
    ]
))

EVENTS.append(_e(
    "灵兽赠毛",
    "一只温顺的灵兽凑近你，在你袖口蹭了蹭，掉下几根灵毛。灵毛可作符笔或炼器辅料。",
    [
        _c("收下灵毛", rewards={"spirit_stones": 30}, flavor="你收下灵毛，可自用或出售。灵石 +30"),
        _c("轻抚灵兽后离开", rewards={"reputation": 5}, flavor="你未取灵毛，只抚了抚灵兽。声望 +5"),
    ]
))

EVENTS.append(_e(
    "渡船闲谈",
    "渡船上与同船修士闲谈，对方说起某地灵气充沛，适合闭关。你记下地点。",
    [
        _c("记下并道谢", rewards={"cultivation": 20}, flavor="你记下地点，心中略有所悟。修为 +20"),
        _c("只当闲话", rewards={}, flavor="你未在意，当闲话听过。"),
    ]
))

EVENTS.append(_e(
    "灵菇炖汤",
    "你在林中采到几朵灵菇，炖汤食之可补气。",
    [
        _c("炖汤并服下", rewards={"lifespan": 8, "cultivation": 18}, flavor="你食了灵菇汤，略得补益。寿元 +8，修为 +18"),
        _c("留一半售出", rewards={"spirit_stones": 22, "lifespan": 4}, flavor="你自食一半，售出一半。灵石 +22，寿元 +4"),
    ]
))

EVENTS.append(_e(
    "修补山路",
    "山道有一处塌陷，路人难行。你若花些力气搬石填土，后人过路会轻松许多。",
    [
        _c("搬石填土", rewards={"reputation": 12, "cultivation": 15}, flavor="你修好山路，路人称谢。声望 +12，修为 +15"),
        _c("不修", rewards={}, flavor="你未动手，绕道而行。"),
    ]
))

EVENTS.append(_e(
    "灵灯一盏",
    "荒庙中有一盏未灭的灵灯，灯油将尽。你若添一点灵油，灯可再亮数日，庙中愿力或会庇佑过客。",
    [
        _c("添灵油", rewards={"lifespan": 5, "reputation": 8}, flavor="你添油后离开，心中略安。寿元 +5，声望 +8"),
        _c("不添，只借光歇息", rewards={"lifespan": 2}, flavor="你借光歇了一夜。寿元 +2"),
        _c("离开", rewards={}, flavor="你未动灵灯，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵叶书签",
    "你拾到一片灵叶，叶脉天然成纹，可作书签或符纸辅料。",
    [
        _c("收起灵叶", rewards={"spirit_stones": 18}, flavor="你收起灵叶，可自用或出售。灵石 +18"),
        _c("将灵叶夹入随身书册", rewards={"cultivation": 12}, flavor="你以灵叶为签，翻书时略有所感。修为 +12"),
    ]
))
