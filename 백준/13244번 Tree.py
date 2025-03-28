n = int(input())
for _ in range(n):
    node = int(input())
    edge = int(input())
    graph = [[] for _ in range(node+1)]
    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    if node-edge != 1:
        print("graph")
        continue
    else:
        visit = []
        queue = [1]
        while queue:
            node2 = queue.pop(0)
            if node2 not in visit:
                visit.append(node2)
                queue.extend(graph[node2])
        if len(visit) == node:
            print("tree")
        else:
            print("graph")
