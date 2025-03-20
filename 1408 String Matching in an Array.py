class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        answer = set()
        for scanning_word in words:
            for word in words:
                if word != scanning_word and scanning_word in word:
                    answer.add(scanning_word)
        return list(answer)


print(Solution().stringMatching(["mass", "as", "hero", "superhero"]))
print(Solution().stringMatching(["leetcode", "et", "code"]))
