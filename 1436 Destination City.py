class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        data = {path[0]: path[1] for path in paths}
        city = paths[0][0]
        while data.get(city, 0):
            city = data[city]
        return city


sol = Solution()
print(sol.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
