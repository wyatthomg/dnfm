# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:52:07 2023

    
                                        `7M`    `7M`
                                         MM      MM
  `7M'    ,M    `MF`7M'   `MF' ,6"Yb. `mmMMmm `mmMMmm 
    VA   ,VAA   ,V   VA   ,V  8)   MM    MM      MM 
     VA ,V  VA ,V     VA ,V    ,pm9MM    MM      MM 
      VVV    VVV       VVV    8M   MM    MM      MM    
       W      W        ,V     `Moo9^Yo.   ML.     ML. 
                      ,V
                    OOb"
"""
from equement import Pet_and_Equepment

class Role(object):
    def __init__(self,
                 job,
                strength_base,#基础力量
                intellect_base, #基础智力
                brawn_base,   #基础体力
                spirit_base, #基础精神
                phyAtkPower_base, #基础物理攻击力
                magicAtkPower_base, #基础魔法攻击力
                critnum_base, #基础暴击数值
                daekel_num, #基础火强
                mipha_num, #基础冰强
                urbosa_num, #基础光强
                revali_num, #基础暗强
                hp_base , #基础生命值
                mp_base , #基础魔法值
                phydef_base, #基础物理防御
                magicdef_base, #基础魔法防御
                attack_speed_base,
                pushskill_speed_base,
                move_speed_base,

      ):
        #魔力结晶和公会的现在算作基础，脱妆抄数据就好
        self.job = job# job类后面映射到Skill Model获取被动过和技能明细  
        #暴击系数其实要看被攻击者等级，先放
        self.strength_base = strength_base #角色力量
        self.intellect_base = intellect_base #智力
        self.brawn_base = brawn_base #体力
        self.sprit_base = spirit_base #精神
        self.phyAtkPower_base = phyAtkPower_base #基础物理攻击力
        self.magicAtkPower_base = magicAtkPower_base #基础魔法攻击力
        self.critnum_base = critnum_base  #基础暴击数值
        self.daekel_num = daekel_num #火强属性值
        self.mipha_num = mipha_num #冰强属性值
        self.urbosa_num = urbosa_num #光强属性值
        self.revali_num = revali_num #暗强属性值
        self.hp_base = hp_base#基础生命值
        self.mp_base = mp_base #基础魔法值
        self.phydef_base = phydef_base #基础物理防御
        self.magicdef_base = magicdef_base #

        #伤害计算基本定义
        self.damage_increase = 1
        self.extra_damage = 1
        self.crit_damage_rate = 5 #暴击增伤比例
        self.critrate = 3 #基础暴击率
        self.skill_attk = 0

        ##其他的基本obj,先空出来
        #宠物
        self.pet = None
        self.pet_red = None
        self.pet_blue = None
        self.pet_green = None
        
        #防具 有可能防具要单独推一个类
        self.top = None
        self.head = None
        self.bottom = None
        self.belt = None
        self.under = None

        #首饰
        self.ring = None
        self.necklace = None
        self.hand = None

        #其他
        self.weapon = None
        self.stone = None

        #三速
        self.attack_speed_base = attack_speed_base
        self.pushskill_speed_base = pushskill_speed_base
        self.move_speed_base = move_speed_base

        self._type_dict = None
        # wyatthomg.add_equement(Saliya)
        self.attr_init()
    def attr_init(self):
      self.strengh = 0
      self.intelligent = 0
      self.brawn = 0
      self.sprit = 0
      self.phydef = 0
      self.magicdef = 0
      self.hp = 0
      self.mp = 0
      self.phyAtkPower = 0
      self.magicAtkPower = 0
      self.critum =0
      self.critrate = 0
      self.cri_damage = 0
      self.damage_increase = 0
      self.extra_damage = 0
      self.skill_attk = 0
      self.mipha_num = 0
      self.daekel_num = 0
      self.urbosa_num = 0
      self.revail_num = 0
      self.strengh_increase_rate = 0
      self.intelligent_increase_rate = 0
      self.brawn_increase_rate = 0
      self.sprit_increase_rate = 0
      self.phyatk_increase_rate = 0
      self.magicatk_increase_rate = 0
      self.shield = 0
      self.attack_speed = 0
      self.pushskill_speed= 0
      self.move_speed = 0
      self.element_extra_damage = 0    
  
      self.all_attr_str =[
          "strengh",
          "intelligent",
          "brawn",
          "sprit",
          "phydef",
          "magicdef",
          "hp",
          "mp",
          "phyAtkPower",
          "magicAtkPower",
          "critum",
          "critrate",
          "cri_damage",
          "damage_increase",
          "extra_damage",
          "skill_attk",
          "mipha_num",
          "daekel_num",
          "urbosa_num",
          "revail_num",
          "strengh_increase_rate",
          "intelligent_increase_rate",
          "phyatk_increase_rate",
          "magicatk_increase_rate",
          "shield",
          "attack_speed",
          "pushskill_speed",
          "move_speed",
          "element_extra_damage"
          ]
         
      
    @property
    def equement_type(self):
        if self._type_dict is None:
            # 仅在首次访问时初始化字典
            self._type_dict = {
                "pet": None,        # 宠物
                "red_pet": None,
                "blue_pet": None,
                "green_pet": None,
                "weapon": None,     # 武器
                "top": None,        # 上衣
                "head": None,       # 头
                "bottom": None,     # 下装
                "belt": None,       # 腰带
                "shoe":None,
                "under": None,      # 下装
                "ring": None,       # 戒指
                "necklace": None,   # 项链
                #套装效果暂时独立出来，后面合并到装备里面，用Eque_group的方式管理
                "three_pet": None,#宠物套装
                "two_left": None, #防具两件套效果
                "three_right":None,#首饰3件套效果
                "five_left":None #防具五件套效果
            }
        return self._type_dict
    def add_equement(self,equement):
        self.equement_type[equement.eque_type] = equement
    
    def eque_cal(self):
        self.attr_init()
        for equ_key in self.equement_type.keys():
            equement = self.equement_type[equ_key]
            for attr in self.all_attr_str:
                if equement:
                    if equement.__dict__[attr] != 0:
                        self.__dict__[attr] += equement.__dict__[attr]


    
    @property
    def info(self):
        self.eque_cal()
        for attr in self.all_attr_str:
            print(attr,":",self.__dict__[attr])
        


if __name__ == "__main__":
    #测试
    wyatthomg = Role("大枪",    
                strength_base = 0, #基础力量
                intellect_base = 0 , #基础智力
                brawn_base = 0 ,   #基础体力
                spirit_base  = 0, #基础精神
                phyAtkPower_base  = 0, #基础物理攻击力
                magicAtkPower_base  = 0, #基础魔法攻击力
                critnum_base  = 0, #基础暴击数值
                daekel_num  = 0, #基础火强
                mipha_num = 0, #基础冰强
                urbosa_num  = 0, #基础光强
                revali_num  = 0, #基础暗强
                hp_base  = 0, #基础生命值
                mp_base  = 0, #基础魔法值
                phydef_base  = 0, #基础物理防御
                magicdef_base  = 0, #基础魔法防御
                attack_speed_base  = 0,
                pushskill_speed_base  = 0,
                move_speed_base = 0)
    
    saliya = Pet_and_Equepment(eque_name= "Saliya",
                                eque_type="pet",
                                strengh = 237,
                                intelligent=237,
                                brawn=237,
                                sprit=237,
                                critrate=2,
                                mipha_num = 8, #冰强
                                daekel_num = 8, #火强
                                urbosa_num = 8,#光强
                                revali_num = 8,#暗强
                                extra_damage = 21 #白字
    )

    red_pet_eque = Pet_and_Equepment(eque_name="红宠装备",
                                    eque_type="red_pet",
                                      strengh = 78,
                                      intelligent=18,
                                      phyAtkPower = 11, #物理攻击力
                                      magicAtkPower = 11) #魔法攻击力

    blue_pet_eque = Pet_and_Equepment(eque_name="蓝宠装备",
                                    eque_type="blue_pet",
                                      attack_speed = 5,
                                      pushskill_speed=7.5,
                                      move_speed = 2.5,
                                      phyAtkPower = 60, 
                                      ) 

    green_pet_eque = Pet_and_Equepment(eque_name="绿宠装备",
                                    eque_type="green_pet",
                                      hp = 165,
                                      mipha_num = 14, #冰强
                                      daekel_num = 14, #火强
                                      urbosa_num = 14,#光强
                                      revali_num = 14,#暗强
                                      )

    three_pet_eque  = Pet_and_Equepment(eque_name="三宠装备",
                                        eque_type="three_pet",
                                      mipha_num = 5, #冰强
                                      daekel_num = 5, #火强
                                      urbosa_num = 5,#光强
                                      revali_num = 5,#暗强
                                      extra_damage = 3, #白字
                                      attack_speed = 3,
                                      pushskill_speed=3,
                                      move_speed = 3,
                                      )

    wyatthomg.add_equement(saliya)
    wyatthomg.add_equement(red_pet_eque)
    wyatthomg.add_equement(blue_pet_eque)
    wyatthomg.add_equement(green_pet_eque)
    wyatthomg.add_equement(three_pet_eque)
    wyatthomg.info



