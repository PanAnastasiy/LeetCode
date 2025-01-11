class Solution:
    def smallestNumber(self, n: int) -> int:
        return self.convertToBin(n)

    def convertToBin(self, n: int) -> int:
        str_number = ''
        while n:
            str_number += str(n % 2)
            n //= 2
        print('bin - ', str_number)
        return self.makeCorrect(str_number)

    def makeCorrect(self, n: str) -> int:
        n = n.replace('0', '1')
        print('correct - ', n)
        return self.convertToNum(n)

    def convertToNum(self, n: str) -> int:
        result_num = 0
        for index in range(len(n)):
            result_num += int(2**(len(n) - index - 1))
        print('num - ', result_num)
        return result_num


print(Solution().smallestNumber(5))
