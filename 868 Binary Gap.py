class Solution:
    def binaryGap(self, n: int) -> int:
         bits =bin(n)[2:]
         for i in range(len(bits)):
             if '1' + '0' * (len(bits) - 2 - i) + '1' in bits:
               return len(bits) - 1 - i
         return 0



print(Solution().binaryGap(4))