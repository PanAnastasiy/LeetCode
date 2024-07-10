
class Solution:

    @staticmethod
    def fib(n: int) -> int:
        if not n:
            return 0
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[-1]


print(Solution.fib(4))
