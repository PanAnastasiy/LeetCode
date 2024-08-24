class Solution(object):

    def findDuplicates(self, nums: list[int]) -> list[int]:
        data = {}
        for num in nums:
            data[num] = data.get(num, 0) + 1
        return list(filter(lambda x: data[x] > 1, data.keys()))


sol = Solution()
print(sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
