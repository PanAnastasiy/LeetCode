class Solution:
    def minimumLength(self, s: str) -> int:
        d = {ch: s.count(ch) for ch in set(s)}
        list_ans = list(map(lambda x: x % 2, d.values()))
        return list_ans.count(0) + len(list_ans)


print(Solution().minimumLength("aa"))
