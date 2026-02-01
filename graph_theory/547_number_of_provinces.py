# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

'''
The idea is to run dfs for every node to find the connected graph (this is the adjacency matrix)
Time complexity: O(R x C) (R == C) => O(N^2)
Space complexity: O(V)
'''

class Solution:
    def findCircleNum(self, isConnected) -> int:
        count = 0
        n = len(isConnected)
        visited = set()

        def dfs(node):
            for nei in range(n):
                if isConnected[node][nei] == 1 and nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1

        return count
    
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
a = Solution()
result = a.findCircleNum(isConnected)
print(result)