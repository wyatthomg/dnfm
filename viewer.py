import streamlit as st

# 装备
EQUIP_DB = {
    "鬼面": {"黄字": 0.32, "攻击系数": 0.62, "技伤": 1.15 * 1.13, "白字": 0.12},
    "冥火": {"属强": 100, "技伤": 1.12 * 1.09, "属白": 0.3, "白字": 0.1, "攻击系数": 0.12},
    "坚定": {"属强": 35, "白字": 0.50, "技伤": 1.26, "攻击系数": 0.17, "黄字": 0.07, "力智系数": 0.1, "爆伤": 0.1,
             "暴击值": 100},
    "虚空": {"属强": 50, "攻击系数": 0.1, "力智系数": 0.1, "技伤": 1.1 * 1.27, "黄字": 0.3, "暴击值": 80, "爆伤": 0.15},
    "色龙": {"力智系数": 0.30, "攻击系数": 0.10, "白字": 0.26, "技伤": 1.19, "黄字": 0.25, "暴击值": 300,
             "减防": 0.048},
    "黑洞": {"白字": 0.58, "技伤": 1.22 * 1.13, "暴击值": 100, "力智系数": 0.07, "黄字": 0.13, "攻击系数": 0.2},
    "安魂": {"属强": 75, "攻击系数": 0.15, "cd": 10, "白字": 0.15, "技伤": 1.27, "其他暂定": 1.5478 * 0.85},

    "黑暗": {"属强": 115, "黄字": 0.35, "技伤": 1.1 * 1.09, "攻击": 100, "属白": 0.05},
    "幽魂": {"属强": 120, "黄字": 0.05, "爆伤": 0.2, "技伤": 1.1 * 1.05, "属白": 0.2, "暴击值": 70, "力智": 50,
             "攻击": 50},
    "深海": {"属强": 65, "技伤": 1.15 * 1.07, "属白": 0.1, "攻击系数": 0.4, "暴击值": 100, "力智系数": 0.08,
             "其他暂定": 1.01125},
    "坠落": {"属强": 50, "黄字": 0.18, "技伤": 1.12 * 1.14, "属白": 0.1, "暴击值": 200, "白字": 0.1,
             "其他暂定": 1.0542},
    "天狼": {"爆伤": 0.12, "力智": 132, "白字": 0.25, "技伤": 1.28, "减防": 0.248, "攻击系数": 0.06, "力智系数": 0.06,
             "黄字": 0.06},
    "恶魔": {"力智系数": 0.34, "攻击系数": 0.24, "技伤": 1.15 * 1.13, "白字": 0.4},
    "纯粹": {"属强": 110, "攻击": 50, "力智系数": 0.02, "属白": 0.1, "减防": 0.074, "暴击值": 80},
}
# 首饰数据库
JEWELRY_DB = {
    "暗杀": {"技伤": 1.32, "黄字": 0.125, "暴击值": 130, "力智系数": 0.03, "爆伤": 0.125},
    "火套": {"属强": 39, "技伤": 1.11, "属白": 0.15, "爆伤": 0.14, "黄字": 0.09},
    "明星": {"属强": 36, "技伤": 1.11, "属白": 0.24},
    "精炼": {"技伤": 1.07 * 1.05 * 1.05, "黄字": 0.0, "暴击值": 130, "力智系数": 0.06, "白字": 0.23, "属强": 26}
}
# 武器数据库
WEAPON_DB = {
    "吞灵左轮": {"黄字": 0.4, "攻击系数": 0.13},
    "夕阳左轮": {"黄字": 0.45, "其他暂定": 0.1 * 1.4 * 1.3 + (1 - 0.1)},  # 爆头 多射两发/30攻击
    "终结左轮": {"暴击值": 150, "攻击系数": 0.55, "其他暂定": 0.15 * 1.2 + (1 - 0.15), "爆伤": 0.05},
    # 移射1.2, 死左 +2 算作 0.05 爆伤

    "麦加手枪": {"白字": 0.5, "其他暂定": 1.067},  # 空投 等级+2/数量+20%/间隔-15%
    "导航手枪": {"力智系数": 0.43, "其他暂定": 1.088},  # 改良+3, 78/定时/机场+3
    "巴顿手枪": {"力智系数": 0.15, "攻击系数": 0.42, "其他暂定": 1.03},  # 65 +2

    "战神步枪": {"力智系数": 0.3, "暴击值": 200, "黄字": 0.18},
    "九龙步枪": {"属强": 24, "属白": 0.3},
    "僵尸步枪": {"属强": 14, "黄字": 0.13, "属白": 0.15, "其他暂定": 0.6 * 1.1 + (1 - 0.6)},  # 爆炎+3

    "铁甲手炮": {"黄字": 0.5, "其他加成": 0.2 * 1.25 * 1.2 * 1.06 + (1 - 0.2)},  # 反坦克  25伤害/cd-1/等级+2
    "破甲手炮": {"黄字": 0.2, "攻击系数": 0.4, "减防": (0.074 + 0.108) / 2 / 2},  # 减防折中计算, 持续时间只有一半再 / 2
    "时空手炮": {"属强": 12, "属白": 0.27, "其他暂定": 0.3 * 1.135 + (1 - 0.3)},  # 压缩 +3

    "暗白手弩": {"属白": 0.3},  # 手弩走无限, 对银弹,破甲相当于0加成
    "苍穹手弩": {"力智系数": 0.55, "其他暂定": (0.15 * 1.06 + (1 - 0.15)) * (1 + 0.0125 * 2)},
    # 核心被动技能 +2 算 1.05, 汽油弹+2
    "撒旦手弩": {"白字": 0.54, "其他暂定": 1 + 0.0125 * 2},  # 两个核心 +2

    "怨恨短剑": {"力智系数": 0.35, "减防": 0.124},
    "百魔短剑": {"攻击系数": 0.15, "白字": 0.3, "其他暂定": 0.25 * 1.2 + (1 - 0.25)},  # lv50+2
    "剑王短剑": {"力智系数": 0.25, "攻击系数": 0.35, "其他暂定": 0.2 * 1.03 + (1 - 0.2)},  # 波动+1

    "九龙太刀": {"力智系数": 0.15, "黄字": 0.45, "其他暂定": 0.4 * 1.1 + (1 - 0.4)},  # 加了一堆技能, 加成按 10% 来算
    "十斩太刀": {"黄字": 0.25 * 0.9, "白字": 0.35},  # 20s 中 12s 流血增伤黄字 25, 考虑抗性金符文后按照 18/20 来测算
    "十闪太刀": {"黄字": 0.5, "其他暂定": 0.2 * 1.3 + (1 - 0.2)},  # 猛龙+30%

    "心脏钝器": {"白字": 0.4, "黄字": 0.2},  # 100/80/60/40/20 hp 下 加伤 0/10/20/30/40. 按照平均20来算
    "矮黄钝器": {"力智系数": 0.2, "攻击系数": 0.27, "力智": 120},
    "地狱钝器": {"爆伤": 0.43},  # 你在逗我, 貌似翻译有问题还是就这样

    "恶魔巨剑": {"力智系数": 0.2, "攻击系数": 0.35, "其他暂定": 1.025},  # 核心 +2
    "地灵巨剑": {"黄字": 0.25, "攻击系数": 0.38},
    "罪恶巨剑": {"黄字": 0.30 * 0.9, "力智": 50, "其他暂定": 0.15 * 1.05 + (1 - 0.15)},
    # 5s 出血 3s 的30黄, 考虑抗性金符文后按照 0.9 来测算, 抓头+2

    "火焰光剑": {"白子": 0.25 * 0.9, "攻击系数": 0.43},  # 10s 灼烧 7s 的25白, 考虑抗性金符文后按照 0.9 来测算
    "冰龙光剑": {"属强": 20, "属白": 0.2, "其他暂定": 0.15 * 1.06 * 1.5 + (1 - 0.15)},  # 猛龙+2/形态+1
    "寒霜光剑": {"黄字": 0.3 * 0.5, "攻击系数": 0.3, "其他暂定": 0.15 * 1.25 + (1 - 0.15)},
    # 感电 30,  拔刀 25%重置算作 1.25 提升

    "灵魂土剑": {"白字": 0.2, "黄字": 0.25, "属强": 20},
    "象征土剑": {"白字": 0.3, "黄字": 0.25},
    "岩石土剑": {"黄字": 0.63},

    "齿轮风刀": {"黄字": 0.45, "攻击系数": 0.13},
    "普斯风刀": {"白字": 0.4, "攻击系数": 0.15},
    "骑士风刀": {"白字": 0.3, "属强": 25, "攻击系数": 0.1},

    "邪恶手套": {"黄字": 0.2, "属强": 35, "其他暂定": 1.05},  # 光刃+2 算 1.05 好了
    "碎骨手套": {"力智": 60, "属白": 0.28, "其他暂定": 0.15 * 1.3 * 1.1 * 1.3 + (1 - 0.15)},  # 分身 +30伤害/-10cd/数量+2
    "异魔手套": {"暴击值": 150, "爆伤": 0.35, "黄字": 0.25},  # 分身 +30伤害/-10cd/数量+2

    "冰冻臂铠": {"属白": 0.3},
    "暴躁臂铠": {"减防": (0.077 + 0.108) / 2, "黄字": 0.2, "攻击系数": 0.4},  # 减防按照中间值来算
    "大地臂铠": {"力智": 100, "属强": 25, "黄字": 0.22, "白字": 0.20},

    "遗迹爪子": {"属强": 15, "属白": 0.26},

    "遗迹拳套": {"黄字": 0.35, "其他暂定": 1.05},  # 1-70 +1
    "狂龙拳套": {"攻击系数": 0.5, "其他暂定": 1.15},  # 一堆乱七八糟直接按照全伤害+15得了
    "狂野拳套": {"黄字": 0.45, "攻击系数": 0.13},

    "飞龙棍子": {"黄字": 0.45, "白字": 0.1},  # 龙加成 10白字 算作全程触发好了
    "狂风棍子": {"黄字": 0.3, "白字": 0.3},
    "蹀血棍子": {"力智系数": 0.33, "力智": 100},

    "纯白长矛": {"属强": 15, "黄字": 0.2, "属白": 0.17},
    "书记长矛": {"暴击值": 200, "爆伤": 0.14, "黄字": 0.3, "其他暂定": 1.025},  # 核心技能 +2
    "地狱长矛": {"属强": 14, "白字": 0.55},

    "地狱棍棒": {"黄字": 0.55, "其他暂定": 0.15 * 1.06 + (1 - 0.15)},  # 碎霸 +2
    "达克棍棒": {"白字": 0.6},
    "终极棍棒": {"力智系数": 0.28, "攻击系数": 0.15, "其他暂定": 0.8 * 1.08 + (1 - 0.8)},  # 一堆技能加成,按照0.8 占比下的 1.08 加成

    "冰龙魔杖": {"属白": 0.25, "属强": 30},
    "灵兔魔杖": {"力智系数": 0.3, "攻击系数": 0.2, "属强": 23},
    "白猫魔杖": {"属白": 0.2, "黄字": 0.35, "属强": 12},

    "黄金法杖": {"爆伤": 0.28, "属白": 0.25, "属强": 15, "其他暂定": 0.12 * 1.026 + (1 - 0.12)},  # 小技能+1
    "灾难法杖": {"属强": 17, "属白": 0.18, "其他暂定": 0.23 * 1.2 * 1.3 * 1.07 * 1.3 + (1 - 0.23)},
    # 5s 7s 20s 技能 +3 +20伤害 + 形态
    "威力法杖": {"力智": 50, "黄字": 0.25, "白字": 0.27},

    "危机扫把": {"力智": 120, "黄字": 0.55},
    "战神扫把": {"攻击": 70, "属强": 20, "白字": 0.2, "减防": 0.048, "力智系数": 0.03},
    "魔术扫把": {"黄字": 0.25, "攻击系数": 0.3, "其他暂定": 0.03 * 1.075 + (1 - 0.03)},  # 小技能 +3

    "亡者十字": {"白字": 0.4, "攻击系数": 0.14, "其他暂定": (0.08 * 1.06 + (1 - 0.08)) * 1.0375},  # 光复 +2, buff + 3
    "戴罪十字": {"白字": 0.4, "攻击系数": 0.12, "其他暂定": (0.08 * 1.06 + (1 - 0.08)) * 1.025},  # 锤子 +2, buff + 2
    "信念十字": {"黄字": 0.2, "减防": 0.124, "其他暂定": 1.025},  # buff + 3

    "瘟疫念珠": {"黄字": 0.43, "攻击系数": 0.15, "其他暂定": 0.08 * 1.06 + (1 - 0.08)},  # 20s技能 + 2
    "米兰念珠": {"暴击值": 50, "属强": 20, "黄字": 0.2, "攻击系数": 0.25, "其他暂定": 0.08 * 1.06 + (1 - 0.08)},
    # 20s技能 + 2
    "逐龙念珠": {"属白": 0.22, "力智系数": 0.15, "其他暂定": 0.3 * 1.12 + (1 - 0.3)},  # 40s技能 + 3

    "暗影图腾": {"属白": 0.2, "暴击值": 150, "黄字": 0.2, "属强": 32},
    "五行图腾": {"白字": 0.08, "属白": 0.3, "其他暂定": 0.2 * 1.045 + (1 - 0.2)},  # 小技能 +1/2 按照 0.03 * 1.5 提升来算
    "触须图腾": {"白字": 0.2, "黄字": 0.37},

    "牛头镰刀": {"白字": 0.15, "力智系数": 0.50},
    "领域镰刀": {"暴伤": 0.3, "黄字": 0.3, "其他暂定": 1.025},  # 被动buff + 2
    "死神镰刀": {"黄字": 0.3, "白字": 0.4},

    "牛头战斧": {"力智系数": 0.43, "攻击系数": 0.15},
    "狮王战斧": {"攻击系数": 0.69},
    "狮王战斧": {"攻击系数": 0.59},
    "巫塔战斧": {"黄字": 0.38, "白字": 0.16},
}
# 辅助左槽数据库, 突破攻擊按照 100 來算
ASSIST_DB = {
    "牛角": {"攻击系数": 0.1, "力智系数": 0.1, "爆伤": 0.08},
    "黑洞": {"属白": 0.1, "技伤": 1.05},
    "怀表": {"黄字": 0.07, "其他暂定": (0.95 * 1.05 + (1 - 0.95)) * 1.02, "攻击": 100},
    "手套": {"攻击": 430, "其他暂定": 1.02},
    "面具": {"白字": 0.2, "其他暂定": 1.02, "攻击": 100},
    "羽毛": {"爆伤": 0.25, "其他暂定": (0.11 * 1.09 + (1 - 0.11)) * 1.02, "攻击": 100},
}


class Home():

    def __init__(self):
        # 最终测算结果
        self.result = []
        self.color = "indigo"
        # 基础力智
        self.base_power = 0
        # 基础攻击
        self.base_attack = 0
        # 基础属强
        self.base_attribute_strengthen = 0
        # 基础黄字
        self.base_yellow = 0
        # 基础白字
        self.base_white = 0
        # 基础减防
        self.base_reduce_defense = 0
        # 基础技伤
        self.base_skill_damage = 0
        # 基础暴击率
        self.base_critical = 0
        # 基础暴击值
        self.base_critical_value = 0
        # 基础暴伤
        self.base_critical_damage = 0
        st.set_page_config(
            page_title='页面标题',
            page_icon='☆☆☆',
            layout='wide',
            initial_sidebar_state='expanded'
        )

    def cal_compose(self, c_weapon=None):
        for equip, equip_info in EQUIP_DB.items():
            for jewelry, jewelry_info in JEWELRY_DB.items():
                # 火套不会跟光以及暗的套装搭配. 直接忽略
                if jewelry == "火套":
                    if equip in ["幽魂(高额暗属白)", "纯粹(光强辅助套)"]:
                        continue
                for weapon, weapon_info in WEAPON_DB.items():
                    if c_weapon and c_weapon not in weapon:
                        continue
                    for assist, assist_info in ASSIST_DB.items():
                        power = 0
                        attack = 0
                        power_rate = 0
                        attack_rate = 0
                        yellow = 0
                        white = 0
                        attribute_strengthen = 0
                        attribute_strengthen_yellow_rate = 0
                        attribute_strengthen_white_rate = 0
                        reduce_defense = 0
                        critical = 0
                        critical_value = 0
                        critical_damage = 0
                        skill_damage = 1
                        other = 1

                        for each in [equip_info, jewelry_info, weapon_info, assist_info]:
                            power += each.get("力智", 0)
                            attack += each.get("攻击", 0)
                            power_rate += each.get("力智系数", 0)
                            attack_rate += each.get("攻击系数", 0)
                            yellow += each.get("黄字", 0)
                            white += each.get("白字", 0)
                            attribute_strengthen += each.get("属强", 0)
                            attribute_strengthen_white_rate += each.get("属白", 0)
                            attribute_strengthen_yellow_rate += each.get("属黄", 0)
                            reduce_defense += each.get("减防", 0)
                            critical += each.get("暴击率", 0)
                            critical_value += each.get("暴击值", 0)
                            critical_damage += each.get("爆伤", 0)
                            if each.get("技伤"):
                                skill_damage *= each.get("技伤")  # 装备间乘算
                            if each.get("其他暂定"):
                                other *= each.get("其他暂定")  # 其他加成乘算

                        self.result.append(self.cal_main(power, attack, power_rate, attack_rate,
                                                         attribute_strengthen, yellow,
                                                         attribute_strengthen_yellow_rate, white,
                                                         attribute_strengthen_white_rate,
                                                         reduce_defense, skill_damage,
                                                         critical, critical_value, critical_damage,
                                                         other, equip, jewelry, weapon, assist))

    def cal_main(self, power, attack, power_rate, attack_rate, attribute_strengthen, yellow,
                 attribute_strengthen_yellow_rate, white, attribute_strengthen_white_rate, reduce_defense,
                 skill_damage, critical, critical_value, critical_damage, other,
                 equip, jewelry, weapon, assist):
        # ----------------- 面板信息 -----------------
        # 面板力智 =  基础力智 + 装备力智[+] * 装备力智百分比[+]
        panel_power = (self.base_power + power) * (1 + power_rate)
        # 面板攻击 = (基础攻击 + 装备攻击值[+]) * (1 + 装备攻击百分比[+] + 武器装扮) * (1 + 最终力智 / 250)
        panel_attack = (self.base_attack + attack) * (1 + attack_rate + 0.05) * (1 + panel_power / 250)
        # 面板暴击值 = 基础暴击值 + 装备暴击值[+]
        panel_critical_value = self.base_critical_value + critical_value
        # 暴击率 = 基础暴击率 + 装备暴击率[+] + 面板暴击值 / 25.3 / 100
        panel_critical = self.base_critical + critical + panel_critical_value / 27.24 / 100
        # 暴击伤害 = 基础暴击伤害 + 装备暴击伤害[+]
        panel_critical_damage = self.base_critical_damage + critical_damage  # 暴击伤害
        # 属强 = 基础属强 + 装备属强[+]
        panel_attribute_strengthen = self.base_attribute_strengthen + attribute_strengthen  # 属强
        # ----------------- 加成系数 -----------------
        # 力智提升
        fin_power_rate = (1 + (self.base_power + power) * (1 + power_rate) / 250) / (1 + (self.base_power / 250))
        # 攻击提升
        fin_attack_rate = (self.base_attack + attack) * (1 + attack_rate) / self.base_attack
        # 黄字提升 = 基础黄字 + 装备黄字[+]
        yellow_rate = self.base_yellow + yellow
        # 白字提升 = 基础白字 + 装备白字[+]
        white_rate = self.base_white + white
        # 属强提升 = (1 + 属强 / 220)
        # attribute_strengthen_rate = (1 + panel_attribute_strengthen / 220)
        attribute_strengthen_rate = panel_attribute_strengthen * 0.0045 + 1.05
        # 属黄提升  = 面板属黄 * 属强提升系数
        attribute_strengthen_yellow_rate *= attribute_strengthen_rate
        # 属白提升 = 面板属白 * 属强提升系数
        fin_attribute_strengthen_white_rate = attribute_strengthen_white_rate * attribute_strengthen_rate
        # 技伤 = 基础技伤 + 装备技伤[*]
        skill_damage_rate = self.base_skill_damage + skill_damage
        # 减防 = 基础减防 + 装备减防[+]
        reduce_defense_rate = self.base_reduce_defense + reduce_defense
        # 其他伤害加成 = 装备其他暂定伤害加成[*]
        other = other
        #  ----------------- 暂存常数系数 -----------------
        # 暴击期望 = 暴击率 * 暴击伤害 + ( 1 - 暴击率 )
        critical_desire = panel_critical * panel_critical_damage + (1 - panel_critical)
        # 最终黄字 = 1 + 属黄提升 + 黄字提升
        yellow = 1 + attribute_strengthen_yellow_rate + yellow_rate
        # 最终白字 = 1 + 属白提升  + 白字提升
        fin_white = 1 + fin_attribute_strengthen_white_rate + white_rate
        # 最终强度 = 面板攻击 * 黄提升 * 白提升 * 暴击期望提升 * 属强提升 * 技伤提升 * 其他提升
        fin_strength = panel_attack * yellow * fin_white * critical_desire * attribute_strengthen_rate * other * \
                       skill_damage_rate
        # 强度系数 = 力智提升 * 攻击提升 * 黄提升 * 白提升 * 暴击期望提升 * 属强提升 * 技伤提升 * 其他提升
        strength_rate = fin_power_rate * fin_attack_rate * yellow * fin_white * critical_desire * \
                        attribute_strengthen_rate * other * skill_damage_rate
        return {
            "装备": equip,
            "首饰": jewelry,
            "武器": weapon,
            "辅助": assist,
            "力智": panel_power,
            "攻击": panel_attack,
            "属强": panel_attribute_strengthen,
            "暴击": panel_critical,
            "暴伤": panel_critical_damage,
            "暴击期望": critical_desire,

            "力智系数": power_rate,
            "攻击系数": attack_rate,
            "黄字": yellow_rate,
            "白字": white_rate,
            "属白": attribute_strengthen_white_rate,
            "属白提升": fin_attribute_strengthen_white_rate,
            "技伤": skill_damage_rate - 1,
            "其他加成": other - 1,
            "减防加成": reduce_defense_rate,
            "强度值": fin_strength,
            "强度系数": strength_rate,
        }

    def start(self):
        st.title("装备测试")
        profession_map = {
            "团长": {"暴击率": 0.075, "暴伤": 0.223},
            "机械": {"力智": 170, "技伤": 0.13},
            "娘漫": {"暴伤": 0.3, "技伤": 0.09, "暴击率": 0.056, "属强": 10},
            "大枪": {"暴击率": 0.098, "暴伤": 0.178},
            "井盖": {"技伤": 0.13, "暴伤": 0.32},
        }
        cols = st.columns([1, 1,  9])
        with cols[0]:
            profession = st.selectbox("职业", profession_map.keys(), placeholder="职业", help="职业")
            base_power = st.number_input("基础力智", value=3500)
            base_attack = st.number_input("基础攻击", value=3200)
            base_attribute_strengthen = st.number_input("基础属强", value=210)
            base_yellow = st.number_input("基础黄字", value=15)
            base_white = st.number_input("基础黄字", value=24)
        with cols[1]:
            base_reduce_defense = st.number_input("基础减防", value=0)
            base_skill_damage = st.number_input("基础技伤", value=21)
            base_critical = st.number_input("基础暴击率", value=16)
            base_critical_value = st.number_input("基础暴击值", value=804)
            base_critical_damage = st.number_input("基础暴伤", value=150)

            self.base_power = base_power + profession_map[profession].get("力智", 0)
            self.base_attack = base_attack + profession_map[profession].get("攻击", 0)
            self.base_attribute_strengthen = base_attribute_strengthen + profession_map[profession].get("属强", 0)
            self.base_yellow = base_yellow / 100
            self.base_white = base_white / 24
            self.base_reduce_defense = base_reduce_defense / 100 + profession_map[profession].get("减防", 0)
            self.base_skill_damage = base_skill_damage / 100 + profession_map[profession].get("技伤", 0)
            self.base_critical = base_critical / 100 + profession_map[profession].get("暴击率", 0)
            self.base_critical_value = base_critical_value + profession_map[profession].get("暴击值", 0)
            self.base_critical_damage = base_critical_damage / 100 + profession_map[profession].get("暴伤", 0)
        with cols[2]:
            self.cal_compose()
            st.dataframe(self.result)

if __name__ == '__main__':
    Home().start()