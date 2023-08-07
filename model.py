# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:44:58 2023

    
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
t1 = time.time()
excelname = 'basedb.xlsx'
equipdb = pandas.read_excel(excelname, sheet_name='BaseDb')

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
                        
        
df = loading_equip()           