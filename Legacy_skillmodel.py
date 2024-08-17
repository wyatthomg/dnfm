# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 20:40:21 2023

    
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
import pandas as pd 

skilldf= pd.read_csv('skill.csv')

class Skill(object):
    def __init__(self, 
                  name, 
                  required_level,
                  skill_type,
                  skill_base_level,
                  base_damage,
                  add_damage_type,
                  add_damage_rate,
                  cd,
                  show_time,
                  tplevel = 0,
                  extra_level=0,
                  **kwargs
        
      ):
        self.name = name #技能名称
        self.required_level = required_level #最低学习等级，装备增加的时候用得上
        self.skill_type = skill_type #主动和被动
        self.base_damage = base_damage #基础伤害
        self.skill_base_level =skill_base_level #基本等级，都写1，只是为了看装备增加多少级
        self.add_damage_type = add_damage_type #增加类型，以前以为有乘算，估计要去掉
        self.add_damage_rate = add_damage_rate #增加的伤害数
        self.cd = cd #cd数值
        self.show_time = show_time
        self.tplevel = tplevel #TP等级
        self.extra_level = extra_level #额外等级

        #用来处理遇到的非伤害词条如何增加的方法
        self.skill_other_item = kwargs.get('skill_other_item')
        self.skill_other_item_rate = kwargs.get('skill_other_item_rate')

        #爆伤暴击技工黄字
        self.skill_critalDammage = kwargs.get('skill_critalDammage')
        self.skill_critalRate = kwargs.get('skill_critalRate')
        self.skill_upscale_attk = kwargs.get('skill_upscale_attk')
        self.skilled_skill_attk = kwargs.get('skilled_skill_attk')

        #这里不应该有两个dict，1个就可以了,以后再改
        self.kdict ={"伤害增加":self.skill_upscale_attk ,
                     '技能技工':self.skilled_skill_attk ,
                     '暴击率': self.skill_critalRate ,
                     '爆伤' :self.skill_critalDammage ,
            }
        self.tdict ={"伤害增加":self.skill_upscale_attk ,
                     '技能技工':self.skilled_skill_attk ,
                     '暴击率': self.skill_critalRate ,
                     '爆伤' :self.skill_critalDammage ,
            }
        self.decrease_cd = 0  #比例CD
        self.decrease_num_cd = 0  #固定CD
        self.extra_damage_rate = 0 #技能增伤 比如铁甲炮，

    def add_level(self,num):
        self.extra_level += num
        
    def add_tp_level(self,num):
        if self.tplevel >=1 :
            self.tplevel += num
        
    def extra_damage_rate_add(self,num):
        self.extra_damage_rate  +=num
        
    def decrease_cdrate(self, num):
        self.decrease_cd += num

    def decrease_cdnum(self, num):
        self.decrease_num_cd += num
        
    @property
    def tp_rate(self):
        if self.tplevel ==0:
            return 0
        if self.tplevel  ==1: 
            return 0.08
        else:
            return self.tplevel *0.03 + 0.05
    @property
    def skill_cd(self):
        return self.cd  * (1-self.decrease_cd) - self.decrease_num_cd
    @property
    def final_damage(self):
        finial_damge = self.base_damage +  self.add_damage_rate * self.extra_level
        return float(finial_damge/100) *(1 +  self.tp_rate)*(1+ self.extra_damage_rate)
    
    @property
    def effect(self):
        item_list = eval(self.skill_other_item)
        item_rate_list = eval(self.skill_other_item_rate)
        for idx in range(len(item_list)):
            self.tdict[item_list[idx]] = self.kdict[item_list[idx]] + self.extra_level * item_rate_list[idx]
        return self.tdict
   
    def __repr__(self):
        return self.name
    





class Character(object):
    def __init__(self, name):
        self.name = name
        self.skills = []
        self.skill_tb =  skilldf[(skilldf['角色名称'] == name)]
        #从 skill.csv加载技能
        self.load_skill()

    def load_skill(self):
        for idx,row in self.skill_tb.iterrows():
            skill = Skill(name = row['名称'],
                          required_level = int(row['技能学习等级']),
                          skill_type = row['技能类型'],
                          base_damage = row['伤害值'],
                          skill_base_level = row['基本等级'],
                          add_damage_type = row['提升方式'],
                          add_damage_rate = row['每等级提升伤害'],
                          tplevel = row['TP等级'],
                          cd =  row['CD'],
                          show_time = row['演出时间']，
                          skill_critalDammage = row['爆伤'],
                          skill_critalRate = row['暴击率'],
                          skill_upscale_attk = row['伤害增加'],
                          skilled_skill_attk = row['技能技工'],
                          skill_other_item = row['提升项目'],
                          skill_other_item_rate = row['其他项目每等级提升'],
                        
                                               )
            
            self.skills.append(skill)


    @property
    def skill(self):
        return self.skills
    #两个基本的查找技能方法
    def find_skill_by_level(self, min_level):
        filtered_skills = [skill for skill in self.skills if skill.required_level == min_level]
        return filtered_skills
    def find_skill_by_name(self, skill_name):
        for skill in self.skills:
            if skill.name == skill_name:
                return skill
        return None
    #镇魂套专用的25-45技能列表，其他的不用
    def zht_skill(self):
        filtered_skills = [skill for skill in self.skills if skill.required_level >= 25 and skill.required_level <=45 and skill.skill_type == '主动']
        filtered_skills.append(skill for skill in self.skills if skill.required_level == 65 and skill.skill_type == '主动')
        return filtered_skills
    
    def find_passive_skill(self):
        filtered_skills = [skill for skill in self.skills if skill.skill_type == '被动']
        return filtered_skills
    def find_activate_skill(self):
        filtered_skills = [skill for skill in self.skills if skill.skill_type == '主动']
        return filtered_skills
    
    #技能如果是非伤害词条如何处理
    def find_passive_skill_effect(self):
        kdict = {'伤害增加': 0.0, '技能技工': 0, '暴击率': 0.0, '爆伤': 0.0} 
     
        for item in self.find_passive_skill():
            for key in item.effect:
                # 如果键在两个字典中都存在，则将对应的值相加并存储到结果字典中
                if key in kdict:
                    kdict[key] +=  item.effect[key] 
    
        return kdict
    
 
    #加技能等级四种方法
    def add_skill_level_by_name(self,name,num):
        skill = self.find_skill_by_name(name)
        skill.add_level(num)
        
    def add_skill_level_by_level(self,min_level,num):
        filtered_skills = self.find_skill_by_level(min_level)
        for skill in filtered_skills:
            skill.add_level(num)
   
    def add_skill_level_by_level_range(self,minL,maxL,num):
        for level in range(minL,maxL+1,5):
            filtered_skills = self.find_skill_by_level(level)
            for skill in filtered_skills:
                skill.add_level(num)
    
    def add_skill_tp_by_level_range(self,minL,maxL,num):
        for level in range(minL,maxL+1,5):
            filtered_skills = self.find_skill_by_level(level)
            for skill in filtered_skills:
                skill.add_tp_level(num)
# DAQIANG = Character('狂暴者')
# print(DAQIANG.find_passive_skill_effect())
# # print(DAQIANG.find_skill_by_name('反坦克炮').final_damage)
# DAQIANG.add_skill_level_by_name('压缩炮',1)
# print(DAQIANG.find_passive_skill_effect())
# DAQIANG.add_skill_level_by_level(50,1)
# print(DAQIANG.find_passive_skill_effect())
# DAQIANG.find_skill_by_name('BUFF').effect