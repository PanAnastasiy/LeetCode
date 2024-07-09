class Solution:

    @staticmethod
    def balancedStringSplit(s: str) -> int:
        count, r, l = 0, 0, 0
        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                count += 1
        return count


print(Solution.balancedStringSplit("RLRRRLLRLL"))
