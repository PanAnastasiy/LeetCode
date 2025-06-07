class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        def all_upper():
            for char in word:
                if char.islower():
                    return False
            return True

        def all_lower():
            for char in word:
                if char.isupper():
                    return False
            return True

        def first_capital():
            if word[0].islower():
                return False
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
            return True

        return all_upper() | all_lower() | first_capital()
