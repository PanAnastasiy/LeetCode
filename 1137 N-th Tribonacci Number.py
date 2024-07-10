
class Solution:

    @staticmethod
    def tribonacci(n: int) -> int:
        answer = [0, 1, 1]
        if n < 3:
            return answer[n]
        for i in range(3, n + 1):
            answer.append(answer[i - 1] + answer[i - 2] + answer[i - 3])
        print(answer)
        return answer[-1]


print(Solution.tribonacci(3))
