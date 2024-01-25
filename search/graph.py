import networkx as nx
from queue import Queue

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None
        """
        # Do some checking first
        all_nodes=self.graph.nodes()
        if start not in all_nodes:
            raise ValueError(f"The start node {start} is not the in the graph")
        if (not end ==None) and (end not in all_nodes):
            raise ValueError(f"The end node {end} is not the in the graph")
        if len(all_nodes)==0:
            raise ValueError("The given graph is empty.")
        Q = Queue()
        visited = []
        Q.put(start)
        visited.append(start)
        found_end=False
        parentage={}
        # Keep exploring as long as Q is not empty and the end node has not been found
        while (not Q.empty()) and (not found_end):
            v = Q.get()
            N = list(self.graph.neighbors(v))
            if (not end == None) and (end in N):
                #We found N and return its shortest path
                found_end=True
                parentage[end]=v
            for w in N:
                if w not in visited:
                    visited.append(w)
                    Q.put(w)
                    parentage[w]=v
        if (not end ==None) and (found_end):
            path_to_end=[end]
            currently_backtracking=end
            while (start not in path_to_end):
                print("path end: ", path_to_end)
                path_to_end.append(parentage[currently_backtracking])
                currently_backtracking=parentage[currently_backtracking]
            path_to_end.reverse()
            answer=path_to_end
        elif (not end == None) and (not found_end):
            answer=None
        elif (end==None):
            answer=visited
        return answer




