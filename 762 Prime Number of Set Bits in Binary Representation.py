class Solution:

    def isPrime(self, n: int) -> bool:
        print(n)
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return n != 1

    def countPrimeSetBits(self, left: int, right: int) -> int:
        answer = 0
        for number in range(left, right + 1):
            answer += self.isPrime(bin(number)[2:].count('1'))
        return answer


print(Solution().countPrimeSetBits(6, 10))