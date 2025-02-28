class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
                if len(stack) > answer:
                    answer = len(stack)
            elif char == ')':
                stack.pop()
        return answer


print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))
print(Solution().maxDepth("(1)+((2))+(((3)))"))
