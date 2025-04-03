class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        answer = 0
        for i in range(len(s)):
            prefix = s[: i + 1]
            if prefix in words:
                answer += words.count(prefix)
        return answer


print(Solution().countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc"))
