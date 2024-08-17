import pandas as pd 
import json
from pathlib import Path
import numpy as np
from collections import defaultdict
###########装备部分###################
equedb_file = Path("data\equedb.csv")
eque_df = pd.read_csv(equedb_file)
eque_dict ={}
for idx,row in eque_df.iterrows():
    if row['eque_type']  not in eque_dict.keys():
          eque_dict[row["eque_type"]] = []
    temp_dict = row.to_dict()
    keys = list(temp_dict.keys())
    for item in keys:
        if item in ["eque_type","equement_name","job"]:
            continue
        try:
            if np.isnan(temp_dict[item])  :
                temp_dict.pop(item) 
        except:
            if temp_dict[item] ==0 :
                temp_dict.pop(item) 
                continue
            else:
                temp_dict[item] =float(temp_dict[item])

       


    eque_dict[row["eque_type"]].append(temp_dict)

with open('eque.json', 'w', encoding='utf-8') as f:
    json.dump(eque_dict, f, ensure_ascii=False)

##########技能部分##################3
skilldb_file = Path("data\skilldb.csv") 
skilldf = pd.read_csv(skilldb_file)
skill_dict ={}
for idx,row in skilldf.iterrows():
    temp_dict = row.to_dict()
    temp_dict['upgrade_increase'] = json.loads(temp_dict['upgrade_increase'])
    keys = list(temp_dict.keys())
    if skill_dict.get(row['job']) == None :
       skill_dict[row['job']]=   defaultdict(dict)  
    if skill_dict[row['job']].get(row['learn_level']) == None :
       skill_dict[row['job']][row['learn_level']] = {}
    temp_dict.pop('job')
    temp_dict.pop('learn_level')
    skill_name = row['skill_name']
    temp_dict.pop('skill_name') 
    skill_dict[row['job']][row['learn_level']][row['skill_name']] = temp_dict


with open('skill.json', 'w', encoding='utf-8') as f:
    json.dump(skill_dict, f, ensure_ascii=False)


##########符文部分##################3
runes_file = Path(r"data\runes.csv") 
runesdf = pd.read_csv(runes_file)
rune_dict ={}
for idx,row in runesdf.iterrows():

    temp_dict = row.to_dict()
    name = temp_dict['fune_name']
    temp_dict.pop('fune_name')
    rune_dict[name] = temp_dict

with open('rune.json', 'w', encoding='utf-8') as f:
    json.dump(rune_dict, f, ensure_ascii=False)