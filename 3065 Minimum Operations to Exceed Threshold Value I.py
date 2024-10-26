
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if min(nums) > k - 1:
            return 0
        else:
            return len(list(filter(lambda x: x < k, nums)))