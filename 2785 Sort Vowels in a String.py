class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        indexes = []
        for i in range(len(s)):
            if s[i].lower() in 'aouei':
                vowels.append(s[i])
                indexes.append(i)
        vowels = sorted(vowels, key=ord)
        j = 0
        s = list(s)
        for index in indexes:
            s[index] = vowels[j]
            j += 1
        return ''.join(s)


print(Solution().sortVowels("lEetcOde"))