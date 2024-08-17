from model.equement import Pet_and_Equepment
from model.base import Role
from pathlib import Path
import json
euque_file = Path("eque.json")
with open(euque_file, "r", encoding="utf-8") as f:
    equedb_json = json.load(f)

wyatthomg = Role("大枪",    
                 level=70,
            strength_base = 0, #基础力量
            intellect_base = 0 , #基础智力
            brawn_base = 0 ,   #基础体力
            spirit_base  = 0, #基础精神
            phyAtkPower_base  = 1146, #基础物理攻击力
            magicAtkPower_base  = 1146, #基础魔法攻击力
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

kalix = Role("卡利克斯",    
                 level=80,
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
for item in equedb_json.keys():
    data = equedb_json[item][0]
    load_eque = Pet_and_Equepment()
    load_eque.load_from_dict(data)
    wyatthomg.add_equement(load_eque)

print(wyatthomg.attack(kalix))


