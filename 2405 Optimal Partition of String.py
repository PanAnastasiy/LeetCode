class Solution:
    def partitionString(self, s: str) -> int:
        parts = []
        part = ''
        for char in s:
            if char not in part:
                part += char
            else:
                parts.append(part)
                part = char
        parts.append(part)
        print(parts)
        return len(parts)


print(Solution().partitionString("abacaba"))
