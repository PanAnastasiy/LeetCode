class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


Solution().findCenter(edges=[[0, 0], [0, 1], [1, 0], [1, 1]])
