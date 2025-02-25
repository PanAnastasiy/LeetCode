class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first_pointer = 0
        last_pointer = len(s) - 1
        while first_pointer < last_pointer:
            s[first_pointer], s[last_pointer] = s[last_pointer], s[first_pointer]
            first_pointer += 1
            last_pointer -= 1


print(Solution().reverseString(["h","e","l","l","o"]))
print(Solution().reverseString(["H","a","n","n","a","h"]))