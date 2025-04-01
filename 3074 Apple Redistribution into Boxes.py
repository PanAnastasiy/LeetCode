class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        print(capacity)
        for i in range(len(capacity)):
            if sum(capacity[:i + 1]) > total - 1:
                return i + 1


print(Solution().minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]))
print(Solution().minimumBoxes([5, 5, 5], [2, 4, 2, 7]))
