import hashlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class player:
    name = str
    md5 = str
    health = float
    power = float
    defence = float
    speed = float
    luck = float
    mana = float
    magic = float
    critical = float
    move = float
    hit_rate = float


player1 = player
player2 = player

print("플레이어1의 이름은 무엇입니까?")
player1.name = str(input("플레이어1의 이름은 무엇입니까? : "))
player2.name = str(input("플레이어2의 이름은 무엇입니까? : "))

player1.md5 = hashlib.md5(player1.name.encode()).hexdigest()
player2.md5 = hashlib.md5(player2.name.encode()).hexdigest()

player1.health = float(int(player1.md5[0]+player1.md5[1], 16))*500/255
player2.health = float(int(player2.md5[0]+player2.md5[1], 16))*100/255
player1.defence = float(int(player1.md5[2]+player1.md5[3], 16))*100/255
player2.defence = float(int(player2.md5[2]+player2.md5[3], 16))*100/255
player1.power = float(int(player1.md5[4]+player1.md5[5], 16))*100/255
player2.power = float(int(player2.md5[4]+player2.md5[5], 16))*100/255
player1.speed = float(int(player1.md5[6]+player1.md5[7], 16))*100/255
player2.speed = float(int(player2.md5[6]+player2.md5[7], 16))*100/255
player1.luck = float(int(player1.md5[8]+player1.md5[9], 16))*100/255
player2.luck = float(int(player2.md5[8]+player2.md5[9], 16))*100/255
player1.mana = float(int(player1.md5[10]+player1.md5[11], 16))*100/255
player2.mana = float(int(player2.md5[10]+player2.md5[11], 16))*100/255
player1.critical = float(int(player1.md5[12]+player1.md5[13], 16))*100/255
player2.critical = float(int(player2.md5[12]+player2.md5[13], 16))*100/255
player1.move = float(int(player1.md5[14]+player1.md5[15], 16))*100/255
player2.move = float(int(player2.md5[14]+player2.md5[15], 16))*100/255
player1.hit_rate = float(int(player1.md5[16]+player1.md5[17], 16))*100/255
player2.hit_rate = float(int(player2.md5[16]+player2.md5[17], 16))*100/255
player1.magic = float(int(player1.md5[18]+player1.md5[19], 16))*100/255
player2.magic = float(int(player2.md5[18]+player2.md5[19], 16))*100/255

print("      이름 : " + player1.name)
print("스텟 기본값 : " + player1.md5)
print("      체력 : " + str(player1.health))
print("      방어 : " + str(player1.defence))
print("        힘 : " + str(player1.power))
print("      회피 : " + str(player1.speed))
print("        운 : " + str(player1.luck))
print("      마나 : " + str(player1.mana))
print("      마법 : " + str(player1.magic))
print("   치명타율 : " + str(player1.critical))
print("     이동력 : " + str(player1.hit_rate))

df = pd.DataFrame(
    {'이름': [player1.name, player2.name]},
    {'스텟 기본값': [player1.md5, player2.md5]},
    {'체력': [player1.health, player2.health]},
    {'방어': [player1.defence, player2.defence]},
    {'힘': [player1.power, player2.power]},
    {'회피': [player1.speed, player2.speed]},
    {'운': [player1.luck, player2.luck]},
    {'마나': [player1.mana, player2.mana]},
    {'마법': [player1.magic, player2.magic]},
    {'치명타율': [player1.critical, player2.critical]},
    {'이동력': [player1.hit_rate, player2.hit_rate]}
)
