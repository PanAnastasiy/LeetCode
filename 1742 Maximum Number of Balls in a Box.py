
class Solution(object):

    @staticmethod
    def countBalls(lowLimit: int, highLimit: int) -> int:
        data = {}
        for ball in range(lowLimit, highLimit + 1):
            ball_sum = sum(list(map(int, list(str(ball)))))
            if ball_sum not in data:
                data[ball_sum] = 1
            else:
                data[ball_sum] += 1
        return max(data.values())


print(Solution.countBalls(1, 10))
