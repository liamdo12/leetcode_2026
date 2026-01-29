# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']):
        copied = {}

        def dfs(curr):
            if curr in copied:
                return copied[curr]
            
            clone = Node(curr.val)
            copied[curr] = clone

            for neigh in curr.neighbors:
                clone_neighbors = dfs(neigh)
                clone.neighbors.append(clone_neighbors)
            
            return clone

        return dfs(node) if node else None
    



            
            