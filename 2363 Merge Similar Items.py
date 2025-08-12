class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        dct = dict(items1)
        for key, value in items2:
            dct[key] = dct.get(key, 0) + value
        return sorted([list(pair) for pair in dct.items()])


print(Solution().mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))
print(Solution().mergeSimilarItems([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]]))
print(Solution().mergeSimilarItems([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]]))
