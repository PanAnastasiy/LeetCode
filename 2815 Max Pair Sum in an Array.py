class Solution:
    def maxSum(self, nums: list[int]) -> int:
        dct = {}
        for num in nums:
            key = max(str(num))
            dct[key] = dct.get(key, []) + [num]
        if not any(len(x) > 1 for x in dct.values()):
            return -1
        answer = 0
        for pair in dct.values():
            if len(pair) > 1:
                pair.sort()
                if pair[-1] + pair[-2] > answer:
                    answer = pair[-1] + pair[-2]
        return answer


print(Solution().maxSum([2536, 1613, 3366, 162]))
