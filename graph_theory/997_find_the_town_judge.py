# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


'''
Time complexity: O(n)
space complexity: O(n)
'''


class Solution:
    def findJudge(self, n: int, trust) -> int:

        # if there was a judge, there is at least n - 1 persons
        if len(trust) < n - 1:
            return -1
        
        # the direction from a node to other
        indegree = [0] * (n + 1)
        # the direction the node received from other
        outdegree = [0] * (n + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        
        # the judge is the node that dont have relationship to other node (outdegree = 0) and receive all other everybody trust (indegree = n - 1)
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        
        return -1


a = Solution()

n = 3
trust = [[1,2],[2,3]]
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
result = a.findJudge(n, trust)
print(result)

        
            
