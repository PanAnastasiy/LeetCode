class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        temp = s
        s += s[0]
        s = s[1:]
        while temp != s:
            if s == goal:
                return True
            else:
                s += s[0]
                s = s[1:]
        return False

