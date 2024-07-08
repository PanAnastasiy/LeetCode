from functools import reduce


class Solution(object):

    @staticmethod
    def findPermutationDifference(s: str, t: str) -> int:
        hash_table = {s[index]: index for index in range(len(s))}
        return sum(list(map(lambda x: abs(int(t.index(x)) - int(hash_table[x])), t)))


print(Solution.findPermutationDifference("abcd", "cdab"))