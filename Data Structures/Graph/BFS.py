import collections

def BFS(g, r):
    visited = set()
    queue = collections.deque([r])

    while queue:
        v = queue.popleft()
        print(v)
        for nbr in graph[v]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)


if __name__ == "__main__":
    graph = {0:[0,1,2], 1:[1], 2:[2]}
    BFS(graph,0)
    # BFS(graph,1)



