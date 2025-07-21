from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        dct = Counter(num)
        print(dct)
        for i in range(len(num)):
            if dct[str(i)] != int(num[i]):
                print(dct[i], num[i])
                return False
        return True


print(Solution().digitCount("1210"))
