chessboard = []
ans = 2500
good_chess1 = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
good_chess2 = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]

l, w = map(int, input().split())
for _ in range(l):
    line = str(input())
    chessboard.append(line)
for i in range(l-7):
    for j in range(w-7):
        check1 = 0
        check2 = 0
        for k1 in range(8):
            for k2 in range(8):
                if chessboard[i+k1][j+k2] != good_chess1[k1][k2]:
                    check1 += 1
                if chessboard[i+k1][j+k2] != good_chess2[k1][k2]:
                    check2 += 1
        ans = min(ans, check1, check2)
print(ans)
