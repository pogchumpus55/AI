from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = defaultdict(list)

num_nodes = int(input("Enter the number of nodes: "))
for i in range(num_nodes):
    node = input(f"Enter node {i+1}: ")
    adj_nodes = input(f"Enter adjacent nodes for {node}: ").split()
    graph[node].extend(adj_nodes)

start_node = input("Enter the starting node: ")
bfs(graph, start_node)
