import sys

a = int(sys.stdin.readline())
data = [0]


for k in range(3 * (a+1)):
    data.append(0)


for i in range(a+1):
    if data[3 * i + 2] == 0 or data[3 * i + 2] > data[i] + 1:
        data[3 * i + 2] = data[i] + 1

    if data[2 * i + 1] == 0 or data[2 * i + 1] > data[i] + 1:
        data[2 * i + 1] = data[i] + 1

    if data[i + 1] == 0 or data[i + 1] > data[i] + 1:
        data[i + 1] = data[i] + 1


print(data[a-1])
#for k in range(len(data)):
#    print(str(k+1) + " : " + str(data[k]))