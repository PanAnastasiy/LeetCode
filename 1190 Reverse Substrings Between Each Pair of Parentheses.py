

class Solution:

    @staticmethod
    def reverseParentheses(s: str) -> str:
        stack = []
        for symbol in s:
            stack.append(symbol)
            if stack[-1] == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp[1:])
        return ''.join(stack)


print(Solution.reverseParentheses("ta()usw((((a))))"))
