class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        for fruit in fruits:
            for basket in baskets:
                if basket >= fruit:
                    baskets.remove(basket)
                    break
        return len(baskets)


print(Solution().numOfUnplacedFruits([4, 2, 5], [3, 5, 4]))
