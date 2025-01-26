class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        answer = []
        for pair in [[nums[i], nums[i + 1]] for i in range(0, len(nums), 2)]:
            answer.extend(pair[0] * [pair[1]])
        return answer


print(Solution().decompressRLElist([1, 2, 3, 4]))
print(Solution().decompressRLElist([1, 1, 2, 3]))
