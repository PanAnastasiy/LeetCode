
def findLoser(n: int, k: int) -> int:
    if n == 1:
        return 0
    else:
        return (findLoser(n - 1, k) + k) % n


class Solution(object):

    @staticmethod
    def findTheWinner(n: int, k: int) -> int:
        return findLoser(n, k) + 1


print(Solution.findTheWinner(6, 5))
