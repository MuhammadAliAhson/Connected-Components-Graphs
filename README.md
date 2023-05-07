# Connected_Components_Graphs
 Strongly connected labels and Weakly connected labels are part of a  graph. Either it is directed or undirected graphs.  Hello Everyone.  We all know that the Graph is used in Mapping analysis, Short distance measurements, Data Management, and much more.  So, I have made this Program in Python language in which you can find the connected components more precisely the most strongly connected components.  In the code, I have used the DFS Algorithm to find the connected components (nodes). The program will make a text file for the connected and least connected nodes present in a graph.  #Note   You Need a Good GPU to run this code for a massive number of nodes in a graph.  
In this you need to put your text file which contain the nodes and the the program will generate the result file with the respective connected components.
You can spilts the graph for larger values and then find the average if ypou are conmfortable.
If you follow this method then your answer can be little different form the rest, because of the average.

## Code_To_Find_Connected_Nodes_1.py

## README

This code implements an algorithm to find strongly connected components in a directed graph. It reads a text file (task1.txt) which contains edge information of the graph. The graph has 5105043 nodes and 6517187 edges. 

### Prerequisites 
* Python 3.x 
* `collections` module 
* `os` module

### How to use
1. Clone the repository.
2. Run the code in Python. 
3. The code reads the 'task1.txt' file which contains the edge information of the graph. 
4. The program creates 10 graphs for the edges and applies DFS algorithm to each one of them. 
5. The strongly connected components of the graphs are written to the 'Result1.txt' file. 
6. Open the 'Result1.txt' file to see the strongly connected components of the graphs.

### Files in Repository 
* `task1.txt` - A text file containing the edge information of the graph.
* `Result1.txt` - A text file to write the strongly connected components of the graphs.
* `README.md` - Information about the repository.

### Running the Code 
```python
python scc.py
```

### Output
The output of the program is written to the 'Result1.txt' file. The strongly connected components of the graphs are written in this file.


## Code_To_Find_Connected_Nodes_2.py

## Readme

## Instructions

This program reads an input file `task2.txt` which contains vertices and edges of a directed graph. It then divides the graph into 3 parts and finds strongly connected components (SCCs) for each part.

To run this program, follow the steps below:

1. Install Python 3.x or later on your computer.

2. Create an input file `task2.txt` with vertices and edges of a directed graph. Each line of the file should have two integers separated by a space, representing a directed edge from the first vertex to the second vertex.

3. Save the `task2.txt` file in the same directory where the Python program is located.

4. Run the Python program by opening a terminal or command prompt, navigating to the directory where the Python program is located, and typing `python3 program_name.py` on the command line.

5. The program will output the number of iterations and the SCCs for each part of the graph in the console.

6. The program will also create a file named `Result2.txt` in the same directory, which contains the SCCs for each part of the graph. The SCCs are separated by a new line.

## Code Explanation

The code first imports the `defaultdict` and `time` modules from Python, and the `os` module for interacting with the operating system. 

Next, a `Graph` class is defined, which represents a directed graph using an adjacency list. The class has the following methods:

- `__init__(self, vertices)`: Initializes a `Graph` object with a given number of vertices, an empty adjacency list, and a file named `Result2.txt` for writing SCCs.
- `addEdge(self, u, v)`: Adds a directed edge from vertex `u` to vertex `v` in the adjacency list.
- `DFSUtil(self, v, visited)`: A utility function used by DFS to traverse the graph recursively. It marks the current vertex as visited, writes the vertex to the `Result2.txt` file, and recursively traverses all adjacent vertices.
- `fillOrder(self, v, visited, stack)`: A utility function used to fill vertices in the stack according to their finishing times during the first DFS traversal.
- `printSCCs(self)`: The main function that finds and prints all strongly connected components. It first fills the stack with vertices in order of their finishing times during the first DFS traversal. It then marks all vertices as not visited during the second DFS traversal and pops vertices from the stack to traverse them. If a vertex is not visited, it calls `DFSUtil` to traverse all its adjacent vertices and write the SCC to the `Result2.txt` file.

After defining the `Graph` class, the program reads the `task2.txt` file to count the number of vertices and edges in the graph. It then creates a `Graph` object for each of the three parts of the graph and adds edges to each object by reading the `task2.txt` file again.

Finally, the program prints the number of iterations and the SCCs for each part of the graph by calling the `printSCCs` method for each `Graph` object. The program also creates a file named `Result2.txt` which contains the SCCs for each part of the graph.


