
class Solution(object):

    @staticmethod
    def differenceOfSums(n: int, m: int) -> int:
        lst = [i for i in range(1, n + 1)]
        return sum(lst) - 2 * sum(list(filter(lambda x: x % m == 0, lst)))


print(Solution.differenceOfSums(10, 3))
