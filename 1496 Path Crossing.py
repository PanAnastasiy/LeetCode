class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        point = [0, 0]
        for direction in path:
            if direction == 'N':
                point[1] += 1
            elif direction == 'S':
                point[1] -= 1
            elif direction == 'E':
                point[0] -= 1
            else:
                point[0] += 1
            if tuple(point) in visited:
                return True
            else:
                visited.add(tuple(point))
        return False


print(Solution().isPathCrossing("NES"))