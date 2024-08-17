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

def loading_equip():
    resultdf = pandas.DataFrame()
    armorlist = set(equipdb['套装名称'].where(equipdb['装备类型']=='五件套效果'))
    armorlist = {item for item in armorlist if isinstance(item, str)}
    jewelrylist = set(equipdb['套装名称'].where(equipdb['装备类型']=='首饰三件套效果'))
    jewelrylist = {item for item in jewelrylist if isinstance(item, str)}
    stonelist = set(equipdb[equipdb['装备类型'] == '左槽']['装备名称'])
    for stone in stonelist:
        for jewelry in jewelrylist:
            for armor in armorlist:
                tse = pandas.Series(dtype=object)
                tse['左槽'] = stone
                tse['防具三件套效果'] =  equipdb[(equipdb['套装名称'] == armor) & (equipdb['装备类型'] == '防具三件套效果')]['装备名称'].values[0]
                tse['五件套效果'] =  equipdb[(equipdb['套装名称'] == armor) & (equipdb['装备类型'] == '五件套效果')]['装备名称'].values[0]
                tse['首饰三件套效果'] =  equipdb[(equipdb['套装名称'] == jewelry) & (equipdb['装备类型'] == '首饰三件套效果')]['装备名称'].values[0]
                for loc in ['上衣','下装','护肩','腰带','鞋子']:
                    tse[loc] = equipdb[(equipdb['套装名称'] == armor) & (equipdb['装备类型'] == loc)]['装备名称'].values[0]
                for loc in ['手镯','项链','戒指']:
                    tse[loc] = equipdb[(equipdb['套装名称'] == jewelry) & (equipdb['装备类型'] == loc)]['装备名称'].values[0]
                tdf = tse.to_frame().T
                resultdf = pandas.concat([resultdf,tdf],ignore_index=True)
    return resultdf
                        
def pretraversal():
    df = loading_equip()     
    df.to_csv('预加载.csv', index=False)    
pretraversal()