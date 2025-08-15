class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        unique = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]  :
                        unique.add((i, j, k))
        return len(unique)


print(Solution().unequalTriplets([4, 4, 2, 4, 3]))
