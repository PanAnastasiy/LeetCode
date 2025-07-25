# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

answer = 6


def guess(n):
    if n == answer:
        return 0
    elif n > answer:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            number = guess(mid)
            if number == 0:
                return mid
            elif number == 1:
                left = mid + 1
            else:
                right = mid - 1




print(Solution().guessNumber(10))
