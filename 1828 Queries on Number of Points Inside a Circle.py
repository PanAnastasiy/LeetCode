class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]])\
            -> list[int]:
        answer = []
        for query in queries:
            count = 0
            for point in points:
                if ((query[1] - point[1])**2 + (query[0] - point[0])**2)**0.5 <= query[2]:
                    count += 1
            answer.append(count)
        return answer
