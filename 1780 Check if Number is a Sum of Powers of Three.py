import numpy as np




class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return '2' not in np.base_repr(n, base=3)


print(Solution().checkPowersOfThree(12))
print(Solution().checkPowersOfThree(91))
print(Solution().checkPowersOfThree(21))