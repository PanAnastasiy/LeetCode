class Solution:
    def sumOfMultiples(self, n: int) -> int:
        answer = []
        for number in range(1, n + 1):
            if any([number % 3 == 0, number % 5 == 0, number % 6 == 0, number % 7 == 0]):
                answer.append(number)
        return sum(answer)


print(Solution().sumOfMultiples(10))
print(Solution().sumOfMultiples(9))
