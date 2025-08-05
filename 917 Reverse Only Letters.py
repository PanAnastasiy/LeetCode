
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst = list(s)
        left, right = 0, len(lst) - 1
        while left < right:
            if lst[left].isalpha() and lst[right].isalpha():
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
            elif lst[left].isalpha():
                right -= 1
            elif lst[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(lst)


print(Solution().reverseOnlyLetters("ab-cd"))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
