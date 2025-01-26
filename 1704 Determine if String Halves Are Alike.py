class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u')
        counter = 0
        a = s[:len(s)//2].lower()
        b = s[len(s)//2:].lower()
        for i in range(len(a)):
            if a[i] in vowels:
                counter += 1
            if b[i] in vowels:
                counter -= 1
        return not bool(counter)


print(Solution().halvesAreAlike("book"))
print(Solution().halvesAreAlike("textbook"))
