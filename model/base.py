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
from model.equement import Pet_and_Equepment

class Role(object):
    JOB_LIST = []
    def __init__(self,
                job,
                level,
                strength_base,#基础力量
                intellect_base, #基础智力
                brawn_base,   #基础体力
                spirit_base, #基础精神
                phyAtkPower_base, #基础物理攻击力
                magicAtkPower_base, #基础魔法攻击力
                critnum_base, #基础暴击数值
                daekel_num_base, #基础火强
                mipha_num_base, #基础冰强
                urbosa_num_base, #基础光强
                revali_num_base, #基础暗强
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
        self.level = level
        self.strength_base = strength_base #角色力量
        self.intellect_base = intellect_base #智力
        self.brawn_base = brawn_base #体力
        self.sprit_base = spirit_base #精神
        self.phyAtkPower_base = phyAtkPower_base #基础物理攻击力
        self.magicAtkPower_base = magicAtkPower_base #基础魔法攻击力
        self.critnum_base = critnum_base  #基础暴击数值
        self.daekel_num_base = daekel_num_base #火强属性值
        self.mipha_num_base = mipha_num_base #冰强属性值
        self.urbosa_num_base = urbosa_num_base #光强属性值
        self.revali_num_base = revali_num_base #暗强属性值
        self.hp_base = hp_base#基础生命值
        self.mp_base = mp_base #基础魔法值
        self.phydef_base = phydef_base #基础物理防御
        self.magicdef_base = magicdef_base #
        
        #三速
        self.attack_speed_base = attack_speed_base
        self.pushskill_speed_base = pushskill_speed_base
        self.move_speed_base = move_speed_base

        #伤害计算基本定义
        self.damage_increase = 1
        self.extra_damage = 1
        self.crit_damage_rate = 50 #暴击增伤比例
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

        self._type_dict = None
        # wyatthomg.add_equement(Saliya)
        self.attr_init()
    def attr_init(self):
      self.strengh = self.strength_base
      self.intelligent = self.intellect_base
      self.brawn = self.brawn_base
      self.sprit = self.sprit_base
      self.phydef = 0
      self.magicdef = 0
      self.hp = 0
      self.mp = 0
      self.phyAtkPower = self.phyAtkPower_base
      self.magicAtkPower = self.magicAtkPower_base
      self.critum = self.critnum_base
      self.critrate = 3
      self.cri_damage = 50

      self.damage_increase = 0
      self.extra_damage = 0
      self.skill_attk = 0

      self.mipha_num = self.mipha_num_base
      self.daekel_num = self.daekel_num_base 
      self.urbosa_num = self.urbosa_num_base
      self.revail_num = self.revali_num_base 

      self.strengh_increase_rate = 0
      self.intelligent_increase_rate = 0
      self.brawn_increase_rate = 0
      self.sprit_increase_rate = 0
      self.phyatk_increase_rate = 0
      self.magicatk_increase_rate = 0
      self.shield = 0

      self.attack_speed = self.attack_speed_base
      self.pushskill_speed= self.pushskill_speed_base
      self.move_speed = self.move_speed_base 
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
        
    def pannel_value(self):
        self.pannel_strengh = self.strengh * (1 + self.strengh_increase_rate* 0.01) #最终力量
        self.pannel_intelligent = self.intelligent * (1 + self.intelligent_increase_rate * 0.01) #最终智力
        self.pannel_brawn = self.brawn #体力
        self.pannel_sprit = self.sprit #精神
        self.pannel_phyATK = self.phyAtkPower * (1 + self.phyatk_increase_rate * 0.01) * (self.pannel_strengh * 0.004 + 1)
        self.pannel_magicATK = self.magicAtkPower * (1 + self.magicatk_increase_rate * 0.01) * (self.pannel_intelligent *0.004 + 1)
        self.pannel_phydef= self.phydef + self.pannel_brawn * 5
        self.pannel_magicdef= self.magicdef + self.pannel_sprit * 5
        self.pannel_hp = self.hp * (1+ self.pannel_brawn * 0.004)
        self.pannel_mp = self.mp * (1+ self.pannel_sprit * 0.004)
       
         

    def attack(self,otherRole):
         self.pannel_value()
         crit_unit = 3.75*1.25**(round(otherRole.level/8,2))
         self.pannel_critrate = self.critrate + (self.critum + self.critnum_base) /crit_unit
         damage = self.pannel_phyATK *  (1 + self.damage_increase * 0.01) * \
                                        (1 + self.extra_damage * 0.01+ (self.element_extra_damage * 0.01 * (1.05 + self.mipha_num/220))) * \
                                        ((1 + self.cri_damage * 0.01) * min(100,self.pannel_critrate)/100 + (1 -  min(100,self.pannel_critrate)/100 )) *\
                                        (1.05 + self.mipha_num/220)
         
         return damage 


if __name__ == "__main__":
    #测试
    pass
 
