class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sub_str = s[: k]
        check = set()
        check.add(sub_str)
        pointer = k
        while pointer < len(s):
            sub_str = sub_str[1:] + s[pointer]
            check.add(sub_str)
            pointer += 1
        return len(check) == 2 ** k


print(Solution().hasAllCodes("00110", 2))


