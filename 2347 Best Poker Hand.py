class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        count = self.countOfSameRank(ranks)
        if count > 2:
            return "Three of a Kind"
        elif count > 1:
            return "Pair"
        else:
            return "High Card"

    def countOfSameRank(self, ranks):
        dct = {rank: ranks.count(rank) for rank in set(ranks)}
        return max(dct.values())


print(Solution().bestHand([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"]))
print(Solution().bestHand([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]))
print(Solution().bestHand([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"]))
