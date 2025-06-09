class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        '''
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        '''
        maxi = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxi
            if temp > maxi:
                maxi = temp
        arr[-1] = -1
        return arr


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
