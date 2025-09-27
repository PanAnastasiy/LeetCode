class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        maxi = 0
        for first_point in range(len(points)):
            for second_point in range(first_point, len(points)):
                for third_point in range(second_point, len(points)):
                    x1, y1 = points[first_point]
                    x2, y2 = points[second_point]
                    x3, y3 = points[third_point]
                    maxi = max(maxi, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return maxi