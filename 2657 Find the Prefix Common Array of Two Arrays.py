
class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        d = {i: [0, 0] for i in range(1, len(A) + 1)}
        print(d)
        counter = 0
        answer = []
        for i in range(len(A)):
            d[A[i]][0] += 1
            d[B[i]][1] += 1
            if all(d[A[i]]) and all(d[B[i]]) and A[i] == B[i]:
                counter += 1
            elif all(d[A[i]]) and all(d[B[i]]):
                counter += 2
            elif all(d[A[i]]):
                counter += 1
            elif all(d[B[i]]):
                counter += 1
            answer.append(counter)
        print(answer)
        print(d)
        return answer


print(Solution().findThePrefixCommonArray([2, 3, 1], [3, 1, 2]))
# [0,2,3,4]
