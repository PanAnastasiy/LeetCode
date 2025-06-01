class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        squares = []
        for rect in rectangles:
            squares.append(min(rect))
        return squares.count(max(squares))


print(Solution().countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
