class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        answer = set()
        for num in nums:
            answer.add(num)
            answer.add(int(str(num)[::-1]))
        return len(answer)
