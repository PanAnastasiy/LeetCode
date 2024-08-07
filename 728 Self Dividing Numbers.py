from typing import List


class Solution:
    @staticmethod
    def selfDividingNumbers(left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            original_num = num
            while num > 0:
                digit = num % 10
                if digit == 0 or original_num % digit != 0:
                    return False
                num //= 10
            return True

        answer = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                answer.append(num)
        return answer


print(Solution.selfDividingNumbers(1, 22))
