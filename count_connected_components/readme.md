DFS practice (not foobar question) 
Question: Connected Components

Given an undirected graph represented as an adjacency list, write a function to find the number of connected components in the graph.

```
def count_connected_components(graph):
    # Your code here
    pass

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

result = count_connected_components(graph)
print("Number of connected components:", result)
```

In this question:

An undirected graph is represented as an adjacency list (graph dictionary).
Your task is to implement the count_connected_components function that takes the graph as input and returns the number of connected components in the graph.
A connected component is a set of vertices where there is a path between every pair of vertices in the set.
This question will allow you to practice implementing DFS for graph traversal and handling connected components in an undirected graph. Try to write a solution and test it with different graph inputs.