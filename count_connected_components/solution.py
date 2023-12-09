
def count_connected_components(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    components = 0
    for node in graph:
        if node not in visited:
            dfs(node)
            components += 1

    return components
