from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "灵泉淬体",
    "你在山谷深处发现一处温热的灵泉，泉水泛着淡淡金光，似乎蕴含某种力量。",
    [
        _c("脱衣入泉，以灵泉淬炼肉身", condition=_cond("physique", 5), rewards={"physique": 1, "lifespan": -2}, flavor="灵泉之力渗入骨肉，你感到全身筋骨都在重塑。体魄 +1，寿元 -2"),
        _c("脱衣入泉，以灵泉淬炼肉身", rewards={"lifespan": -5}, flavor="灵泉之力过于猛烈，你勉强承受，伤了根基。寿元 -5"),
        _c("取泉水装入玉瓶，日后再用", rewards={"spirit_stones": 30}, flavor="灵泉水离开泉眼后灵气渐散，但仍可卖个好价。灵石 +30"),
        _c("在泉边打坐，吸收溢出的灵气", rewards={"cultivation": 50}, flavor="灵泉溢出的灵气温和纯净，修炼效果不错。修为 +50"),
    ]
))

EVENTS.append(_e(
    "铁臂猿挑衅",
    "一只铁臂猿拦住去路，捶胸怒吼，似乎在宣示领地。它的双臂粗壮如铁柱。",
    [
        _c("与它正面搏斗", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 40}, flavor="你以力破力，击退铁臂猿，在搏斗中体魄得到锤炼。体魄 +1，灵石 +40"),
        _c("与它正面搏斗", rewards={"lifespan": -6}, flavor="铁臂猿力大无穷，你被一掌拍飞，狼狈逃走。寿元 -6"),
        _c("模仿它的动作，以示友好", condition=_cond("comprehension", 6), rewards={"bone": 1}, flavor="铁臂猿见你模仿它的姿态，竟安静下来。你从它的动作中悟出一丝炼体之法。根骨 +1"),
        _c("模仿它的动作，以示友好", rewards={}, flavor="铁臂猿困惑地看着你，随后转身离去。"),
        _c("绕道而行", rewards={}, flavor="你绕了一大圈，避开了它的领地。"),
    ]
))

EVENTS.append(_e(
    "古修士石刻",
    "崖壁上刻着一套古老的炼体图谱，线条简练却蕴含深意，旁边刻着几行小字已模糊不清。",
    [
        _c("仔细研读图谱，尝试修炼", condition=_cond("comprehension", 6), rewards={"bone": 1, "cultivation": 30}, flavor="你参悟图谱中的炼体之法，根骨得到强化。根骨 +1，修为 +30"),
        _c("仔细研读图谱，尝试修炼", rewards={"cultivation": 20}, flavor="图谱晦涩难懂，你只领悟了皮毛。修为 +20"),
        _c("拓印图谱带走", rewards={"spirit_stones": 50}, flavor="你将图谱拓印下来，日后或可卖给有缘人。灵石 +50"),
        _c("按图谱姿势运功", condition=_cond("bone", 5), rewards={"physique": 1}, flavor="你按图运功，一股热流贯通全身经脉，肉身得到淬炼。体魄 +1"),
        _c("按图谱姿势运功", rewards={"lifespan": -3}, flavor="运功不当，经脉受损。寿元 -3"),
    ]
))

EVENTS.append(_e(
    "雷雨炼体",
    "天空突然乌云密布，雷电交加。你感到空气中弥漫着一股狂暴的灵气。",
    [
        _c("在雷雨中运功，以雷电淬体", condition=_cond("physique", 8), rewards={"bone": 1, "physique": 1}, flavor="雷电劈在身上，你咬牙承受，筋骨在雷霆中得到重塑。根骨 +1，体魄 +1"),
        _c("在雷雨中运功，以雷电淬体", rewards={"lifespan": -10}, flavor="雷电之力远超你的承受极限，你被劈得外焦里嫩。寿元 -10"),
        _c("寻找避雨之处", rewards={"spirit_stones": 20}, flavor="你在山洞中避雨，意外发现几块灵石。灵石 +20"),
        _c("盘坐感悟雷霆之道", condition=_cond("comprehension", 7), rewards={"soul": 1}, flavor="你在雷鸣中感悟天地之威，神识得到拓展。神识 +1"),
        _c("盘坐感悟雷霆之道", rewards={"cultivation": 30}, flavor="虽未大悟，但修为略有精进。修为 +30"),
    ]
))

EVENTS.append(_e(
    "瀑布冲击",
    "一道百丈飞瀑从悬崖倾泻而下，水势惊人，瀑布下方的岩石被冲出一个深潭。",
    [
        _c("站在瀑布下方，以水流锤炼肉身", condition=_cond("physique", 6), rewards={"physique": 1}, flavor="瀑布的冲击如千锤百炼，你的肉身在水流中变得更加坚韧。体魄 +1"),
        _c("站在瀑布下方，以水流锤炼肉身", rewards={"lifespan": -4}, flavor="水势太猛，你被冲入深潭，呛了好几口水。寿元 -4"),
        _c("在潭边打坐修炼", rewards={"cultivation": 40}, flavor="瀑布溅起的水雾中灵气充沛，修炼效果不错。修为 +40"),
    ]
))

EVENTS.append(_e(
    "地底矿脉",
    "你脚下的地面突然塌陷，跌入一处地下空间，四周岩壁上嵌着发光的矿石。",
    [
        _c("徒手挖掘矿石", condition=_cond("physique", 6), rewards={"bone": 1, "spirit_stones": 60}, flavor="你用拳头砸开岩壁，在反复的冲击中拳骨变得更加坚硬。根骨 +1，灵石 +60"),
        _c("徒手挖掘矿石", rewards={"spirit_stones": 30}, flavor="你费了好大力气，只挖出几块碎矿。灵石 +30"),
        _c("寻找出路", rewards={}, flavor="你找到一条裂缝，勉强爬了出去。"),
    ]
))

EVENTS.append(_e(
    "炼体散修",
    "路遇一位浑身肌肉虬结的散修，他正在用巨石砸自己的手臂，见你路过便招呼道：「来，一起练。」",
    [
        _c("加入他的炼体训练", condition=_cond("bone", 5), rewards={"physique": 1, "bone": 1}, flavor="散修的炼体之法虽然粗暴，但确实有效，你的筋骨肉身都得到了强化。体魄 +1，根骨 +1"),
        _c("加入他的炼体训练", rewards={"physique": 1}, flavor="你咬牙坚持了下来，虽然浑身酸痛，但肉身确实强了几分。体魄 +1"),
        _c("向他请教炼体心得", rewards={"bone": 1}, flavor="散修虽然粗犷，但炼体经验丰富，你从中受益匪浅。根骨 +1"),
        _c("婉拒，继续赶路", rewards={}, flavor="散修耸耸肩，继续砸石头。"),
    ]
))

EVENTS.append(_e(
    "灵药温泉",
    "你发现一处天然温泉，泉水中漂浮着几株不知名的灵草，散发着药香。",
    [
        _c("浸泡温泉，让药力渗入体内", condition=_cond("bone", 5), rewards={"bone": 1, "lifespan": 5}, flavor="灵药温泉的药力渗入骨髓，你感到根骨在缓缓强化。根骨 +1，寿元 +5"),
        _c("浸泡温泉，让药力渗入体内", rewards={"lifespan": 3}, flavor="温泉舒适宜人，虽无大用，但身心舒畅。寿元 +3"),
        _c("采集灵草带走", rewards={"spirit_stones": 40}, flavor="灵草品质不错，可以卖个好价。灵石 +40"),
    ]
))

EVENTS.append(_e(
    "负重登山",
    "前方是一座陡峭的灵山，山路上散落着前人留下的铁锁和石锁，似乎是某种修炼方式。",
    [
        _c("背负石锁攀登", condition=_cond("physique", 6), rewards={"physique": 1, "bone": 1}, flavor="你背着百斤石锁登顶，全身筋骨在极限中得到突破。体魄 +1，根骨 +1"),
        _c("背负石锁攀登", rewards={"physique": 1}, flavor="你勉强登到半山腰便力竭，但肉身确实强了些。体魄 +1"),
        _c("轻装登顶", rewards={"cultivation": 30}, flavor="山顶灵气充沛，你盘坐修炼片刻。修为 +30"),
        _c("绕山而行", rewards={}, flavor="你选择了平坦的路。"),
    ]
))

EVENTS.append(_e(
    "古井沉剑",
    "废弃村落中有一口古井，井底隐约有寒光闪烁，似乎沉着什么东西。",
    [
        _c("潜入井底探查", condition=_cond("physique", 7), rewards={"bone": 1, "spirit_stones": 80}, flavor="井底寒气刺骨，你在极寒中取出一柄残剑，骨骼在寒气淬炼下更加坚韧。根骨 +1，灵石 +80"),
        _c("潜入井底探查", rewards={"lifespan": -5}, flavor="井底寒气太重，你被冻得半死才爬上来。寿元 -5"),
        _c("用绳索打捞", rewards={"spirit_stones": 30}, flavor="捞上来一些碎铁片，勉强能卖几个灵石。灵石 +30"),
    ]
))

EVENTS.append(_e(
    "妖兽骨架",
    "林中发现一具巨大的妖兽骨架，骨骼上还残留着丝丝灵气，散发着淡淡的威压。",
    [
        _c("取一根骨头研究", condition=_cond("comprehension", 6), rewards={"bone": 1}, flavor="你从妖兽骨骼的纹理中悟出一丝强化根骨的法门。根骨 +1"),
        _c("取一根骨头研究", rewards={"spirit_stones": 20}, flavor="骨头品质一般，但还能卖几个灵石。灵石 +20"),
        _c("在骨架旁打坐，感悟妖兽生前的气息", condition=_cond("soul", 6), rewards={"soul": 1}, flavor="你从残留的威压中感悟到一丝强大生灵的神识波动。神识 +1"),
        _c("在骨架旁打坐，感悟妖兽生前的气息", rewards={"cultivation": 20}, flavor="略有所悟，修为精进。修为 +20"),
    ]
))

EVENTS.append(_e(
    "铁砂掌传承",
    "一块石碑上刻着「铁砂掌」三字，下方是详细的修炼步骤：将双手反复插入铁砂中锤炼。旁边果然有一缸铁砂。",
    [
        _c("按照石碑所述修炼", condition=_cond("bone", 5), rewards={"physique": 1}, flavor="双手在铁砂中反复锤炼，虽然疼痛难忍，但掌力大增。体魄 +1"),
        _c("按照石碑所述修炼", rewards={"lifespan": -2}, flavor="铁砂磨破了双手，伤口感染，折腾了好一阵。寿元 -2"),
        _c("记下修炼方法离去", rewards={"cultivation": 15}, flavor="虽未实践，但理论知识也有些用处。修为 +15"),
    ]
))

EVENTS.append(_e(
    "深渊凝视",
    "你站在一处深不见底的悬崖边，崖底传来阵阵诡异的低鸣，凝视深渊时感到神识被牵引。",
    [
        _c("集中精神，以神识探入深渊", condition=_cond("soul", 6), rewards={"soul": 1}, flavor="你的神识在深渊中经受考验，回来后变得更加凝练。神识 +1"),
        _c("集中精神，以神识探入深渊", rewards={"lifespan": -5}, flavor="深渊中的力量反噬了你的神识，头痛欲裂。寿元 -5"),
        _c("后退几步，不再凝视", rewards={}, flavor="你明智地选择了远离。"),
    ]
))

EVENTS.append(_e(
    "吞服生铁",
    "一位游方药师向你推荐一种古老的炼体秘法：吞服特制的铁丸，以铁淬骨。",
    [
        _c("购买铁丸吞服", condition=_cond("physique", 6), rewards={"spirit_stones": -30, "bone": 1}, flavor="铁丸入腹，一股灼热之力渗入骨骼，你感到根骨在强化。灵石 -30，根骨 +1"),
        _c("购买铁丸吞服", rewards={"spirit_stones": -30, "lifespan": -3}, flavor="铁丸品质不佳，你腹痛了好几天。灵石 -30，寿元 -3"),
        _c("婉拒", rewards={}, flavor="你对来路不明的东西保持警惕。"),
    ]
))

EVENTS.append(_e(
    "灵兽追逐",
    "一头灵兽突然从林中窜出，朝你扑来。你本能地开始奔跑。",
    [
        _c("全力奔跑，在追逐中锤炼体魄", condition=_cond("physique", 5), rewards={"physique": 1}, flavor="你在极限奔跑中突破了身体的桎梏，体魄得到提升。体魄 +1"),
        _c("全力奔跑，在追逐中锤炼体魄", rewards={"lifespan": -3}, flavor="你跑得上气不接下气，摔了好几跤。寿元 -3"),
        _c("转身迎战", condition=_cond("physique", 7), rewards={"bone": 1, "spirit_stones": 50}, flavor="你一拳击退灵兽，在搏斗中骨骼得到锤炼。根骨 +1，灵石 +50"),
        _c("转身迎战", rewards={"lifespan": -8}, flavor="灵兽比你想象的强，你被咬伤后才逃脱。寿元 -8"),
    ]
))

EVENTS.append(_e(
    "悟道石碑",
    "路边立着一块古老的石碑，上面刻着一段晦涩的经文，字迹模糊但隐含大道。",
    [
        _c("静心参悟经文", condition=_cond("comprehension", 7), rewards={"soul": 1, "comprehension": 1}, flavor="你在经文中悟出一丝天道真意，神识与悟性同时提升。神识 +1，悟性 +1"),
        _c("静心参悟经文", rewards={"cultivation": 40}, flavor="虽未大悟，但修为有所精进。修为 +40"),
        _c("拓印经文带走", rewards={"spirit_stones": 30}, flavor="经文拓本或许有人愿意收购。灵石 +30"),
    ]
))

EVENTS.append(_e(
    "寒潭沐浴",
    "一处寒潭冒着白气，潭水冰冷刺骨，但水底隐约有灵光闪烁。",
    [
        _c("跳入寒潭，以极寒淬体", condition=_cond("physique", 6), rewards={"bone": 1}, flavor="寒气渗入骨髓，你在极寒中咬牙坚持，根骨得到强化。根骨 +1"),
        _c("跳入寒潭，以极寒淬体", rewards={"lifespan": -4}, flavor="寒气太重，你差点冻僵在潭中。寿元 -4"),
        _c("在潭边修炼", rewards={"cultivation": 35}, flavor="寒潭散发的灵气有助修炼。修为 +35"),
    ]
))

EVENTS.append(_e(
    "搬运巨石",
    "一位老农请你帮忙搬开堵住水渠的巨石，他说搬开后会有报酬。",
    [
        _c("运起全身力气搬石", condition=_cond("physique", 5), rewards={"physique": 1, "reputation": 5}, flavor="你搬开巨石，在极限发力中体魄得到锤炼，老农感激不已。体魄 +1，声望 +5"),
        _c("运起全身力气搬石", rewards={"reputation": 3}, flavor="你费了好大力气才搬开，累得够呛，但老农很感激。声望 +3"),
        _c("婉拒离去", rewards={}, flavor="你有更重要的事要做。"),
    ]
))

EVENTS.append(_e(
    "古墓石门",
    "你发现一座古墓的入口，石门紧闭，门上刻着一道谜题。",
    [
        _c("以蛮力推开石门", condition=_cond("physique", 8), rewards={"physique": 1, "spirit_stones": 100}, flavor="你以惊人的力量推开了石门，墓中有不少陪葬灵石。体魄 +1，灵石 +100"),
        _c("以蛮力推开石门", rewards={"lifespan": -5}, flavor="石门纹丝不动，你用力过猛伤了筋骨。寿元 -5"),
        _c("解开谜题开门", condition=_cond("comprehension", 7), rewards={"soul": 1, "spirit_stones": 80}, flavor="你解开谜题，石门缓缓开启，墓中有灵石和一丝神识感悟。神识 +1，灵石 +80"),
        _c("解开谜题开门", rewards={"spirit_stones": 40}, flavor="你勉强解开谜题，墓中只有些普通灵石。灵石 +40"),
        _c("离开此地", rewards={}, flavor="古墓凶险，不宜久留。"),
    ]
))
