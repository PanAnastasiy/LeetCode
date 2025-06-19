class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        arr.sort()
        unique = set()
        for i in range(len(arr)):
            if arr[i] * 2 in unique or (arr[i] % 2 == 0 and arr[i] // 2 in unique):
                return True
            unique.add(arr[i])
        return False
