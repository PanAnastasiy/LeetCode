class Solution:
    def sumZero(self, n: int) -> list[int]:
        answer = [-i for i in range(1, n // 2 + 1)] + [i for i in range(1, n // 2 + 1)]
        if n % 2:
            answer.append(0)
        return answer
