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

        if not node in visited:
            visited.append(node)
            need_visited.extend(graph_input[node])

    return visited

def dfs(graph_input, start_node,visited = []):
    visited.append(start_node)

    for node in graph_input[start_node]:
        if node not in visited:
            dfs(graph_input, node, visited)
    return visited


for _ in range(dot+1):
    graph.append([])

for _ in range(line):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

for gg in dfs(graph,start): print(gg, end=" ")
print('')
for gg in bfs(graph,start): print(gg, end=" ")