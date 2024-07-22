
class Solution(object):

    def losingPlayer(self: object, x: int, y: int) -> str:
        return 'Alice' if min(x, y // 4) % 2 else 'Bob'


solution = Solution()
print(solution.losingPlayer(4, 11))
