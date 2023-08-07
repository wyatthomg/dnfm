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
from skillmodel import Character
DAQIANG = Character('狂暴者')
t1 = time.time()
excelname = 'basedb.xlsx'
equipdb = pandas.read_excel(excelname, sheet_name='BaseDb')
equipdb= equipdb[equipdb['suit_name'].isin(['牛角4级', '属强套', '手炮','鬼面君主套','镇魂曲套'])]
equipdb= equipdb[~equipdb['name'].isin(['铁甲炮', '卸甲炮'])]
equipdb = equipdb.fillna(0)
def loading_equip(weapon_type=['手炮'],isozima=False):
    resultdf = pandas.DataFrame()
    weapon_list =  set(equipdb[equipdb['suit_name'].isin(weapon_type)]['name'])
    armorlist = set(equipdb['suit_name'].where(equipdb['location']=='五件套效果'))
    armorlist = {item for item in armorlist if isinstance(item, str)}
    jewelrylist = set(equipdb['suit_name'].where(equipdb['location']=='首饰三件套效果'))
    jewelrylist = {item for item in jewelrylist if isinstance(item, str)}
    stonelist = set(equipdb[equipdb['location'] == '左槽']['name'])
    for weapon in weapon_list:
        for stone in stonelist:
            for jewelry in jewelrylist:
                for armor in armorlist:
                    tse = pandas.Series(dtype=object)
                    tse['武器'] = weapon
                    tse['武器类型'] =  equipdb[(equipdb['name'] == weapon)]['suit_name'].values[0]
                    tse['左槽'] = stone
                    tse['防具三件套效果'] =  equipdb[(equipdb['suit_name'] == armor) & (equipdb['location'] == '防具三件套效果')]['name'].values[0]
                    tse['五件套效果'] =  equipdb[(equipdb['suit_name'] == armor) & (equipdb['location'] == '五件套效果')]['name'].values[0]
                    tse['首饰三件套效果'] =  equipdb[(equipdb['suit_name'] == jewelry) & (equipdb['location'] == '首饰三件套效果')]['name'].values[0]
                    for loc in ['上衣','下装','护肩','腰带','鞋子']:
                        tse[loc] = equipdb[(equipdb['suit_name'] == armor) & (equipdb['location'] == loc)]['name'].values[0]
                    for loc in ['手镯','项链','戒指']:
                        tse[loc] = equipdb[(equipdb['suit_name'] == jewelry) & (equipdb['location'] == loc)]['name'].values[0]
                    tdf = tse.to_frame().T
                    resultdf = pandas.concat([resultdf,tdf],ignore_index=True)
    return resultdf
                        
        
                    


def runcal(row,have_ele=1,eat='手炮'):
    levelcretiaRate=25.3 #暴击换算系数
    base_lizhi = 1681 #角色基础力智
    base_shuanggong = 180 #基础双攻
    base_duli =  343 #独立攻击,后面懒得管了
    base_critalRate = 0.28 #基础暴击,加上了技能暴击
    base_critalvalue = 327 #基础暴击值
    base_critalDammage = 1.7 #爆伤
    base_element = 47 #属强
 
    base_skill_attk = 0.11 #60技工
    
    lizhi_Rate = 0 #力智系数
    shuanggong_Rate = 0.05
    extra_attk_pet = 0.24 #宠物白字，赛利亚+最强装备，21+3
    
    equip_lizhi = 1910 #60装备提供的力智，但是65似乎高一点
    equip_shuanggong = 1789#同上
    equip_elememt= 158#其他地方堆得属强
    equip_critalvalue = 700#暴击
    equip_upscale_attk = 0.21 #称号和 6黄词条
    skill_skill_attak = 0.12 if row['武器类型'] == eat else 0 #如果带手炮就来12技工
    
    #初始化一下参数
    resutl_lizhi = equip_lizhi + base_lizhi
    resutl_shuanggong = base_shuanggong + equip_shuanggong
    result_skill_attk = base_skill_attk + skill_skill_attak
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
    context =""
    for loca in ['武器','左槽','防具三件套效果', 
                 '五件套效果' , '首饰三件套效果',  
                 '上衣',    '下装',    '护肩',
                 '腰带','鞋子' , '手镯', '项链', '戒指' ]:
        #根据装备类型换算过程，dddd，我先算一个技工。啊哈啊哈
        equip_attr =  equipdb[equipdb['name']==row[loca]].iloc[0,4:].fillna(0)
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
        context +=loca+":"+ str(equip_attr['备注描述'])+"\n"
        baozhu  = 0.05 if have_ele >=1 else 0 #角色自带，或者装备有属强，我就默认上一个宝珠5%
    final_lizhi = resutl_lizhi * (1+lizhi_Rate)
    final_mianban = resutl_shuanggong*(1 + shuanggong_Rate)*(1+final_lizhi/250)
    final_baizi = result_extra_attk_ele*(1+result_ele/220) + result_extra_attk + result_extra_attk_abnormal+1
    final_huangzi = result_upscale_attk_ele*(1+result_ele/220) +result_upscale_attk + baozhu +1
    final_critalRate = result_critalRate + result_critalvalue / levelcretiaRate/100
    final_crital_mexp = final_critalRate * result_critalDammage + (1-final_critalRate)
    final_skill_attak = result_skill_attk + eque_skill_attk
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
    row['最终爆伤'] = result_critalDammage
    row['最终暴击期望'] = final_crital_mexp
    row['最终强度'] = final_attack
    row['备注描述'] = context
    return row
 
# main
#还要改很多，但是懒得
df = loading_equip()
tdf = df.apply(runcal, axis=1)
# df.to_csv('排名结果.csv', index=False)
print(time.time()-t1)




def set_dict(name,cd,damagep,level,increase_per_level,increase_type):
    if level >1:
        if increase_type ==0:
            damagep  =damagep *(1+increase_per_level)**(level-1)
        if increase_type ==1:
            damagep  =damagep + increase_per_level*(level-1)
    return {'name':name,
            'cd':cd,
            'damagep':damagep,
            'level':level,
            'increase_per_level':increase_per_level,
            'increase_type':increase_type
        }
import math
def skill_attr():
    skill_dict ={}
    skill_dict['level15']=set_dict("15级技能", 5, 3372, 1, 0.026, 0)
    skill_dict['level152']=set_dict("15级技能2", 5, 2372, 1, 0.026, 0)
    skill_dict['level25']=set_dict("25级技能", 7, 4379, 1, 0.026, 0)
    skill_dict['level30']=set_dict("30级技能", 10, 6919, 1, 0.028, 0)
    skill_dict['level35']=set_dict("35级技能", 20, 11016, 1, 0.03, 0)
    skill_dict['level40']=set_dict("40级技能", 20, 6919, 1, 0.03, 0)
    skill_dict['level45']=set_dict("45级技能", 40, 16482, 3, 0.045, 0)
    skill_dict['level50']=set_dict("50级技能", 145, 50190, 2, 5389, 1)
    skill_dict['level65']=set_dict("65级技能", 40, 11353, 2, 0.045, 0)
    skill_dict['level70']=set_dict("70级技能", 40, 9980, 2, 0.045, 0)
    return skill_dict
    
def skill_attr2():
    skill_dict ={}
    skill_dict['level15']=set_dict("15级技能", 4.5, 3372, 1, 0.026, 0)
    skill_dict['level152']=set_dict("15级技能2", 4.5, 2372, 1, 0.026, 0)
    skill_dict['level25']=set_dict("25级技能", 6.3, 4379, 4, 0.026, 0)
    skill_dict['level30']=set_dict("30级技能", 9, 6919, 4, 0.028, 0)
    skill_dict['level35']=set_dict("35级技能", 18, 11016, 4, 0.03, 0)
    skill_dict['level40']=set_dict("40级技能", 18, 6919, 4, 0.03, 0)
    skill_dict['level45']=set_dict("45级技能", 36, 16482, 5, 0.045, 0)
    skill_dict['level50']=set_dict("50级技能", 130, 50190, 1, 5389, 1)
    skill_dict['level65']=set_dict("65级技能", 36, 11353, 1, 0.045, 0)
    skill_dict['level70']=set_dict("70级技能", 36, 9980, 1, 0.045, 0)
    return skill_dict
import random
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
def mpt(df,second):
    skill_dict = skill_attr()
    reuslt= {'damage':0,'second':second}
    base_damage = int(df['最终强度']/100)
    for key in skill_dict:
        attack_times =math.floor( second/ (skill_dict[key]['cd'] +0.4)) +1
        skill_damage = attack_times*skill_dict[key]['damagep']/100*base_damage
        reuslt['damage'] += skill_damage
    return reuslt

def zht(df,second):
    skill_dict = skill_attr2()
    reuslt= {'damage':0,'second':second,'context':''}
    base_damage = int(df['最终强度']/100)
    for key in skill_dict:
        attack_times =math.floor( second/ (skill_dict[key]['cd'] + 0.4)) +1
        if any(value in skill_dict[key]['name']  for value in ['25','30','35','40','45','65'] ):
            use =1
        else:
            use =0
        finaly_times = zh_random(attack_times,skill_dict[key]['name'],use)
   
        skill_damage = finaly_times['finaly_time']*skill_dict[key]['damagep']/100*base_damage
        reuslt['damage'] += skill_damage
        if use ==1:
            reuslt['context'] +=finaly_times['name'] + str(finaly_times['extra_time']) +'次; '
    return reuslt

def zlt(df,second):
    skill_dict = skill_attr2()
    reuslt= {'damage':0,'second':second,'context':''}
    base_damage = int(df['最终强度']/100)
    for key in skill_dict:
        attack_times =math.floor( second/ (skill_dict[key]['cd'] + 0.4)) +1
        if any(value in skill_dict[key]['name']  for value in ['25','30','35','40','45','65'] ):
            use =1
        else:
            use =0
        finaly_times = zh_random(attack_times,skill_dict[key]['name'],use)
   
        skill_damage = finaly_times['finaly_time']*skill_dict[key]['damagep']/100*base_damage
        reuslt['damage'] += skill_damage
        if use ==1:
            reuslt['context'] +=finaly_times['name'] + str(finaly_times['extra_time']) +'次; '
    return reuslt
mptao = mpt(tdf.iloc[0],60)
zhenhuntao = zht(tdf.iloc[1],60)
# zhenlitao = zlt(tdf.iloc[2],120)
























# # 技能列表，每个元素代表一个技能的CD时间（秒）
# skills = [10, 15, 20, 30]

# # 初始化技能CD字典，key为技能索引，value为CD时间（秒）
# skill_cds = {i: skill for i, skill in enumerate(skills)}

# def release_skill(skill_index):
#     # 模拟释放技能
#     print(f"释放技能 {skill_index + 1}")
#     skill_cds[skill_index] = skills[skill_index]  # 技能释放后重置CD

# def clock_tick():
#     # 每秒钟的操作
#     for i in range(1, 121):
#         print(f"第 {i} 秒")
#         for skill_index in sorted(skill_cds.keys(), reverse=True):
#             if skill_cds[skill_index] == 0:
#                 release_skill(skill_index)
#                 # 释放技能后有0.2的概率重置其他技能的CD
#                 if random.random() < 0.2:
#                     reset_skill_index = random.choice(list(skill_cds.keys()))
#                     skill_cds[reset_skill_index] = skills[reset_skill_index]
#             skill_cds[skill_index] -= 1
#         time.sleep(1)

# clock_tick()










    
    