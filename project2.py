from collections import defaultdict
import time
import os
#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.file = open("Result2.txt","a")
        
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


count = 0
with open('task2.txt', 'r') as file:
    # reading each line
    for line in file:
        # reading each word
        for word in line.split():
            count = count + 1

print(count)

converted_num = []
converted_num = [0 for i in range(count)]

file.close()
x = -1

with open('task2.txt', 'r') as file:
    # reading each line
    for line in file:
        for word in line.split():
            x = x + 1
            converted_num[x] = int(word)

# print(converted_num)


re = max(converted_num)


g = Graph(8000)
g1 = Graph(re)
g2 = Graph(re)
g3 = Graph(re)
g4 = Graph(re)
g5 = Graph(re)
g6 = Graph(re)
g7 = Graph(re)
g8 = Graph(re)
g9 = Graph(re)


count=0
x = 0
with open('task2.txt', 'r') as file:
    for value in file.readlines():
        if(count<8000):
      
         g.addEdge(converted_num[x], converted_num[x+1])
         x+=2
        count+=1
        
        if(count<16000):
            g1.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
            
        if(count<24000):
      
            g2.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
        """
        if(count<2042016):
      
            g3.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
        if(count<2552520):
        
            g4.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
        if(count<3063024):
       
            g5.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
        if(count<3573528):
        
            g6.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
        if(count<4084032):
        
            g7.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
        if(count<4594536):
   
            g8.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
        if(count<5105043):
   
            g9.addEdge(int(converted_num[x]), int(converted_num[x+1]))
            x+=2
            count+=1
"""

print("Loading ",end = ' ')
for i in range(3):
    time.sleep(0.8)
    print(" . ",end = ' ')

os.system('cls')

print("Number of Iterations are  ",count)
print ("Following are strongly connected components in given graph")
g.printSCCs()
g1.printSCCs()
g2.printSCCs()

print("End of the procedure .........")