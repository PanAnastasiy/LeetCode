class Solution:

    def reverse_elements(self, s: list, letters: bool) -> list:
        first, second, = 0, len(s) - 1,

        if letters:
            check = lambda x: x.isalpha()
        else:
            check = lambda x: not x.isalnum()

        while first < second:

            if check(s[first]) and check(s[second]):
                s[first], s[second] = s[second], s[first]
                first += 1
                second -= 1
            elif check(s[first]):
                second -= 1
            elif check(s[second]):
                first += 1
            else:
                first += 1
                second -= 1
        return s

    def reverseByType(self, s: str) -> str:
        s = list(s)

        s = self.reverse_elements(s, letters=True)
        s = self.reverse_elements(s, letters=False)

        return ''.join(s)


print(Solution().reverseByType(")ebc#da@f("))
