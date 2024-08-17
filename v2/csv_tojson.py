import pandas as pd 
import json
from pathlib import Path
import numpy as np
equedb_file = Path(r"E:\python\dnfm\v2\equedb.csv")
eque_df = pd.read_csv(equedb_file)
# eque_df.to_json("equedb.json", orient="records", force_ascii=False, lines=True)
# eque_dfs=1
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