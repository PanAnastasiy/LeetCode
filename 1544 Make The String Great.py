class Solution:

    def check_reg(self, first: str, second: str) -> bool:
        if ord(first) != ord(second) and first.lower() == second.lower():
            return True
        return False

    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and self.check_reg(char, stack[-1]):
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


print(Solution().makeGood("leEeetcode"))
print(Solution().makeGood("abBAcC"))
