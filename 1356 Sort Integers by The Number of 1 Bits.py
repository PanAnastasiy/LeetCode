class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


print(Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))
