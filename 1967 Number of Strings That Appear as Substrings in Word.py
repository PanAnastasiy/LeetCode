
class Solution(object):
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        answer = 0
        for pattern in patterns:
            if pattern in word:
                answer += 1
        return answer


sol = Solution()
print(sol.numOfStrings(["a", "abc", "bc", "d"], "abc"))
