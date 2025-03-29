class Solution:
    def minLength(self, s: str) -> int:
        stack = [s[0]]
        i = 1
        while i < len(s):
            if stack and stack[-1] + s[i] in ('AB', 'CD'):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return len(stack)


print(Solution().minLength("ABFCACDB"))
print(Solution().minLength("ACBBD"))
print(Solution().minLength("CCCCDDDD"))
