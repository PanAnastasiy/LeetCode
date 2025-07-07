class Solution:

    def isPrefixAndSuffix(self, str1: str, str2: str) -> int:
        print(str1, str2)
        l = len(str1)
        print(f'str1 - {str1}, prefix-  {str2[: l]}, suffix - {str2[-l:]}')
        if str1 == str2[: l] == str2[-l:]:
            return 1
        return 0

    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        answer = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                answer += self.isPrefixAndSuffix(words[i], words[j])
        return answer


print(Solution().countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
