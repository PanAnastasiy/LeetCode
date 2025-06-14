class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        words = sentence.split()
        for i in range(0, len(words)):
            if words[i][0] != words[i - 1][-1]:
                return False
        return True


print(Solution().isCircularSentence("leetcode exercises sound delightful"))
