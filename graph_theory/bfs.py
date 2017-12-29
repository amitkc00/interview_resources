#!/usr/local/bin/python3

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # Add Edge from Vertex v to Neighbour n
    def addEdge(self,v,n):
        self.graph[v].append(n)

    def BFS(self,v):

        visited = [False]*(len(self.graph))
        queue = []
        queue.append(v)
        visited[v]=True
        
        print(self.graph)
        while queue:
            print(queue)
            print(visited)
            s = queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]=True




    
g = Graph()

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.BFS(2)
