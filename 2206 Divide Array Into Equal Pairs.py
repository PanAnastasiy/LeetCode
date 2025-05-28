class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        if len(nums) % 2:
            return False
        dct = {num: nums.count(num) for num in set(nums)}
        return all(x % 2 == 0 for x in dct.values())


print(Solution().divideArray([3,2,3,2,2,2]))