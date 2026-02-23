class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        first, second = 0, len(s) - 1
        s = list(s)
        while first <= second:
            if s[first].lower() not in vowels:
                first += 1
            elif s[second].lower() not in vowels:
                second -= 1
            else:
                s[first], s[second] = s[second], s[first]
                first += 1
                second -= 1
        return ''.join(s)