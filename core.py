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

t1 = time.time()
excelname = 'basedb.xlsx'
equipdb = pandas.read_excel(excelname, sheet_name='BaseDb')
predf = pandas.read_csv('预加载.csv')

def loading_equip(predf,weapon_type=['手炮','步枪']):
    resultdf = pandas.DataFrame()
    weapon_list =  set(equipdb[equipdb['套装名称'].isin(weapon_type)]['装备名称'])
    for weapon in weapon_list:
        predf['武器'] = weapon
        predf['武器类型'] =  equipdb[(equipdb['装备名称'] == weapon)]['套装名称'].values[0]
        resultdf = pandas.concat([resultdf,predf],ignore_index=True)
    return resultdf
                        
  ##########下面三个是用来模拟打桩用的  ######    
  #普通套装打桩计算
def mpt(skill_list,base_damage):
    reuslt = 0
    for key in  skill_list:
        attack_times =math.floor( 60/ (key.skill_cd +key.show_time)) +1
        skill_damage = attack_times*base_damage*key.final_damage
        reuslt += skill_damage
    return reuslt

def zh_random(rawtime,name,use):
    finaly_time = rawtime
    if use ==1:
        for i in range(1,rawtime+1):
            k = random.randint(1, 1000)
            if k<=500:
                finaly_time +=1
            else:
                pass
    return {'finaly_time':finaly_time,'extra_time':finaly_time-rawtime,"name":name}

#镇魂套打桩计算
def zht(skill_list,extra_skill,base_damage):
    reuslt= 0
    for i in range(100):
        for key in skill_list:
            attack_times =math.floor( 60/ (key.skill_cd + key.show_time))) +1
            if key in extra_skill:
                use =1
            else:
                use =0
            finaly_times = zh_random(attack_times,key.name,use)
            skill_damage = finaly_times['finaly_time']*key.final_damage*base_damage
            reuslt += skill_damage
    return reuslt/100           
################

def runcal(row,have_ele=1):
    Role = Character('狂暴者')
    levelcretiaRate=26.7 #暴击换算系数
    base_lizhi = 1681 #角色基础力智
    base_shuanggong = 180 + 1000 #基础双攻 + 突破囤一堆
    base_duli =  343 #独立攻击,后面懒得管了
    base_critalRate = 0.03 #基础暴击
    base_critalvalue = 327 #基础暴击值
    base_critalDammage = 1.5 #爆伤
    base_element = 47 #属强
 
    base_skill_attk = 0 #60技工
    
    lizhi_Rate = 0 #力智系数
    shuanggong_Rate = 0.05
    extra_attk_pet = 0.24 #宠物白字，赛利亚+最强装备，21+3
    
    equip_lizhi = 1910 #60装备提供的力智，但是65似乎高一点
    equip_shuanggong = 1789#同上
    equip_elememt= 158#其他地方堆得属强
    equip_critalvalue = 700#暴击
    equip_upscale_attk = 0.22 #称号和 7黄词条

    
    #初始化一下参数
    resutl_lizhi = equip_lizhi + base_lizhi
    resutl_shuanggong = base_shuanggong + equip_shuanggong
    result_skill_attk = base_skill_attk 
    result_extra_attk = extra_attk_pet
    result_upscale_attk = equip_upscale_attk
    result_ele = base_element + equip_elememt
    result_critalRate = base_critalRate
    result_critalvalue = base_critalvalue +equip_critalvalue
    result_critalDammage = base_critalDammage
    result_extra_attk_ele = 0
    result_upscale_attk_ele = 0
    reduce_diffence = 0
    eque_skill_attk =1
    result_extra_attk_abnormal = 0
    have_ele = have_ele
    # context =""

    for loca in ['武器','左槽','防具三件套效果', 
                 '五件套效果' , '首饰三件套效果',  
                 '上衣',    '下装',    '护肩',
                 '腰带','鞋子' , '手镯', '项链', '戒指' ]:
        #根据装备类型换算过程，dddd，我先算一个技工。啊哈啊哈
        try:
            equip_attr =  equipdb[equipdb['装备名称']==row[loca]].iloc[0,3:].fillna(0)
        except:
            pass
        try:
            if equip_attr['eval'] ==0:
                pass
            else:
                eval_list = eval(equip_attr['eval'])
                for el in eval_list:
                    if el == "Role.find_skill_by_name('反坦克炮').extra_damage_rate(0.25)":
                        print(eval_list)
                        pass
               
                    eval(el)
        except Exception as e :
            print(eval_list,e)
            pass

        
        eque_skill_attk *= (1+equip_attr['技能攻击力'])
        
        result_extra_attk += equip_attr['附加伤害']
        result_upscale_attk += equip_attr['伤害增加']
        lizhi_Rate += equip_attr['力智系数']
        shuanggong_Rate += equip_attr['双攻系数']
      
        result_ele += equip_attr['属强']
        result_critalRate += equip_attr['暴击率']
        result_critalvalue += equip_attr['暴击值']
        result_critalDammage += equip_attr['爆伤'] 
        result_extra_attk_ele += equip_attr['属性附加伤害']
        result_upscale_attk_ele += equip_attr['属性伤害增加']
        result_extra_attk_abnormal += equip_attr['异常附加伤害']
        reduce_diffence += equip_attr['减防增伤']
        resutl_lizhi += equip_attr['额外基础力智']
        resutl_shuanggong +=  equip_attr['额外基础物攻']
        have_ele += equip_attr['是否有属性攻击']
        # context +=loca+":"+ str(equip_attr['备注描述'])+"\n"
        baozhu  = 0.05 if have_ele >=1 else 0 #角色自带，或者装备有属强，我就默认上一个宝珠5%
        
        
    role_dict = Role.find_passive_skill_effect()
    final_lizhi = resutl_lizhi * (1+lizhi_Rate)
    final_mianban =( base_duli+resutl_shuanggong)*(1 + shuanggong_Rate)*(1+final_lizhi/250)
    final_baizi = result_extra_attk_ele*(1+result_ele/220) + result_extra_attk + result_extra_attk_abnormal+1
    final_huangzi = result_upscale_attk_ele*(1+result_ele/220) +result_upscale_attk + baozhu +1 + role_dict['伤害增加']
    final_critalRate = result_critalRate + result_critalvalue / levelcretiaRate/100 +  role_dict['暴击率']
    final_critalDammage= result_critalDammage + role_dict['爆伤']
    final_crital_mexp = final_critalRate * final_critalDammage + (1-final_critalRate)
    final_skill_attak = result_skill_attk + eque_skill_attk  + role_dict['技能技工']
    final_attack = final_mianban * final_baizi *final_huangzi *final_crital_mexp *(1+result_ele/220) * final_skill_attak
    row['最终力智'] = final_lizhi
    row['最终力智系数'] = 1+lizhi_Rate
    row['最终双攻系数'] =  1 + shuanggong_Rate
    row['最终面板'] = final_mianban
    row['最终白字'] = final_baizi
    row['最终黄字'] = final_huangzi
    row['最终属强'] = result_ele
    row['最终技工'] = final_skill_attak
    row['装备技工'] = eque_skill_attk
    row['最终暴击率'] = final_critalRate
    row['最终爆伤'] = final_critalDammage
    row['最终暴击期望'] = final_crital_mexp
    row['最终强度'] = final_attack
    # row['备注描述'] = context
    Role.find_activate_skill()
    if "镇魂曲" in row['防具三件套效果']:
        row['damage'] =  zht( Role.find_activate_skill(), Role.zht_skill(), row['最终强度'])
    else : 
        row['damage'] =  mpt( Role.find_activate_skill(),  row['最终强度'])
    # row['ftk'] = Role.find_skill_by_name('反坦克炮').final_damage
    # row['decrease_num_cd'] = Role.find_skill_by_name('觉醒').final_damage
    # row['ysp'] = Role.find_skill_by_name('压缩炮').final_damage
    return row

# main
#还要改很多，但是懒得
df = loading_equip(predf)
tdf = df.apply(runcal, axis=1)
tdf = tdf.sort_values(by='damage', ascending=False)
tdf.to_csv('排名结果.csv')
    
    
    