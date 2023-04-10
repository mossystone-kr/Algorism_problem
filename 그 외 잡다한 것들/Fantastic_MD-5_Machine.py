import hashlib
import time
import os
import random as rd


magics = [
    "화염 발사",            #
    "마나 회복",
    "체력 회복",
    "회복",
    "방어 마법",
    "반사 마법",
    "번개 마법",
    "독 마법",              # 지속딜
    "상대 체력 회복 마법",
    "상대 마나 회복 마법",
    "상대 회복 마법",
    "저주 마법",            # 지속딜 + 힘 감소
    "혼란 마법",            # 크리, 중첩 확률 감소
    "불운 방법",            # 운 감소
    "흡혈",                # 상대 체력 강탈
    "마나 흡수"             # 상대 마나 강탈
]


class player:
    def __init__(self):
        self.name = foolish_fun
        self.md5 = foolish_fun
        self.health = 0       # 체력
        self.power = 0        # 힘           : 공격 확률
        self.defence = 0      # 방어          : 대미지 반감 확률
        self.speed = 0        # 회피          : 공격 무효화 확률
        self.luck = 0         # 운            : 뭔가 정말 우연이 일어날 확률
        self.mana = 0         # 마나          :
        self.magic = 0        # 마법 강도      : 마법의 세기
        self.magics = []      # 마법 종류
        self.critical = 0     # 크리티컬 확률
        self.critic = 0      # 크리티컬 배수
        self.hit_rate = 0     # 중첩 공격 확률

    def attack(self, ally):
        ply_persent = rd.randrange(1, 1000)
        if self.power >= ply_persent:
            ply_persent2 = rd.randrange(1, 1000)
            if self.critical >= ply_persent2:
                ally.health = ally.health - self.power * self.critic / 1000
                return self.name, "크리티컬!!", self.power * self.critic / 10000, ally.name, ally.health / 10
            else:
                ally.health = ally.health - self.power
                return self.name, "일반 공격", self.power / 10, ally.name, ally.health / 10
        else:
            return self.name, "공격 실패!", 0, ally.name, ally.health / 10


def typing(strigab, dsv=True):
    for dab in strigab:
        print(dab, end='')
        time.sleep(0.01)
    if dsv:
        print()


def foolish_fun(dsav, da=True):
    dsav = dsav / 10
    if dsav/100 >= 1:
        return str(dsav)
    else:
        if dsav/10 >= 1:
            if da:
                return str(' ' + str(dsav))
            else:
                return str(str(dsav) + ' ')
        else:
            if da:
                return str('  ' + str(dsav))
            else:
                return str(str(dsav) + '  ')


def mapping_md5(adbad):
    adbad.md5 = hashlib.md5(adbad.name.encode()).hexdigest()
    adbad.health = int((int(adbad.md5[0] + adbad.md5[1], 16) + 1) * 4000 / 256 + 1000)
    adbad.defence = int((int(adbad.md5[2] + adbad.md5[3], 16) + 1) * 1000 / 256)
    adbad.power = int((int(adbad.md5[4] + adbad.md5[5], 16) + 1) * 1000 / 256)
    adbad.speed = int((int(adbad.md5[6] + adbad.md5[7], 16) + 1) * 1000 / 256)
    adbad.luck = int((int(adbad.md5[8] + adbad.md5[9], 16) + 1) * 1000 / 256)
    adbad.mana = int((int(adbad.md5[10] + adbad.md5[11], 16) + 1) * 1000 / 256)
    adbad.critical = int((int(adbad.md5[12] + adbad.md5[13], 16) + 1) * 1000 / 256)
    adbad.critic = int((int(adbad.md5[14] + adbad.md5[15], 16) + 1) * 1000 / 256) + 1000
    adbad.hit_rate = int((int(adbad.md5[16] + adbad.md5[17], 16) + 1) * 1000 / 256)
    adbad.magic = int((int(adbad.md5[18] + adbad.md5[19], 16) + 1) * 1000 / 256)
    adbad.magics = [int(adbad.md5[20], 16), int(adbad.md5[21], 16), int(adbad.md5[22], 16)]


player1 = player()
player2 = player()

typing("Fantastic MD-5 Machine Operating .....\n")
typing("플레이어 1의 이름은 무엇입니까? : ", False)
player1.name = str(input())
typing("플레이어 2의 이름은 무엇입니까? : ", False)
player2.name = str(input())

mapping_md5(player1)
mapping_md5(player2)

os.system('cls')
print(player1.name + ' vs ' + player2.name)
print("")
typing("서로의 스텟")
print("")
time.sleep(1)
print(foolish_fun(player1.health), '|', foolish_fun(player2.health, False), ": 체력")
time.sleep(1)
print(foolish_fun(player1.power), '|', foolish_fun(player2.power, False), ": 힘")
time.sleep(1)
print(foolish_fun(player1.defence), '|', foolish_fun(player2.defence, False), ": 방어")
time.sleep(1)
print(foolish_fun(player1.speed), '|', foolish_fun(player2.speed, False), ": 회피")
time.sleep(1)
print(foolish_fun(player1.luck), '|', foolish_fun(player2.luck, False), ": 운")
time.sleep(1)
print(foolish_fun(player1.mana), '|', foolish_fun(player2.mana, False), ": 마나")
time.sleep(1)
print(foolish_fun(player1.magic), '|', foolish_fun(player2.magic, False), ": 마법 세기")
time.sleep(1)
print(foolish_fun(player1.critical), '|', foolish_fun(player2.critical, False), ": 크리티컬 확률")
time.sleep(1)
print(foolish_fun(player1.critic), '|', foolish_fun(player2.critic, False), ": 크리티컬 배수")
time.sleep(1)
print(foolish_fun(player1.hit_rate), '|', foolish_fun(player2.hit_rate, False), ": 중첩 공격 확률")
time.sleep(1.5)
print("")
print(player1.name, "의 마법 : ", end='')
for i in player1.magics:
    time.sleep(1)
    print(magics[i], end='. ')
print()
time.sleep(1)
print(player2.name, "의 마법 : ", end='')
for i in player2.magics:
    time.sleep(1)
    print(magics[i], end='. ')
print()  # 맵핑 결과 알려주는 코드... 쓸데없이 길어서 줄임.

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

typing("게임을 시작합니다...")

turn = 1
while True:
    print('%s의 공격\n %s %d 데미지\n %s의 남은 체력 : %d' % player1.attack(player2))
    print('------------------------------------------')
    if player2.health <= 0:
        os.system("cls")
        print(player1.name + "승리!")
        print('승자의 남은 체력 : %.2f ' % (player1.health / 10))
        print('진행한 턴 수 : %d' % turn)
        break
    time.sleep(1)
    print('%s의 공격\n %s %d 데미지\n %s의 남은 체력 : %d' % player2.attack(player1))
    print('------------------------------------------')
    if player1.health <= 0:
        os.system("cls")
        print(player2.name + "승리!")
        print('승자의 남은 체력 : %.2f ' % (player2.health / 10))
        print('진행한 턴 수 : %d' % turn)
        break
    time.sleep(1)
    turn = turn + 1
