from collections import deque
import numpy as np

class Graph:
    
    def __init__(self,graph,adj):
        self.graph = graph
        self.adj = adj
    
    def bfs(self,start,goal,graph):
        visited = list()
        trace = dict()
        buffer = deque()
        
        buffer.append(start)
        trace[start] = 0
        
        while len(buffer)!=0:
            n = buffer.pop()
            if n not in visited:
                if n == goal:
                    break
                visited.append(n)
                for i in np.where(np.array(self.adj[n-1])==1)[0]:
                    if i+1 not in visited and i+1 not in buffer:
                        buffer.appendleft(i+1)
                        trace[i+1] = n
        
        route= ""
        print(f"the path from {graph[start-1]} to {graph[goal-1]} is ",end="")
        while goal!= 0:
            route += graph[goal-1]
            goal = trace[goal]
            if goal != 0:
                route += " >- "
        
        print(route[::-1])
        
    def dfs(self,start,goal,graph):
        visited = list()
        trace = dict()
        buffer = deque()
        
        buffer.append(start)
        trace[start] = 0
        
        while len(buffer)!=0:
            n = buffer.pop()
            if n not in visited:
                self.recursive(n,visited,buffer,trace)
        
        route= ""
        print(f"the path from {graph[start-1]} to {graph[goal-1]} is ",end="")
        while goal!= 0:
            route += graph[goal-1]
            goal = trace[goal]
            if goal != 0:
                route += " >- "   
        print(route[::-1])       
                
    def recursive(self,n,visited,buffer,trace):
        visited.append(n)
        for i in np.where(np.array(self.adj[n-1])==1)[0]:
            if i+1 not in visited:
                buffer.appendleft(i+1)
                trace[i+1] = int(n)
                self.recursive(i+1,visited,buffer,trace)
                
    
graph = list(input("Enter the nodes in the graph: ").split(' '))
n = len(graph)
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    connect = list(map(str,input(f"Enter connected nodes to {graph[i]}: ").split(' ')))
    for node in connect:
        matrix[i][graph.index(node)] = 1
        
        
gr = Graph([i for i in range(1,n+1)],matrix)
s = graph.index((input("\nEnter the start node: ")))+1
g = graph.index((input("\nEnter the goal node: ")))+1

gr.bfs(s,g,graph)
gr.dfs(s,g,graph)
        