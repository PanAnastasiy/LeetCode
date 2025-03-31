class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        answer = 0
        for pair in enumerate(sorted(heights)):
            if pair[1] != heights[pair[0]]:
                answer += 1
        return answer


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]))
print(Solution().heightChecker([5, 1, 2, 3, 4]))