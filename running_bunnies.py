from typing import List, Tuple
from queue import Queue
from itertools import count


class GraphNode:
    def __init__(self, vertex_name, capacity, flow):
        self.vertex_name = vertex_name
        self.capacity = capacity
        self.flow = flow

    def __eq__(self, other):
        return self.vertex_name == other.vertex_name

    def __lt__(self, other):
        return self.vertex_name < other.vertex_name


class Vertex:
    def __init__(self, vertex_name, graph_nodes=None):
        self.vertex_name = vertex_name
        self.l = graph_nodes if graph_nodes is not None else []

    def get_vertex_name(self):
        return self.vertex_name

    def add_edge(self, v, c):
        if self.check_if_edge_exists(v):
            for graph_node in self.l:
                if graph_node.vertex_name == v:
                    graph_node.capacity += c
                    return
        else:
            self.l.append(GraphNode(v, c, 0))

    def add_flow(self, v, f):
        if not self.check_if_edge_exists(v):
            for graph_node in self.l:
                if graph_node.vertex_name == v:
                    graph_node.flow = graph_node.capacity + f
                    return
        else:
            self.find_edge(v).flow = f

    def remove_edge(self, v):
        if not self.check_if_edge_exists(v):
            raise ValueError("Edge doesn't exist")
        else:
            self.l.remove(self.find_edge(v))

    def get_adj_full_list(self):
        temp_list = sorted(self.l)
        return temp_list

    def get_adj_list(self):
        return [graph_node.vertex_name for graph_node in self.get_adj_full_list()]

    def print_adj_list(self):
        for graph_node in self.get_adj_full_list():
            print(graph_node)

    def find_edge(self, v):
        for graph_node in self.l:
            if graph_node.vertex_name == v:
                return graph_node

    def check_if_edge_exists(self, v):
        return any(graph_node.vertex_name == v for graph_node in self.l)

    def get_capacity(self, v):
        if not self.check_if_edge_exists(v):
            raise ValueError(f"getCapacity error: {self.get_vertex_name()} and vertex: {v} tried to getCapacity")
        return self.find_edge(v).capacity

    def get_flow(self, v):
        return self.find_edge(v).flow

    def __eq__(self, other):
        return self.vertex_name == other.vertex_name

    def __copy__(self):
        return Vertex(self.vertex_name, self.l.copy())


class GraphNode:
    def __init__(self, vertex_name, capacity, flow):
        self.vertex_name = vertex_name
        self.capacity = capacity
        self.flow = flow

    def get_vertex_name(self):
        return self.vertex_name

    def get_capacity(self):
        return self.capacity

    def get_flow(self):
        return self.flow

    def set_vertex_name(self, vertex_name):
        self.vertex_name = vertex_name

    def set_capacity(self, capacity):
        self.capacity = capacity

    def set_flow(self, flow):
        self.flow += flow

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __eq__(self, other):
        if isinstance(other, int):
            return self.vertex_name == other
        elif isinstance(other, GraphNode):
            return self.vertex_name == other.vertex_name

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __str__(self):
        return f"Vertex Name: {self.get_vertex_name()} Capacity: {self.get_capacity()} Flow: {self.get_flow()}"


class ShorterRouteNode:
    def __init__(self, vertex_name=None, parent=None, level=None):
        self.vertex_name = vertex_name
        self.parent = parent
        self.level = level

    def get_vertex_name(self):
        return self.vertex_name

    def get_parent(self):
        return self.parent

    def get_level(self):
        return self.level

    def set_vertex_name(self, vertex_name):
        self.vertex_name = vertex_name

    def set_parent(self, parent):
        self.parent = parent

    def set_level(self, level):
        self.level = level

    def __lt__(self, other):
        return self.level < other.level

    def __gt__(self, other):
        return self.level > other.level

    def __eq__(self, other):
        return self.level == other.level


class Graph:
    def __init__(self, n):
        self.make_empty_graph(n)

    def make_empty_graph(self, n):
        self.g = [Vertex(i, []) for i in range(n + 1)]
        self.l_size = n

    @classmethod
    def from_adjacency_matrix(cls, adj_matrix: List[List[int]]):
        n = len(adj_matrix)
        graph = cls(n)

        for i in range(n):
            for j in range(n):
                graph.add_edge(i, j, adj_matrix[i][j])  # Assuming the matrix is 0-indexed

        return graph

    def get_adj_list(self, u):
        return self.g[u].get_adj_list()

    def get_adj_full_list(self, u):
        return self.g[u].get_adj_full_list()

    def add_edge(self, u, v, c):
        self.g[u].add_edge(v, c)

    def add_flow(self, u, v, f):
        if not self.g[u].check_if_edge_exists(v):
            self.g[u].add_edge(v, f)
        elif self.g[u].get_capacity(v) < f:
            error = f"Error in add flow of vertex: {u} and vertex: {v}. Tried to add flow of: {f} to capacity: {self.g[u].get_capacity(v)}"
            raise ValueError(error)
        else:
            self.g[u].add_flow(v, f)

    def remove_edge(self, u, v):
        self.g[u].remove_edge(v)

    def print_graph(self):
        for vertex in self.g:
            print(f"Vertex Name: {vertex.get_vertex_name()} {{")
            vertex.print_adj_list()
            print("}}")

    def get_residual_graph(self):
        result = Graph(self.l_size)

        for u in range(0, self.l_size):
            temp_list = self.g[u].get_adj_full_list()
            for v in temp_list:
                f = v.get_flow()
                cf = v.get_capacity() - f
                if cf > 0:
                    result.g[u].add_edge(v.get_vertex_name(), v.get_capacity() - v.get_flow())
                if f > 0:
                    result.g[v.get_vertex_name()].add_edge(u, v.get_flow())

        return result

    def get_v_size(self):
        return self.l_size

    def get_vector_vertex(self):
        return self.g

    def get_capacity(self, u, v):
        return self.g[u].get_capacity(v)

    def get_flow(self, s):
        count = 0
        temp_list = self.g[s].get_adj_full_list()
        for node in temp_list:
            count += node.get_flow()

        return count


class BFSSolution:
    def __init__(self):
        pass

    def run(self, g, s, t):
        residual_graph = g.get_residual_graph()
        bfs_result = self.bfs(residual_graph, s)
        cur = ShorterRouteNode()
        while self.get_ancestor_parent(bfs_result, t) == s:
            min_capacity = self.get_min_capacity_in_route(residual_graph, bfs_result, t)
            cur = bfs_result[t]
            parent = cur.get_parent()
            while cur.get_vertex_name() != s:
                g.add_flow(parent, cur.get_vertex_name(), min_capacity)
                cur = bfs_result[parent]
                parent = cur.get_parent()

            residual_graph = g.get_residual_graph()
            bfs_result = self.bfs(residual_graph, s)

        return g

    def get_ancestor_parent(self, bfs_result, u):
        cur = u
        parent = bfs_result[u].get_parent()
        while parent != -1:
            cur = parent
            parent = bfs_result[parent].get_parent()
        return cur

    def bfs(self, g, s):
        bfs_queue = Queue()
        v_result = [ShorterRouteNode(vertex.get_vertex_name(), -1, float('inf')) for vertex in g.get_vector_vertex()]

        bfs_queue.put(g.get_vector_vertex()[s])
        v_result[s].set_level(0)

        while not bfs_queue.empty():
            u = bfs_queue.get()
            temp_list = u.get_adj_full_list()

            for v in temp_list:
                if v_result[v.get_vertex_name()].get_level() == float('inf'):
                    v_result[v.get_vertex_name()].set_level(v_result[u.get_vertex_name()].get_level() + 1)
                    v_result[v.get_vertex_name()].set_parent(u.get_vertex_name())
                    bfs_queue.put(g.get_vector_vertex()[v.get_vertex_name()])

        return v_result

    @staticmethod
    def sort_bfs_list(bfs_list):
        bfs_list.sort(key=lambda x: x.get_level())

    def get_min_capacity_in_route(self, g, bfs_result, u):
        parent = bfs_result[u].get_parent()
        min_capacity = g.get_capacity(parent, u)
        cur = u
        cur_capacity = min_capacity

        while parent != -1:
            cur_capacity = g.get_capacity(bfs_result[cur].get_parent(), cur)
            if cur_capacity < min_capacity:
                min_capacity = cur_capacity
            cur = parent
            parent = bfs_result[parent].get_parent()

        return min_capacity


def answer(times, time_limit):
    graph_from_matrix = Graph.from_adjacency_matrix(times)
    bfsResult = BFSSolution().run(graph_from_matrix, 0, len(times) - 1)
    print(f"Max flow = {bfsResult.get_flow(0)}")
