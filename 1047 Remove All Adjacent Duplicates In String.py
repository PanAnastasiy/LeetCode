class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


sol = Solution()
print(sol.removeDuplicates("abbaca"))
