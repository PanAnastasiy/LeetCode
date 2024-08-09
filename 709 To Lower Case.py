

class Solution:

    @staticmethod
    def toLowerCase(s: str) -> str:
        return ''.join([letter if ord(letter) > ord('Z') or not letter.isalpha() else chr(ord(letter) + 32) for letter in s])


print(Solution.toLowerCase("Hello"))
