class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        answer = []
        for i in range(len(cost)):
            answer.append(min(cost[:i + 1]))
        return answer
