
class Solution(object):

    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        data = dict.fromkeys(['answer1', 'answer2'], 0)
        print(data)
        for num in nums1:
            if num in nums2:
                data['answer1'] += 1
        for num in nums2:
            if num in nums1:
                data['answer2'] += 1
        return data.values()


sol = Solution()
print(sol.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]))
