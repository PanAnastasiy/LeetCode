class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        parentheses = []
        stack = []
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
                stack.append(ch)
            if ch == ')':
                count -= 1
                stack.append(ch)
            if count == 0:
                parentheses.append(''.join(stack[1:-1]))
                stack = []
        return ''.join(parentheses)


print(Solution().removeOuterParentheses("(()())(())"))
print(Solution().removeOuterParentheses("(()())(())(()(()))"))
print(Solution().removeOuterParentheses("()()"))
