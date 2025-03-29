class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        count = 0
        unique = set(words1 + words2)
        for word in unique:
            if words1.count(word) == 1 and words2.count(word) == 1:
                count += 1
        return count


print(Solution().countWords(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]))
print(Solution().countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"]))
