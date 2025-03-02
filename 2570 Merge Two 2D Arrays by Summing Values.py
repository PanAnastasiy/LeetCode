import operator

class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        answer = []
        dct = dict(nums1)
        dct2 = dict(nums2)
        first = list(dct.keys())
        second = list(dct2.keys())
        keys = first.copy()
        for key in dct2.keys():
            if key not in first:
                keys.append(key)
        keys.sort()
        for key in keys:
            if key in first and key in second:
                answer.append([key, dct[key] + dct2[key]])
            elif key in first:
                answer.append([key, dct[key]])
            else:
                answer.append([key, dct2[key]])
        return answer



print(Solution().mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
print(Solution().mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]))
