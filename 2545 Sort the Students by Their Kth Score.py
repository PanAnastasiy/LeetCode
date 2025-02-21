class Solution:
    '''
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        for i in range(len(score)):
            for j in range(len(score)):
                if score[j][k] < score[i][k]:
                    score[i], score[j] = score[j], score[i]
        return score
    '''

    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=lambda y: y[k], reverse=True)


print(Solution().sortTheStudents([[10, 6, 9, 1],
                                       [7, 5, 11, 2],
                                       [4, 8, 3, 15]], 2))

print(Solution().sortTheStudents([[3, 4], [5, 6]], 0))
