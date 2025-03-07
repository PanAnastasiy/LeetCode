
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < len(s) // 2 < right_pointer:
            if s[left_pointer].isalpha() and s[right_pointer].isalpha():
                s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
                left_pointer += 1
                right_pointer -= 1
            elif s[left_pointer].isalpha():
                right_pointer -= 1
            elif s[right_pointer].isalpha():
                left_pointer += 1
            else:
                left_pointer += 1
                right_pointer -= 1
            return ''.join(s)


print(Solution().reverseOnlyLetters("ab-cd"))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
