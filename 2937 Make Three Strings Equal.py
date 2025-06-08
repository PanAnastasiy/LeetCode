class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        length = 0
        for i in range(len(min(s1, s2, s3, key=len))):
            if s1[i] == s2[i] == s3[i]:
                length += 1
            else:
                break
        if length == 0:
            return -1
        return len(s1 + s2 + s3) - 3 * length


print(Solution().findMinimumOperations("abc", s2="abb", s3="ab"))
