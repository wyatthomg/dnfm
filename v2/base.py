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
import pandas 
import numpy as np
import math
import time 
import random
from skillmodel import Character

class Role(object):
    def __init__(self,
                strength_base,
                intellect_base,
                brawn_base,   
                spirit_base,
                phyAtkPower_base,
                magicAtkPower_base,
                critnum_base,
                daekel_num,
                mipha_num,
                urbosa_num,
                revali_num,
                hp_base ,
                mp_base ,
                ):
        #魔力结晶和公会的现在算作基础，脱妆抄数据就好
        self.job = "大枪"# job类后面映射到Skill Model获取被动过和技能明细  
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

        #伤害计算基本定义
        self.damage_increase = 1
        self.extra_damage = 0
        self.crit_damage_rate = 0.5 #暴击增伤比例
        self.critrate = 0.03 #基础暴击率
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

    def add_pet(self,petobj):
        

class Pet_and_Equepment(object):
    #宠物本身当做一个装备来处就好了
    def __init__(self,name,level,strength,intellect,brawn,spirit,hp,mp,critnum,critrate,damage_increase,extra_damage,skill_attk):
        self.name = name
        self.level = level
        self.strength = strength
        self.intellect = intellect
        self.brawn = brawn
        self.spirit = spirit

