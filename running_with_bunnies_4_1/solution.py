import copy


# Graph API:
#   iter(graph) gives all nodes
#   iter(graph[u]) gives neighbours of u
#   graph[u][v] gives weight of edge (u, v)
class Graph:

    def __init__(self, square_matrix):
        self.graph = square_matrix
        self.V = len(square_matrix)  # No. of vertices

        # Initialize distances from src to all other vertices as INFINITE
        # so, start admiting that the rest of nodes are very very far
        self.INF = float("Inf")
        self.distances = [[self.INF for _ in range(self.V)] for _ in range(self.V)]
        self.parents = [[None for _ in range(self.V)] for _ in range(self.V)]
        # self.shortestPath = [[None for _ in xrange(self.V)] for _ in xrange(self.V)]

    def relax(self, src, u, v):
        if self.distances[src][u] != self.INF and self.distances[src][v] > self.distances[src][u] + self.graph[u][v]:
            self.distances[src][v] = self.distances[src][u] + self.graph[u][v]
            self.parents[src][v] = u

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm.  The function
    # also detects negative weight cycle

    def BellmanFord(self, src):
        # keep lower distances from source to another vertexes
        self.distances[src][src] = 0

        # Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1 edges
        for _ in range(self.V - 1):  # Run this until is converges
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in queue
            for u in range(self.V):
                for v in range(self.V):
                    self.relax(src, u, v)

        # Check for negative-weight cycles.  The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there is a cycle.
        for u in range(self.V):
            for v in range(self.V):
                if self.distances[src][u] != self.INF and self.distances[src][u] + self.graph[u][v] < \
                        self.distances[src][v]:
                    print("Graph contains negative weight cycle")
                    return False

        return True

    # The Bellman-Ford's complete sources algorithm.
    # Shortest path from all to all points
    def BellmanFordCompleteSource(self):
        for v in range(self.V):
            if not self.BellmanFord(v):
                return False
        return True

    def get_paths(self, start, goal, time):
        all_paths = []  # Collect all paths here
        # Initialize the stack with the starting vertex, its path, remaining time, and cycle factor vertices
        stack = [(start, [start], time, [[i] for i in range(self.V)])]
        child_vertices = set(range(self.V))

        while stack:
            current_vertex, path, remaining_time, cycle_factor_vertices = stack.pop()

            for next_vertex in child_vertices - set(cycle_factor_vertices[current_vertex]):
                # Calculate times to the next vertex and relevant points
                time_to_next = self.distances[current_vertex][next_vertex]
                time_to_goal_from_next = self.distances[next_vertex][goal]
                time_to_back_from_next = self.distances[next_vertex][current_vertex]

                next_cycle_factor_vertices = copy.deepcopy(cycle_factor_vertices)

                # Check for a zero-cost cycle to block
                if time_to_back_from_next + time_to_next == 0:
                    next_cycle_factor_vertices[current_vertex].append(next_vertex)
                    next_cycle_factor_vertices[next_vertex].append(current_vertex)

                # Check if it's possible to go to the next vertex and then reach the goal within the remaining time
                if 0 <= remaining_time - time_to_next - time_to_goal_from_next:
                    # Update the path and remaining time
                    next_path = path + [next_vertex]
                    next_remaining_time = remaining_time - time_to_next

                    # Add the next state to the stack
                    stack.append((next_vertex, next_path, next_remaining_time, next_cycle_factor_vertices))

                    # Check if the goal is reached and yield the set of freed bunnies
                    if next_vertex == goal:
                        freed_bunnies = set(next_path)
                        all_paths.append(freed_bunnies)

                        # If all bunnies are freed, terminate the search
                        if len(freed_bunnies) == self.V:
                            return all_paths
        return all_paths


def get_freed_bunnies(max_freed_bunnies, start_vertex, end_vertex):
    # Remove start and end vertices
    bunnies_set = max_freed_bunnies - set([start_vertex, end_vertex])

    # Sort the set in ascending order
    sorted_bunnies = sorted(bunnies_set)

    # Subtract 1 from each element
    adjusted_bunnies = [bunny - 1 for bunny in sorted_bunnies]

    return adjusted_bunnies


def answer(times, time_limit):
    g = Graph(times)

    if g.V < 3:
        return []

    maxFreedBunnies = set([])
    # if g.bellman_ford(0):
    #     print(g)
    if g.BellmanFordCompleteSource():
        # -------- print all distance -----------------
        # print("shortest distances:")
        # for row in xrange(g.V):
        #     print(row, g.distances[row])
        # print("shortest paths:")
        # for c in xrange(g.V):
        #     print(c, g.shortestPath[c])
        # ---------------------------------------------
        for freedBunnies in g.get_paths(0, g.V - 1, time_limit):
            # print freedBunnies
            # print("result", freedBunnies)

            maxLen = len(maxFreedBunnies)
            freedLen = len(freedBunnies)
            if maxLen < freedLen or (maxLen == freedLen and sum(maxFreedBunnies) > sum(freedBunnies)):
                maxFreedBunnies = freedBunnies
    else:
        return [i for i in range(g.V - 2)]

    return get_freed_bunnies(maxFreedBunnies, 0, g.V - 1)
