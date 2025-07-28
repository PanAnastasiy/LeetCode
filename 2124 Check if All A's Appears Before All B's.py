class Solution:
    def checkString(self, s: str) -> bool:
        flag = True
        for char in s:
            if char == 'b':
                flag = False
            elif not flag:
                return False
        return True

