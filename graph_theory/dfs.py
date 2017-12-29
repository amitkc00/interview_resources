#!/usr/local/bin/python3
from collections import defaultdict
# Depth First Search
# Doing it on my own.
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    #add Edge from Vertex v to Neighbour n
    def addEdge(self,v,n):
        self.graph[v].append(n)

    def DFSUtil(self,stack,visited):
        
        stacksize = len(stack)
        n = stack.pop(stacksize-1)

        print(n)
        
        nEdges = self.graph[n]
        
        print("nEdges = ")
        print(nEdges)

        print("visited =")
        print(visited)
        for edge in nEdges:
            print("Edge = %d"%(edge))
            if visited[edge] == False:
                stack.append(edge)
                visited[edge] = True
                self.DFSUtil(stack,visited)


    def DFS(self,v,size):
        print(self.graph)
        stack = []
        #visited = [False]*(len(self.graph))
        visited = [False]*size

        stack.append(v)
        visited[v] = True

        self.DFSUtil(stack,visited)


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(5,7)
g.DFS(0,8)

print('\n\n')
g.DFS(4,8)
