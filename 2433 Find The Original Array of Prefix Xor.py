class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        answer = [pref[0]]
        for i in range(1, len(pref)):
            answer.append(pref[i] ^ pref[i-1])
        return answer


sol = Solution()
print(sol.findArray([5, 2, 0, 3, 1]))
