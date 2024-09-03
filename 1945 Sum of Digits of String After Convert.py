class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dict_map = {chr(pos): str(pos - 96) for pos in range(ord('a'), ord('z')+1)}
        s = ''.join(list(map(lambda x: dict_map[x], list(s))))
        for _ in range(k):
            s = sum(list(map(int, list(str(s)))))
        return s



sol = Solution()
print(sol.getLucky("leetcode", 2))
print(sol.getLucky("iiii", 1))
