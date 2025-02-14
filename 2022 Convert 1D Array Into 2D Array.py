class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:

        if (n * m) != len(original):
            return []

        answer = [[0] * n for _ in range(m)]
        idx = 0
        for i in range(0, m):
            for j in range(0, n):
                answer[i][j] = original[idx]
                idx += 1
        return answer


sol = Solution()
print(sol.construct2DArray([1, 2, 3, 4], 2, 2))
