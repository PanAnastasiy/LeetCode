class Solution:
    def isValid(self, word: str) -> bool:
        vowel = False
        consonant = False
        if len(word) < 3:
            return False
        for char in word:
            if not char.isalnum():
                return False
            if char.lower() in "aeiou":
                vowel = True
            if char.lower() in "bcdfghjklmnpqrstvwxyz":
                consonant = True
        return vowel and consonant
