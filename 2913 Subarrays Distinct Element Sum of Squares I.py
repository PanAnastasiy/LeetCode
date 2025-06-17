class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        distinct = []
        for i in range(len(nums)):
            unique = set()
            for j in range(i, len(nums)):
                unique.add(nums[j])
                distinct.append(len(unique))
        return sum(map(lambda x: x**2, distinct))


print(Solution().sumCounts([1, 2, 1]))
