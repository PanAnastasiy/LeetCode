from collections import Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dct = {}
        for s in strs:
            new_s = ''.join(sorted(s))
            if new_s in dct.keys():
                dct[new_s].append(s)
            else:
                dct[new_s] = [s]
        return list(dct.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
