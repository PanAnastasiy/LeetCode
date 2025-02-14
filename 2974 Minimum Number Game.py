class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        arr = []
        while nums:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(alice)
        return arr


print(Solution().numberGame([5, 4, 2, 3]))