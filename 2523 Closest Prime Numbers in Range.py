class Solution:

    def findPrimes(self, left: int, right: int) -> list[int]:
        if right < 2:
            return []

        is_prime = [True] * (right + 1)
        is_prime[0], is_prime[1] = False, False

        for num in range(2, int(right ** 0.5) + 1):
            if is_prime[num]:
                for multiple in range(num * num, right + 1, num):
                    is_prime[multiple] = False

        return [num for num in range(left, right + 1) if is_prime[num]]

    def closestPrimes(self, left: int, right: int) -> list[int]:
        answer = []
        primes = self.findPrimes(left, right)
        if len(primes) < 2:
            return [-1, -1]
        closest = 10000
        for index in range(1, len(primes)):
            if primes[index] - primes[index - 1] < closest:
                closest = primes[index] - primes[index - 1]
                answer = [primes[index - 1], primes[index]]
        return answer


print(Solution().closestPrimes(10, 19))
print(Solution().closestPrimes(4, 6))
print(Solution().closestPrimes(4, 7))