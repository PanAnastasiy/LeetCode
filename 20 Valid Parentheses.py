class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        dct = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in dct.keys():
                stack.append(c)
            elif not stack:
                return False
            elif c == dct[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0


sol = Solution()
print(sol.isValid("([])"))
print(sol.isValid("}["))
