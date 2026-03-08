from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "淬骨丹方",
    "一名散修手中有一张古方「淬骨丹」，称可固本培元、滋养根骨。他缺几味辅药，若你帮忙采集，炼成后分你一枚。",
    [
        _c("答应采药并等丹成", next_event={
            "desc": "你采齐辅药交给散修，三日后丹成，他分你一枚淬骨丹。",
            "choices": [
                _c("服下淬骨丹并静心炼化", condition=_cond("bone", 5), rewards={"bone": 1, "cultivation": 45}, flavor="丹力入骨，根骨与修为皆进。根骨 +1，修为 +45"),
                _c("服下淬骨丹并静心炼化", rewards={"cultivation": 30}, flavor="你略有所得。修为 +30"),
                _c("将丹留待日后服用", rewards={"bone": 1}, flavor="你收起淬骨丹，日后服用可固根骨。根骨 +1"),
            ]
        }),
        _c("不答应", rewards={}, flavor="你婉拒后离开。"),
    ]
))

EVENTS.append(_e(
    "石锁练力",
    "练武场边摆着数对石锁，从百斤到千斤不等。体修常在此举锁练力，可强体魄。",
    [
        _c("举石锁练力", next_event={
            "desc": "你选了一对石锁，反复举放。需坚持足够久，体魄方能有所进益。",
            "choices": [
                _c("练至力竭方休", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 35}, flavor="你练至力竭，体魄与修为皆进。体魄 +1，修为 +35"),
                _c("练至力竭方休", rewards={"cultivation": 25}, flavor="你略有所得。修为 +25"),
                _c("练片刻便停", rewards={"cultivation": 15}, flavor="你练了一会儿便收功。修为 +15"),
            ]
        }),
        _c("不练", rewards={}, flavor="你未举石锁，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵髓滴骨",
    "洞中石笋尖有灵髓滴落，据说滴在筋骨处可润泽根骨。但灵髓极慢，需静候多时。",
    [
        _c("静候灵髓滴落", next_event={
            "desc": "你候了半日，接到数滴灵髓，涂于关节与脊骨处。",
            "choices": [
                _c("静心引导灵髓入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 6}, flavor="灵髓润骨，根骨与寿元皆进。根骨 +1，寿元 +6"),
                _c("静心引导灵髓入骨", rewards={"lifespan": 4}, flavor="你略有所得。寿元 +4"),
                _c("未等够便离开", rewards={"cultivation": 20}, flavor="你只接到一两滴，略得滋润。修为 +20"),
            ]
        }),
        _c("不候", rewards={}, flavor="你未等候，径自离开。"),
    ]
))

EVENTS.append(_e(
    "攀崖锻体",
    "绝壁上有体修凿出的攀岩路径，不用灵力、只凭手脚与体魄攀爬，可锻体魄。",
    [
        _c("徒手攀崖", next_event={
            "desc": "你扣石缝、踏凸岩，一路向上。臂力与腰腹皆在发力。",
            "choices": [
                _c("攀至崖顶", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 40}, flavor="你攀至崖顶，体魄与修为皆进。体魄 +1，修为 +40"),
                _c("攀至崖顶", rewards={"cultivation": 28}, flavor="你勉强登顶，略有所得。修为 +28"),
                _c("半途力竭而下", rewards={"lifespan": -2}, flavor="你力竭滑落，受了轻伤。寿元 -2"),
            ]
        }),
        _c("不攀", rewards={}, flavor="你未攀崖，径自离开。"),
    ]
))

EVENTS.append(_e(
    "龙骨汤",
    "坊市酒楼有一道「龙骨汤」，以灵兽骨熬制，据说常饮可壮筋骨、养根骨。今日只剩一盅。",
    [
        _c("买下龙骨汤并饮尽", next_event={
            "desc": "你饮下龙骨汤，汤热入腹，暖流走遍筋骨。",
            "choices": [
                _c("静坐化开汤力", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 8}, flavor="汤力入骨，根骨与寿元皆进。根骨 +1，寿元 +8"),
                _c("静坐化开汤力", rewards={"lifespan": 5}, flavor="你略有所得。寿元 +5"),
                _c("饮完便走", rewards={"cultivation": 22}, flavor="汤力未完全化入骨，部分转为修为。修为 +22"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买汤，径自离开。"),
    ]
))

EVENTS.append(_e(
    "扛鼎过关",
    "城门口有人设擂：不用灵力扛起千斤铜鼎走十步，便可获一枚「壮骨丹」，专养根骨。",
    [
        _c("上前扛鼎", next_event={
            "desc": "你运足气力，将铜鼎扛上肩头。十步之遥，步步沉重。",
            "choices": [
                _c("扛鼎走满十步", condition=_cond("physique", 7), rewards={"physique": 1, "bone": 1}, flavor="你走满十步，获壮骨丹服下，体魄与根骨皆进。体魄 +1，根骨 +1"),
                _c("扛鼎走满十步", rewards={"bone": 1}, flavor="你勉强走满十步，服下壮骨丹，根骨略固。根骨 +1"),
                _c("未满十步便放下", rewards={"cultivation": 20}, flavor="你力有不逮，放下铜鼎，略得锻炼。修为 +20"),
            ]
        }),
        _c("不试", rewards={}, flavor="你未上前，径自离开。"),
    ]
))

EVENTS.append(_e(
    "地火蒸身",
    "地脉火口旁有体修以地火蒸汽蒸身，称可通经络、强体魄。但若体魄不足，易被灼伤。",
    [
        _c("入蒸汽中蒸身", next_event={
            "desc": "你置身地火蒸汽中，热浪裹身，汗如雨下。",
            "choices": [
                _c("坚持一炷香", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 38}, flavor="你撑过一炷香，体魄与修为皆进。体魄 +1，修为 +38"),
                _c("坚持一炷香", rewards={"cultivation": 25}, flavor="你勉强撑住，略有所得。修为 +25"),
                _c("很快退出", rewards={"lifespan": -2}, flavor="你耐不住热，提前退出，略损元气。寿元 -2"),
            ]
        }),
        _c("不蒸", rewards={}, flavor="你未入蒸汽，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵根草",
    "山崖缝中生有一株「灵根草」，据说服之可略微滋养灵根与根骨。但草根深扎石缝，需费力气才能采到。",
    [
        _c("费力采下灵根草", next_event={
            "desc": "你抠石挖土，终于将灵根草连根采出。服下草叶与根须，需静心炼化。",
            "choices": [
                _c("静心炼化草力", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 6}, flavor="草力润泽根骨，你根基略固。根骨 +1，寿元 +6"),
                _c("静心炼化草力", rewards={"lifespan": 4}, flavor="你略有所得。寿元 +4"),
                _c("嚼碎便咽", rewards={"cultivation": 28}, flavor="草力未完全入骨，部分化为修为。修为 +28"),
            ]
        }),
        _c("不采", rewards={}, flavor="你未采灵根草，径自离开。"),
    ]
))

EVENTS.append(_e(
    "撞钟炼体",
    "寺中有一口大钟，有体修以肩背撞钟，借反震之力炼体。据说可淬炼筋骨、强健体魄。",
    [
        _c("以肩背撞钟", next_event={
            "desc": "你运足气力撞向大钟，钟声轰鸣，反震之力透体而入。",
            "choices": [
                _c("连撞九次", condition=_cond("physique", 6), rewards={"physique": 1, "bone": 1}, flavor="你连撞九次，筋骨在反震中得以淬炼。体魄 +1，根骨 +1"),
                _c("连撞九次", rewards={"physique": 1}, flavor="你撑完全程，体魄略增。体魄 +1"),
                _c("撞三次便停", rewards={"cultivation": 22}, flavor="你撞了几次便收手，略有所得。修为 +22"),
            ]
        }),
        _c("不撞", rewards={}, flavor="你未撞钟，径自离开。"),
    ]
))

EVENTS.append(_e(
    "养骨丹",
    "一名丹师在路边摆摊，卖的是「养骨丹」，称可温和滋养根骨、不伤经脉。价格适中。",
    [
        _c("买一枚养骨丹服下", next_event={
            "desc": "你服下养骨丹，药力温和，缓缓渗入筋骨。",
            "choices": [
                _c("静心引导药力入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 5}, flavor="药力入骨，根骨与寿元皆进。根骨 +1，寿元 +5"),
                _c("静心引导药力入骨", rewards={"lifespan": 3}, flavor="你略有所得。寿元 +3"),
                _c("服下便赶路", rewards={"cultivation": 18}, flavor="药力未完全化入骨。修为 +18"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买丹，径自离开。"),
    ]
))

EVENTS.append(_e(
    "拉弓练臂",
    "练武场上有灵弓数把，弓弦需体魄方能拉满。有体修在此练拉弓，称可强臂力、固体魄。",
    [
        _c("拉弓练臂", next_event={
            "desc": "你取弓开弦，一次次拉满再松。臂膀与背脊皆在发力。",
            "choices": [
                _c("拉满百次", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 32}, flavor="你拉满百次，体魄与修为皆进。体魄 +1，修为 +32"),
                _c("拉满百次", rewards={"cultivation": 22}, flavor="你勉强完成，略有所得。修为 +22"),
                _c("拉三十次便停", rewards={"cultivation": 12}, flavor="你练了一会儿便收手。修为 +12"),
            ]
        }),
        _c("不练", rewards={}, flavor="你未拉弓，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵池泡骨",
    "山谷中有一池灵液，池底铺满灵矿碎屑。据说泡在其中可令灵液渗入筋骨、滋养根骨。",
    [
        _c("入灵池浸泡", next_event={
            "desc": "你浸入灵池，灵液没过肩颈，丝丝灵气钻入筋骨。",
            "choices": [
                _c("泡足一个时辰", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 7}, flavor="灵液润骨，根骨与寿元皆进。根骨 +1，寿元 +7"),
                _c("泡足一个时辰", rewards={"lifespan": 4}, flavor="你略有所得。寿元 +4"),
                _c("泡半时辰便出", rewards={"cultivation": 25}, flavor="你未泡够时辰，部分灵液化为修为。修为 +25"),
            ]
        }),
        _c("不泡", rewards={}, flavor="你未入池，径自离开。"),
    ]
))

EVENTS.append(_e(
    "挑担行路",
    "货栈招人挑灵货走山路，按担计酬。担子沉重，是体力活，也是练体的机会。",
    [
        _c("应招挑担", next_event={
            "desc": "你挑着担子走了数十里山路，肩背腿脚皆在承重。",
            "choices": [
                _c("挑满三趟", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 45}, flavor="你挑满三趟，体魄在劳作中有所进益，工钱也足。体魄 +1，灵石 +45"),
                _c("挑满三趟", rewards={"spirit_stones": 35}, flavor="你完成三趟，领到工钱。灵石 +35"),
                _c("挑一趟便歇", rewards={"spirit_stones": 15}, flavor="你挑了一趟便收工。灵石 +15"),
            ]
        }),
        _c("不挑", rewards={}, flavor="你未应招，径自离开。"),
    ]
))

EVENTS.append(_e(
    "虎骨酒",
    "猎户手中有一坛「虎骨酒」，以灵虎骨泡制，称可壮筋骨、养根骨。他愿以灵石换，或帮你做一件事抵价。",
    [
        _c("付灵石买酒并饮一盏", next_event={
            "desc": "你买下虎骨酒，饮了一盏。酒力与骨力一同化开，需引导入骨。",
            "choices": [
                _c("静心引导酒力入骨", condition=_cond("bone", 5), rewards={"bone": 1, "physique": 1}, flavor="酒力入骨，根骨与体魄皆进。根骨 +1，体魄 +1"),
                _c("静心引导酒力入骨", rewards={"bone": 1}, flavor="根骨得滋养。根骨 +1"),
                _c("饮完便歇", rewards={"cultivation": 25}, flavor="酒力未完全入骨，部分化为修为。修为 +25"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买酒，径自离开。"),
    ]
))

EVENTS.append(_e(
    "擂台上挨打",
    "城中擂台有体修设局：上台接他十拳不倒地，便赠一枚「固本丹」养根骨。不少人试过，多半撑不过五拳。",
    [
        _c("上台接拳", next_event={
            "desc": "你站定擂台，体修一拳接一拳轰在你身上。需以体魄硬抗。",
            "choices": [
                _c("接满十拳不倒地", condition=_cond("physique", 7), rewards={"physique": 1, "bone": 1}, flavor="你接满十拳，获固本丹服下，体魄与根骨皆进。体魄 +1，根骨 +1"),
                _c("接满十拳不倒地", rewards={"bone": 1}, flavor="你勉强撑住，服下固本丹，根骨略固。根骨 +1"),
                _c("接五拳便倒地", rewards={"lifespan": -3}, flavor="你被击倒在地，略受内伤。寿元 -3"),
            ]
        }),
        _c("不上台", rewards={}, flavor="你未上台，径自离开。"),
    ]
))

EVENTS.append(_e(
    "晨露润骨",
    "据说黎明前灵草上的晨露可润泽筋骨。有修士专程早起，以露水涂于关节与脊骨处，再吐纳片刻。",
    [
        _c("早起收集晨露并涂骨", next_event={
            "desc": "你收集了一小瓶晨露，涂于关节与脊骨，随后打坐吐纳。",
            "choices": [
                _c("静心吐纳化露入骨", condition=_cond("bone", 5), rewards={"bone": 1, "cultivation": 28}, flavor="晨露润骨，根骨与修为皆进。根骨 +1，修为 +28"),
                _c("静心吐纳化露入骨", rewards={"cultivation": 18}, flavor="你略有所得。修为 +18"),
                _c("涂完便走", rewards={"lifespan": 2}, flavor="露力未完全入骨，略得滋润。寿元 +2"),
            ]
        }),
        _c("不早起", rewards={}, flavor="你未早起收露，径自离开。"),
    ]
))

EVENTS.append(_e(
    "劈柴练劲",
    "柴房缺人劈灵木，灵木质硬，需气力与巧劲才能劈开。劈足一垛可领酬劳，也是练体的法子。",
    [
        _c("应招劈柴", next_event={
            "desc": "你举斧落斧，一根根灵木被劈开。臂力与腰劲皆在反复发力。",
            "choices": [
                _c("劈足一垛", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 38}, flavor="你劈足一垛，体魄在劳作中有所进益。体魄 +1，灵石 +38"),
                _c("劈足一垛", rewards={"spirit_stones": 28}, flavor="你完成一垛，领到工钱。灵石 +28"),
                _c("劈半垛便歇", rewards={"spirit_stones": 12}, flavor="你劈了半垛便收手。灵石 +12"),
            ]
        }),
        _c("不劈", rewards={}, flavor="你未应招，径自离开。"),
    ]
))

EVENTS.append(_e(
    "蛇胆吞服",
    "猎户刚取出一枚灵蛇胆，称生吞可清毒、亦可略养根骨。但蛇胆极苦，且需体魄方能化开胆力。",
    [
        _c("买下灵蛇胆并生吞", next_event={
            "desc": "你吞下蛇胆，苦味冲顶，随后一股热力自腹中散开。",
            "choices": [
                _c("以体魄化开胆力", condition=_cond("physique", 6), rewards={"bone": 1, "physique": 1}, flavor="胆力入骨，根骨与体魄皆进。根骨 +1，体魄 +1"),
                _c("以体魄化开胆力", rewards={"bone": 1}, flavor="根骨得滋养。根骨 +1"),
                _c("化不开，略损元气", rewards={"lifespan": -2}, flavor="你体魄不足，胆力未完全化开，略损元气。寿元 -2"),
            ]
        }),
        _c("不吞", rewards={}, flavor="你未吞蛇胆，径自离开。"),
    ]
))

EVENTS.append(_e(
    "冰火两重",
    "一处秘境中半边地火、半边寒泉。体修常在此先入火再入冰，以冷热交替淬炼体魄与筋骨。",
    [
        _c("先入火再入冰", next_event={
            "desc": "你先入地火边蒸身，再跃入寒泉浸体。一热一寒，筋骨如遭锤炼。",
            "choices": [
                _c("各坚持半炷香", condition=_cond("physique", 7), rewards={"physique": 1, "bone": 1, "cultivation": 35}, flavor="你撑过冰火交替，体魄与根骨皆进。体魄 +1，根骨 +1，修为 +35"),
                _c("各坚持半炷香", rewards={"physique": 1, "cultivation": 25}, flavor="你勉强撑住，体魄略增。体魄 +1，修为 +25"),
                _c("很快退出", rewards={"lifespan": -3}, flavor="你耐不住冷热交替，提前退出，略损元气。寿元 -3"),
            ]
        }),
        _c("不试", rewards={}, flavor="你未尝试，径自离开。"),
    ]
))

EVENTS.append(_e(
    "根骨试金石",
    "坊市中有「根骨试金石」，手按石上可测根骨强弱。若根骨达标，试金石会反哺一缕灵气润骨。",
    [
        _c("将手按在试金石上", next_event={
            "desc": "你按上试金石，石中传来一股吸力，似在探你根骨。",
            "choices": [
                _c("放松任其探测", condition=_cond("bone", 6), rewards={"bone": 1, "cultivation": 30}, flavor="试金石认可你的根骨，反哺灵气润骨。根骨 +1，修为 +30"),
                _c("放松任其探测", rewards={"cultivation": 20}, flavor="试金石略有反应，你略有所得。修为 +20"),
                _c("根骨不足，无反应", rewards={}, flavor="试金石无反应，你根骨未达标准。"),
            ]
        }),
        _c("不测", rewards={}, flavor="你未按试金石，径自离开。"),
    ]
))

EVENTS.append(_e(
    "背人过河",
    "河边有老者欲过河，河水湍急。他道：「若道友背我过河，我赠你一枚家传的养骨丹。」",
    [
        _c("背老者过河", next_event={
            "desc": "你背起老者，一步步涉水过河。水冲腿脚，需体魄与平衡方能站稳。",
            "choices": [
                _c("稳稳背过河", condition=_cond("physique", 6), rewards={"physique": 1, "bone": 1}, flavor="你稳稳过河，老者赠你养骨丹，服后体魄与根骨皆进。体魄 +1，根骨 +1"),
                _c("稳稳背过河", rewards={"bone": 1}, flavor="你背过河，老者赠你养骨丹，根骨略固。根骨 +1"),
                _c("中途险些跌倒", rewards={"lifespan": -1}, flavor="你险些滑倒，勉强过河，老者仍赠丹，但你略损元气。寿元 -1"),
            ]
        }),
        _c("不背", rewards={}, flavor="你婉拒，径自离开。"),
    ]
))

EVENTS.append(_e(
    "踏桩练步",
    "练武场上有梅花桩，体修常在上方练步法，不用灵力、只凭体魄与平衡。据说可强腿脚、固体魄。",
    [
        _c("上桩练步", next_event={
            "desc": "你在桩上行走跳跃，一步踏空便会落桩。腿力与腰腹皆在发力。",
            "choices": [
                _c("走满三圈不落桩", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 30}, flavor="你走满三圈，体魄与修为皆进。体魄 +1，修为 +30"),
                _c("走满三圈不落桩", rewards={"cultivation": 20}, flavor="你勉强完成，略有所得。修为 +20"),
                _c("中途落桩", rewards={"cultivation": 12}, flavor="你落桩数次，略得锻炼。修为 +12"),
            ]
        }),
        _c("不练", rewards={}, flavor="你未上桩，径自离开。"),
    ]
))

EVENTS.append(_e(
    "龟甲煅骨",
    "坊市有人卖「龟甲粉」，称以灵龟甲研磨而成，服之可煅骨强筋、略养根骨。",
    [
        _c("买龟甲粉并服下", next_event={
            "desc": "你以水送服龟甲粉，粉入腹中，一股沉坠之力往筋骨去。",
            "choices": [
                _c("静心引导药力入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 4}, flavor="药力入骨，根骨与寿元皆进。根骨 +1，寿元 +4"),
                _c("静心引导药力入骨", rewards={"lifespan": 3}, flavor="你略有所得。寿元 +3"),
                _c("服下便走", rewards={"cultivation": 18}, flavor="药力未完全入骨，部分化为修为。修为 +18"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买龟甲粉，径自离开。"),
    ]
))

EVENTS.append(_e(
    "推磨炼劲",
    "村中有一盘石磨，磨盘极重。有体修在此推磨练劲，称可强腰臂、固体魄。",
    [
        _c("推磨练劲", next_event={
            "desc": "你双手推磨，一圈又一圈。腰臂与腿脚皆在发力。",
            "choices": [
                _c("推满百圈", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 28}, flavor="你推满百圈，体魄与修为皆进。体魄 +1，修为 +28"),
                _c("推满百圈", rewards={"cultivation": 18}, flavor="你勉强完成，略有所得。修为 +18"),
                _c("推三十圈便停", rewards={"cultivation": 10}, flavor="你推了一会儿便收手。修为 +10"),
            ]
        }),
        _c("不推", rewards={}, flavor="你未推磨，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵兽骨髓",
    "猎户刚剖开一头灵兽，取出一截腿骨，称骨髓可食，食之可润泽根骨。他愿分你一碗。",
    [
        _c("饮下一碗灵兽骨髓", next_event={
            "desc": "你饮下骨髓，浓稠温热，入腹后暖流走遍筋骨。",
            "choices": [
                _c("静坐化开髓力入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 5}, flavor="髓力润骨，根骨与寿元皆进。根骨 +1，寿元 +5"),
                _c("静坐化开髓力入骨", rewards={"lifespan": 3}, flavor="你略有所得。寿元 +3"),
                _c("饮完便走", rewards={"cultivation": 22}, flavor="髓力未完全入骨，部分化为修为。修为 +22"),
            ]
        }),
        _c("不饮", rewards={}, flavor="你婉拒，径自离开。"),
    ]
))

EVENTS.append(_e(
    "倒立撑体",
    "体修在崖边倒立练功，称可强臂力、稳气血、固体魄。你若能倒立撑住一炷香，便算过关。",
    [
        _c("倒立撑体", next_event={
            "desc": "你双手撑地，倒立而起。臂力与核心皆在支撑。",
            "choices": [
                _c("撑满一炷香", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 32}, flavor="你撑满一炷香，体魄与修为皆进。体魄 +1，修为 +32"),
                _c("撑满一炷香", rewards={"cultivation": 22}, flavor="你勉强撑住，略有所得。修为 +22"),
                _c("半途落下", rewards={"cultivation": 12}, flavor="你撑了片刻便落下，略得锻炼。修为 +12"),
            ]
        }),
        _c("不练", rewards={}, flavor="你未倒立，径自离开。"),
    ]
))

EVENTS.append(_e(
    "地乳饮",
    "洞窟深处有石钟乳滴落「地乳」，据说饮之可养根骨、稳道基。但地乳量少，需静候。",
    [
        _c("静候地乳滴满一盅并饮下", next_event={
            "desc": "你候了许久，接满一盅地乳，仰头饮尽。",
            "choices": [
                _c("静心引导地乳入骨", condition=_cond("bone", 5), rewards={"bone": 1, "cultivation": 35}, flavor="地乳润骨，根骨与修为皆进。根骨 +1，修为 +35"),
                _c("静心引导地乳入骨", rewards={"cultivation": 22}, flavor="你略有所得。修为 +22"),
                _c("饮完便走", rewards={"lifespan": 3}, flavor="地乳未完全入骨，略得滋润。寿元 +3"),
            ]
        }),
        _c("不候", rewards={}, flavor="你未等候，径自离开。"),
    ]
))

EVENTS.append(_e(
    "抱石深蹲",
    "练武场上有大石球，体修常抱石深蹲，称可强腿力、固体魄。蹲满百次可领一枚壮体丹。",
    [
        _c("抱石深蹲", next_event={
            "desc": "你抱起石球，一次次深蹲再起。腿力与腰腹皆在发力。",
            "choices": [
                _c("蹲满百次", condition=_cond("physique", 6), rewards={"physique": 1, "bone": 1}, flavor="你蹲满百次，获壮体丹服下，体魄与根骨皆进。体魄 +1，根骨 +1"),
                _c("蹲满百次", rewards={"physique": 1}, flavor="你勉强完成，服下壮体丹，体魄略增。体魄 +1"),
                _c("蹲五十次便停", rewards={"cultivation": 18}, flavor="你蹲了五十次便收手，略有所得。修为 +18"),
            ]
        }),
        _c("不蹲", rewards={}, flavor="你未抱石，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵藤缠身",
    "山谷中有灵藤，据说以藤缠身再运功抵抗，可锻体魄、略养根骨。但藤会越缠越紧，需体魄方能撑住。",
    [
        _c("让灵藤缠身并运功抵抗", next_event={
            "desc": "灵藤缠上你的四肢与躯干，越缠越紧。你运功抵抗，筋骨承压。",
            "choices": [
                _c("撑至灵藤自行松开", condition=_cond("physique", 6), rewards={"physique": 1, "bone": 1}, flavor="你撑至灵藤松开，体魄与根骨皆在缠缚中有所进益。体魄 +1，根骨 +1"),
                _c("撑至灵藤自行松开", rewards={"physique": 1}, flavor="你勉强撑住，体魄略增。体魄 +1"),
                _c("半途呼救脱身", rewards={"lifespan": -2}, flavor="你撑不住，旁人助你脱身，略损元气。寿元 -2"),
            ]
        }),
        _c("不让藤缠", rewards={}, flavor="你未靠近灵藤，径自离开。"),
    ]
))

EVENTS.append(_e(
    "牛力丹",
    "丹师在卖「牛力丹」，称服之可暂增气力、久服可略固根骨。今日打折，限购一枚。",
    [
        _c("买一枚牛力丹服下", next_event={
            "desc": "你服下牛力丹，一股蛮力自腹中涌出，随后缓缓沉入筋骨。",
            "choices": [
                _c("趁药力未散时练体一番", condition=_cond("physique", 6), rewards={"physique": 1, "bone": 1}, flavor="你趁药力练体，体魄与根骨皆进。体魄 +1，根骨 +1"),
                _c("趁药力未散时练体一番", rewards={"bone": 1}, flavor="你略得锻炼，根骨得药力滋养。根骨 +1"),
                _c("静坐化开药力", rewards={"cultivation": 25}, flavor="药力未完全入骨，部分化为修为。修为 +25"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买丹，径自离开。"),
    ]
))

EVENTS.append(_e(
    "沙袋捶身",
    "体修以沙袋自捶胸背与四肢，称可活血锻骨、强体魄。你若愿试，他可教你捶法。",
    [
        _c("学捶法并自捶一炷香", next_event={
            "desc": "你按他所教，以沙袋捶打己身。初时疼痛，渐渐发热。",
            "choices": [
                _c("捶满一炷香", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 28}, flavor="你捶满一炷香，体魄与修为皆进。体魄 +1，修为 +28"),
                _c("捶满一炷香", rewards={"cultivation": 18}, flavor="你勉强完成，略有所得。修为 +18"),
                _c("捶半炷香便停", rewards={"cultivation": 10}, flavor="你捶了一会儿便收手。修为 +10"),
            ]
        }),
        _c("不学", rewards={}, flavor="你未学捶法，径自离开。"),
    ]
))

EVENTS.append(_e(
    "芝马嚼根",
    "药农在山中采到一株「芝马」，根须可嚼食，称可养根骨、延年。他愿分你一段根须。",
    [
        _c("收下根须并嚼食", next_event={
            "desc": "你嚼食芝马根须，味苦回甘，药力缓缓渗入筋骨。",
            "choices": [
                _c("静心引导药力入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 6}, flavor="药力润骨，根骨与寿元皆进。根骨 +1，寿元 +6"),
                _c("静心引导药力入骨", rewards={"lifespan": 4}, flavor="你略有所得。寿元 +4"),
                _c("嚼完便走", rewards={"cultivation": 20}, flavor="药力未完全入骨，部分化为修为。修为 +20"),
            ]
        }),
        _c("不收", rewards={}, flavor="你婉拒，径自离开。"),
    ]
))

EVENTS.append(_e(
    "拖石而行",
    "山路旁有体修拖巨石练功，称可强腿腰、固体魄。石上系绳，拖行百步可领赏。",
    [
        _c("拖石百步", next_event={
            "desc": "你将绳系于腰间，拖石而行。腿腰与全身皆在发力。",
            "choices": [
                _c("拖满百步", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 25}, flavor="你拖满百步，体魄在劳作中有所进益，领到赏钱。体魄 +1，灵石 +25"),
                _c("拖满百步", rewards={"spirit_stones": 18}, flavor="你勉强完成，领到赏钱。灵石 +18"),
                _c("拖五十步便停", rewards={"spirit_stones": 8}, flavor="你拖了五十步便收手。灵石 +8"),
            ]
        }),
        _c("不拖", rewards={}, flavor="你未拖石，径自离开。"),
    ]
))

EVENTS.append(_e(
    "骨符贴脊",
    "符师在卖「骨符」，称贴于脊背可引灵气润骨、略养根骨。贴足七日方见效。",
    [
        _c("买骨符并贴脊七日", next_event={
            "desc": "你将骨符贴于脊背，符力丝丝渗入脊椎与肋骨。",
            "choices": [
                _c("静心配合符力入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 4}, flavor="符力润骨，根骨与寿元皆进。根骨 +1，寿元 +4"),
                _c("静心配合符力入骨", rewards={"lifespan": 3}, flavor="你略有所得。寿元 +3"),
                _c("贴三日便揭", rewards={"cultivation": 15}, flavor="你未贴足七日，符力未完全入骨。修为 +15"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买骨符，径自离开。"),
    ]
))

EVENTS.append(_e(
    "伏地挺身",
    "练武场上体修在做伏地挺身，称可强臂胸、固体魄。若能一次做满两百，便赠一枚炼体丹。",
    [
        _c("伏地挺身", next_event={
            "desc": "你俯身撑地，一起一落。臂力与胸腹皆在发力。",
            "choices": [
                _c("做满两百", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 30}, flavor="你做满两百，服下炼体丹，体魄与修为皆进。体魄 +1，修为 +30"),
                _c("做满两百", rewards={"physique": 1}, flavor="你勉强完成，服下炼体丹，体魄略增。体魄 +1"),
                _c("做一百便停", rewards={"cultivation": 15}, flavor="你做了一百便收手，略有所得。修为 +15"),
            ]
        }),
        _c("不做", rewards={}, flavor="你未做伏地挺身，径自离开。"),
    ]
))

EVENTS.append(_e(
    "灵泉蒸骨",
    "温泉谷中有一眼灵泉，泉边蒸汽氤氲。据说在蒸汽中打坐，可令灵气渗入筋骨、滋养根骨。",
    [
        _c("在灵泉蒸汽中打坐", next_event={
            "desc": "你盘坐于灵泉蒸汽中，热气裹身，灵气丝丝入体。",
            "choices": [
                _c("打坐一个时辰并引导灵气入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 5}, flavor="灵气润骨，根骨与寿元皆进。根骨 +1，寿元 +5"),
                _c("打坐一个时辰并引导灵气入骨", rewards={"lifespan": 3}, flavor="你略有所得。寿元 +3"),
                _c("打坐半时辰便出", rewards={"cultivation": 20}, flavor="你未坐够时辰，部分灵气化为修为。修为 +20"),
            ]
        }),
        _c("不坐", rewards={}, flavor="你未在蒸汽中打坐，径自离开。"),
    ]
))

EVENTS.append(_e(
    "扛人跑山",
    "体修在招人「扛人跑山」：背一名同修跑山路十里，两人皆不用灵力。完成者可获一枚锻骨丹。",
    [
        _c("背人跑山十里", next_event={
            "desc": "你背起对方，沿山路奔跑。十里之遥，腿力与耐力皆在支撑。",
            "choices": [
                _c("跑完全程", condition=_cond("physique", 7), rewards={"physique": 1, "bone": 1}, flavor="你跑完全程，服下锻骨丹，体魄与根骨皆进。体魄 +1，根骨 +1"),
                _c("跑完全程", rewards={"bone": 1}, flavor="你勉强跑完，服下锻骨丹，根骨略固。根骨 +1"),
                _c("半途力竭", rewards={"lifespan": -2}, flavor="你力竭而止，略损元气。寿元 -2"),
            ]
        }),
        _c("不跑", rewards={}, flavor="你未应招，径自离开。"),
    ]
))

EVENTS.append(_e(
    "石肤膏",
    "坊市有人在卖「石肤膏」，称涂于肌肤后可略增体表韧性、久用可养根骨。一罐可用七日。",
    [
        _c("买石肤膏并连涂七日", next_event={
            "desc": "你每日涂膏于身，膏力渗入皮肉筋骨。七日下来，肌肤略韧。",
            "choices": [
                _c("涂满七日并配合练体", condition=_cond("physique", 6), rewards={"physique": 1, "bone": 1}, flavor="你涂满七日并略加练体，体魄与根骨皆进。体魄 +1，根骨 +1"),
                _c("涂满七日并配合练体", rewards={"bone": 1}, flavor="你涂满七日，根骨略得滋养。根骨 +1"),
                _c("涂三日便停", rewards={"cultivation": 15}, flavor="你未涂满七日，膏力未完全化入。修为 +15"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买石肤膏，径自离开。"),
    ]
))

EVENTS.append(_e(
    "憋气潜渊",
    "寒潭边有体修练「憋气潜渊」，不用灵力、只凭体魄潜入潭底，待足一炷香再上浮。完成者可强体魄。",
    [
        _c("憋气潜入潭底", next_event={
            "desc": "你深吸一口气，潜入潭底。水压裹身，需体魄与意志方能撑住。",
            "choices": [
                _c("在潭底待满一炷香", condition=_cond("physique", 7), rewards={"physique": 1, "cultivation": 35}, flavor="你在潭底撑满一炷香，体魄与修为皆进。体魄 +1，修为 +35"),
                _c("在潭底待满一炷香", rewards={"cultivation": 22}, flavor="你勉强撑住，略有所得。修为 +22"),
                _c("未满便上浮", rewards={"lifespan": -2}, flavor="你憋不住提前上浮，略损元气。寿元 -2"),
            ]
        }),
        _c("不潜", rewards={}, flavor="你未潜入潭底，径自离开。"),
    ]
))

EVENTS.append(_e(
    "龙骨煅身",
    "炼器坊在卖「龙骨粉」，称以灵龙骨研磨，可掺入药浴煅身养骨。若你自备药浴，他们可代你配一剂。",
    [
        _c("配一剂龙骨药浴并泡浴", next_event={
            "desc": "你按方配好药浴，浸身其中。龙骨粉化开，药力渗入筋骨。",
            "choices": [
                _c("泡足一个时辰并引导药力入骨", condition=_cond("bone", 5), rewards={"bone": 1, "physique": 1}, flavor="药力入骨，根骨与体魄皆进。根骨 +1，体魄 +1"),
                _c("泡足一个时辰并引导药力入骨", rewards={"bone": 1}, flavor="根骨得滋养。根骨 +1"),
                _c("泡半时辰便出", rewards={"cultivation": 25}, flavor="你未泡够，药力未完全入骨。修为 +25"),
            ]
        }),
        _c("不配", rewards={}, flavor="你未配药浴，径自离开。"),
    ]
))

EVENTS.append(_e(
    "擂鼓练心",
    "军营旁有人擂战鼓，鼓声震心。体修常在此听鼓练功，称可稳气血、强体魄。你若在鼓声中练体一炷香，或有所得。",
    [
        _c("在鼓声中练体一炷香", next_event={
            "desc": "鼓声隆隆，你按体修之法在鼓声中练体。气血随鼓点起伏。",
            "choices": [
                _c("练满一炷香", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 28}, flavor="你练满一炷香，体魄与修为皆进。体魄 +1，修为 +28"),
                _c("练满一炷香", rewards={"cultivation": 18}, flavor="你勉强完成，略有所得。修为 +18"),
                _c("练半炷香便停", rewards={"cultivation": 10}, flavor="你练了一会儿便收功。修为 +10"),
            ]
        }),
        _c("不练", rewards={}, flavor="你未在鼓声中练体，径自离开。"),
    ]
))

EVENTS.append(_e(
    "固本灵茶",
    "茶摊在卖「固本灵茶」，称常饮可固本培元、略养根骨。一壶可饮三日。",
    [
        _c("买一壶固本灵茶并连饮三日", next_event={
            "desc": "你每日饮一盏灵茶，茶力温和，缓缓渗入筋骨。",
            "choices": [
                _c("静心品茶并引导茶力入骨", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 4}, flavor="茶力润骨，根骨与寿元皆进。根骨 +1，寿元 +4"),
                _c("静心品茶并引导茶力入骨", rewards={"lifespan": 3}, flavor="你略有所得。寿元 +3"),
                _c("饮完便走", rewards={"cultivation": 18}, flavor="茶力未完全入骨，部分化为修为。修为 +18"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买灵茶，径自离开。"),
    ]
))
