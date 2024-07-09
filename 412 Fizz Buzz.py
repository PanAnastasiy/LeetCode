from typing import List


class Solution(object):

    @staticmethod
    def fizzBuzz(n: int) -> List[str]:
        answer = ['FizzBuzz' if i % 15 == 0 else str(i) for i in range(1, n+1)]
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3:
                answer[i - 1] = 'Buzz'
            elif i % 3 == 0 and i % 5:
                answer[i - 1] = 'Fizz'
        return answer


Solution.fizzBuzz(10)
