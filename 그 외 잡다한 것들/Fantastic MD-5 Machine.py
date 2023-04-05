import hashlib


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

player1.health = float(int(player1.md5[0]+player1.md5[1], 16))
player2.health = float(int(player2.md5[0]+player2.md5[1], 16))
player1.defence = float(int(player1.md5[2]+player1.md5[3], 16))
player2.defence = float(int(player2.md5[2]+player2.md5[3], 16))
player1.power = float(int(player1.md5[4]+player1.md5[5], 16))
player2.power = float(int(player2.md5[4]+player2.md5[5], 16))
player1.speed = float(int(player1.md5[6]+player1.md5[7], 16))
player2.speed = float(int(player2.md5[6]+player2.md5[7], 16))
player1.luck = float(int(player1.md5[8]+player1.md5[9], 16))
player2.luck = float(int(player2.md5[8]+player2.md5[9], 16))
player1.mana = float(int(player1.md5[10]+player1.md5[11], 16))
player2.mana = float(int(player2.md5[10]+player2.md5[11], 16))
player1.critical = float(int(player1.md5[12]+player1.md5[13], 16))
player2.critical = float(int(player2.md5[12]+player2.md5[13], 16))
player1.move = float(int(player1.md5[14]+player1.md5[15], 16))
player2.move = float(int(player2.md5[14]+player2.md5[15], 16))
player1.hit_rate = float(int(player1.md5[16]+player1.md5[17], 16))
player2.hit_rate = float(int(player2.md5[16]+player2.md5[17], 16))
player1.magic = float(int(player1.md5[18]+player1.md5[19], 16))
player2.magic = float(int(player2.md5[18]+player2.md5[19], 16))

print(player1.name)
print(player1.md5)
print(player1.health)
print(player1.defence)
print(player1.power)
print(player1.speed)
print(player1.luck)
print(player1.mana)
print(player1.magic)
print(player1.critical)
print(player1.move)
print(player1.hit_rate)
