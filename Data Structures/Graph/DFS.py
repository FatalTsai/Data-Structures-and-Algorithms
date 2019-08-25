def DFS(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        DFS(graph, next, visited)
    return visited



graph = {'0': set(['0', '1', '2']) , '1': set(['1']), '2': set(['2'])}
print(DFS(graph, '0'))
