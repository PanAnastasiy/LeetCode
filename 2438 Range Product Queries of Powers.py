from functools import reduce


class Solution:

    def findPowers(self, number: int) -> list[int]:
        numbers = []
        biniary = bin(number)[:1:-1]
        print(biniary)
        for i in range(len(biniary)):
            if biniary[i] == '1':
                numbers.append(2**i)
        return numbers


    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        answer = []
        powers = self.findPowers(n)
        for query in queries:
            value = reduce(lambda x, y: x*y, powers[query[0]: query[1] + 1], 1)
            answer.append(value % (10**9 + 7))
        return answer


print(Solution().productQueries(15, [[0,1],[2,2],[0,3]]))
print(Solution().productQueries(2, [[0, 0]]))


