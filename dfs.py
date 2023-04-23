from collections import defaultdict

def dfs(graph, start, visited):
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = defaultdict(list)

num_nodes = int(input("Enter the number of nodes: "))
for i in range(num_nodes):
    node = input(f"Enter node {i+1}: ")
    adj_nodes = input(f"Enter adjacent nodes for {node}: ").split()
    graph[node].extend(adj_nodes)

start_node = input("Enter the starting node: ")
visited = set()
dfs(graph, start_node, visited)
