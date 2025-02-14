class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        arr = []
        for i in range(len(mat)):
            arr.extend(mat[i])
        answer = []
        for i in range(0, len(arr), c):
            answer.append(arr[i: i + c])
        return answer


print(Solution().matrixReshape([[1, 2], [3, 4]], 1,  4))
