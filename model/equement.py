class Base_Equement(object):
    #ABC类，不可用，懒得定义
    def __init__(self,
                eque_name =None,
                eque_type =None,
                need_job ="all", #是否有职业限定，但是我可能会放弃这个的定义,
                strengh = 0,#力量
                intelligent =  0 ,#智力
                brawn = 0 ,#  体力
                sprit = 0,# 精神
                phydef = 0, #物理防御
                magicdef = 0, #魔法防御
                hp = 0, #生命值
                mp = 0, #魔法值

                phyAtkPower = 0, #物理攻击力
                magicAtkPower = 0, #魔法攻击力
                critnum = 0, #暴击数值
                critrate = 0, #直接暴击率
                cri_damage = 0, #暴击伤害
                damage_increase = 0, #黄字
                extra_damage = 0, #白字
                skill_attk = 0, #技攻

                mipha_num = 0, #冰强
                daekel_num = 0, #火强
                urbosa_num = 0,#光强
                revali_num = 0,#暗强


                strengh_increase_rate = 0 ,#力量加成系数
                intelligent_increase_rate = 0, #智力加成系数
                phyatk_increase_rate = 0, #物理加成系数
                magicatk_increase_rate = 0, #魔法加成系数

                shield = 0,#护盾
                attack_speed = 0,
                pushskill_speed =0 ,
                move_speed =0 ,

                element_extra_damage = 0

    ):
        #所有输入值都SELF化
        self.eque_name = eque_name
        self.need_job = need_job
        self.eque_type = eque_type

        self.strengh = strengh
        self.intelligent = intelligent
        self.brawn = brawn
        self.sprit = sprit

        self.phydef = phydef
        self.magicdef = magicdef
        self.hp = hp
        self.mp = mp

        self.phyAtkPower = phyAtkPower
        self.magicAtkPower = magicAtkPower
        self.critum =critnum
        self.critrate = critrate
        self.cri_damage = cri_damage

        self.damage_increase = damage_increase
        self.extra_damage = extra_damage
        self.skill_attk = skill_attk
        self.mipha_num = mipha_num
        self.daekel_num = daekel_num
        self.urbosa_num = urbosa_num
        self.revail_num = revali_num

        self.strengh_increase_rate = strengh_increase_rate
        self.intelligent_increase_rate = intelligent_increase_rate
        self.phyatk_increase_rate = phyatk_increase_rate
        self.magicatk_increase_rate = magicatk_increase_rate

        self.shield = shield
        self.attack_speed = attack_speed
        self.pushskill_speed= pushskill_speed
        self.move_speed = move_speed
        self.element_extra_damage = element_extra_damage


        self.all_attr =[
            self.strengh,
            self.intelligent,
            self.brawn,
            self.sprit,
            self.phydef,
            self.magicdef,
            self.hp,
            self.mp,
            self.phyAtkPower,
            self.magicAtkPower,
            self.critum,
            self.critrate,
            self.cri_damage,
            self.damage_increase,
            self.extra_damage,
            self.skill_attk,
            self.mipha_num,
            self.daekel_num,
            self.urbosa_num,
            self.revail_num,
            self.strengh_increase_rate,
            self.intelligent_increase_rate,
            self.phyatk_increase_rate,
            self.magicatk_increase_rate,
            self.shield,
            self.attack_speed,
            self.pushskill_speed,
            self.move_speed,
            self.element_extra_damage
            
        ]

    def load_from_dict(self,data):
        for key, value in data.items():
                setattr(self, key, value)
    


                                          
class Pet_and_Equepment(Base_Equement):
    #宠物本身当做一个装备来处就好了
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        