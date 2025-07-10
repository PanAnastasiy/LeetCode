

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + [str(i) for i in range(4, len(score) + 1)]
        sorted_scores = sorted(score, reverse=True)
        dct = dict(zip(sorted_scores, ranks))
        return [dct[sc] for sc in score]


print(Solution().findRelativeRanks([10, 3, 8, 9, 4]))



