class Solution:

    def getClearString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        print(stack)
        return ''.join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.getClearString(s) == self.getClearString(t)


print(Solution().backspaceCompare("##ab", "c#d#"))
