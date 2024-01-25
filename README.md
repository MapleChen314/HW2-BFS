![BuildStatus](https://github.com/MapleChen314/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)
# Assignment 2
Breadth-first search

# Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

## Breadth-First Search
This implementation of breadth-first search takes in a .adjlist file describing a graph and traverses it in a breadth-first way starting from a user-defined starting node. It starts at the starting node and traverses all neighbors before traversing all of the neighbor's neighbors (and so on). The code can also be used to find the shortest path between a start and end node. It will throw an error if the user-defined start/end nodes are not part of the given graph, or if the given graph is empty.

# Getting Started
To get started you will need to fork this repository onto your own github. You will then work on the code base from your own repo and make changes to it in the form of commits. 

# Reference Information
## Test Data
Two networks have been provided in an adjacency list format readable by [networkx](https://networkx.org/), is a commonly used python package for working with graph structures. These networks consist of two types of nodes:
* Faculty nodes 
* Pubmed ID nodes

However, since these are both stored as strings, you can treat them as equivalent nodes when traversing the graph. The first graph ("citation_network.adjlist") has nodes consisting of all BMI faculty members, the top 100 Pubmed papers *cited by* faculty, and the top 100 papers that *cite* faculty publications. Edges are directed and and edge from node A -> B indicates that node A *is cited by* node B. There are 5120 nodes and 9247 edges in this network.

The second network is a subgraph of the first, consisting of only the nodes and edges along the paths between a small subset of faculty. There are 30 nodes and 64 edges.

# Completing the assignment
Make sure to push all your code to github, ensure that your unit tests are correct, and submit a link to your github through the google classroom assignment.

# Grading

## Code (6 points)
* Breadth-first traversal works correctly (3)
* Traces the path from one faculty to another (2)
* Handles edge cases (1)

## Unit tests (3 points)
* Output traversal for mini data set (1)
* Tests for at least two possible edge cases (1)
* Correctly uses exceptions (1)

## Style (1 points)
* Readable code with clear comments and method descriptions
* Updated README with description of your methods

