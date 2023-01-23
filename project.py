from collections import defaultdict
import time
import os
#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.file = open("Result1.txt","a")
        
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited[v]= True
        self.file.write(str(v) +" ")
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)


    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    # The main function that finds and prints all strongly
    # connected components
    def printSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)

        #Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i]==False:
                self.DFSUtil(i, visited)
                self.file.write("\n")
        self.file.close()



#os.system('cls')

file = open("task1.txt")
headers=4
for index in range(0,4):
    file.readline()
    
g = Graph(5105044)
g1 = Graph(5105044)
g2 = Graph(5105044)
g3 = Graph(5105044)
g4 = Graph(5105044)
g5 = Graph(5105044)
g6 = Graph(5105044)
g7 = Graph(5105044)
g8 = Graph(5105044)
g9 = Graph(5105044)

FromNodeId=0
ToNodeId=0
count=0
for value in file.readlines():
    if(count<510504):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<1021008):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g1.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<1531512):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g2.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<2042016):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g3.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<2552520):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g4.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<3063024):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g5.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<3573528):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g6.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<4084032):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g7.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<4594536):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g8.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1
    if(count<5105043):
        value=value.replace('\n','')
        temp=value.split('\t')
        FromNodeId=temp[0]
        ToNodeId=temp[1]
        g9.addEdge(int(FromNodeId), int(ToNodeId))
        count+=1


print("Loading ",end = ' ')
for i in range(3):
    time.sleep(0.8)
    print(" . ",end = ' ')

os.system('cls')

print("Number of Iterations are  ",count)
print ("Strongly connected components in graph are given below")
g.printSCCs()
g1.printSCCs()

g2.printSCCs()
"""
g3.printSCCs()
g4.printSCCs()
g5.printSCCs()
g6.printSCCs()
g7.printSCCs()
g8.printSCCs()
g9.printSCCs()
"""
fin= open("Result1.txt", 'r') 

for index in range(0,15251652):
        fin.readline()

for index in range(15251652,15252405):    
        print(fin.read())
        time.sleep(0.5)

fin.close()

print("End of the procedure .........")