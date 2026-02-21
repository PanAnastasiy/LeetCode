class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        answer = []
        min_diff = float('inf')
        for i in range(len(arr)-1):
            if arr[i + 1] - arr[i] < min_diff:
                answer.clear()
                min_diff = arr[i + 1] - arr[i]
                answer.append([arr[i], arr[i + 1]])
            elif arr[i + 1] - arr[i] == min_diff:
                answer.append([arr[i], arr[i + 1]])
        return answer


