class Solution:
    '''
    def containsDuplicate(self, nums: list[int]) -> bool:
        data = dict.fromkeys(set(nums), 0)
        for number in sorted(nums):
            data[number] += 1
            if data[number] > 1:
                return True
        return False
    '''

    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))

