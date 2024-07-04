
class Solution(object):

    @staticmethod
    def numSquares(n):
        prefect_squares = [i**2 for i in range(1, int(n**0.5 + 1))]
        print(prefect_squares)
        for number in range(n):
            pass
        return 1


Solution.numSquares()
