import sys

dot, line, start =  map(int,sys.stdin.readline().split())
graph = []
data = []
end = False

def bfs(graph_input, start_node):
    need_visited, visited = [],[]
    need_visited.append(start_node)

    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        for k in graph_input[node]:
            if not k in visited:
                visited.append(k)

for _ in range(dot+1):
    graph.append([])

for _ in range(line):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()