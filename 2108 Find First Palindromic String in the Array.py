from typing import List


class Solution:

    @staticmethod
    def firstPalindrome(words: List) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ''


print(Solution.firstPalindrome(["abc","car","ada","racecar","cool"]))
