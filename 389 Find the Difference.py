class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_lst = sorted(list(s))
        t_lst = sorted(list(t))
        for i in range(len(s_lst)):
            if s_lst[i] != t_lst[i] and t_lst[i + 1] != s_lst[i]:
                return t_lst[i]
        return t_lst[-1]
