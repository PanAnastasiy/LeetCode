class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:

        def check(arr1, arr2):
            dct_1 = {a: arr1.count(a) for a in set(arr1)}
            dct_2 = {a: arr2.count(a) for a in set(arr2)}

            for key in dct_1:
                if dct_2[key]:
                    return key
            return -1

        return check(nums1, nums2) if len(nums1) > len(nums2) else check(nums2, nums1)
