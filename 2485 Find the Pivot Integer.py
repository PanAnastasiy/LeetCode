
class Solution:

    def pivotInteger(self: object(), num: int) -> int:
        nums = list(range(1, num + 1))
        for i in range(len(nums)):
            if sum(nums[:i + 1]) == sum(nums[i:]):
                return i + 1
        return -1


sol = Solution()
print(sol.pivotInteger(4))
