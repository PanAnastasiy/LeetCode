class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        answer = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                answer.append(i)
        return answer


sol = Solution()
print(sol.stableMountains([1, 2, 3, 4, 5], 2))
