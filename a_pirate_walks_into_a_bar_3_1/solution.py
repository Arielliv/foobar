def answer(pirates_redirections_list):
    # create a graph entity from given list of connections
    graph = {i: [pirates_redirections_list[i]] for i in range(len(pirates_redirections_list))}

    if not has_cycle(graph):
        return 0

    cycles = find_all_cycles(graph)

    total_number_pf_pirates_in_a_cycle = 0
    for cycle in cycles:
        total_number_pf_pirates_in_a_cycle += len(cycle)
    return total_number_pf_pirates_in_a_cycle


def has_cycle(graph):
    visited = set()

    def dfs(node):
        visited.add(node)

        # Iterates over the neighbors of the current node. If the current node has no neighbors, the empty list is used as a default.
        for neighbor in graph.get(node, []):
            if neighbor not in visited or dfs(neighbor):
                return True

        return False

    # Uses a generator expression with any() to check if there is a cycle in any connected component of the graph.
    # for node in range(len(graph)): Iterates over all nodes in the graph.
    # dfs(node): Calls the DFS function for each node.
    # any(): Returns True if at least one of the DFS calls returns True, indicating the presence of a cycle.
    return any(dfs(node) for node in range(len(graph)))


def find_all_cycles(graph):
    visited = set()
    cycles = []

    def dfs(node, path):
        visited.add(node)
        path.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, path.copy())
            elif neighbor in path:
                # If the neighbor is already in the current path, it means a cycle is found.
                # The cycle is appended to the cycles list, starting from the index where the neighbor is first encountered in the path.
                cycles.append(path[path.index(neighbor):])

    for node in range(len(graph)):
        if node not in visited:
            dfs(node, [])

    return cycles


def find_cycle_length(graph):
    visited = set()

    def dfs(node, depth):
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = dfs(neighbor, depth + 1)
                if result is not None:
                    return result
            elif neighbor in visited and depth - visited[neighbor] > 1:
                return depth - visited[neighbor] + 1

        visited.remove(node)
        return None

    for node in graph:
        if node not in visited:
            result = dfs(node, 0)
            if result is not None:
                return result

    return None
