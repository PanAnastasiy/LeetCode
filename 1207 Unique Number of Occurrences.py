class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dct = {number: arr.count(number) for number in set(arr)}
        return len(dct) == len(set(dct.values()))


print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))