import sys

data = []
blue, white = 0,0

def fun(paper_x, paper_y, paper_size):
    global blue, white
    color = 0

    if paper_size == 1:
        if data[paper_x][paper_y]:
            blue += 1
            return 0
        else:
            white += 1
            return 0

    color = data[paper_x][paper_y]

    for i in range(paper_size):
        for j in range(paper_size):
            if color != data[paper_x + i][paper_y + j]:
                fun(paper_x, paper_y, paper_size // 2)
                fun(paper_x, paper_y + paper_size // 2, paper_size // 2)
                fun(paper_x + paper_size // 2, paper_y, paper_size // 2)
                fun(paper_x + paper_size // 2, paper_y + paper_size // 2, paper_size // 2)
                return 0

    if color:
        blue += 1
    else:
        white += 1

    return 0

size = int(sys.stdin.readline())

for i in range(size):
    data.append(list(map(int,sys.stdin.readline().split())))

fun(0,0,size)
print(white)
print(blue)