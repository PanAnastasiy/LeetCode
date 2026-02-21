class Solution:

    def find_new_value_by_next(self, code: list[int], index: int, k: int) -> int:
        total = 0
        for i in range(index + 1, index + k + 1, 1):
            total += code[i % len(code)]
        return total

    def find_new_value_by_prev(self, code: list[int], index: int, k: int) -> int:
        total = 0
        for i in range(index - 1, index + k - 1, -1):
            total += code[i % len(code)]
        return total

    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k > 0:
            return [self.find_new_value_by_next(code, i, k) for i in range(len(code))]
        elif k < 0:
            return [self.find_new_value_by_prev(code, i, k) for i in range(len(code))]
        else:
            return [0] * len(code)


print(Solution().decrypt([2, 4, 9, 3], -2)) # [12, 5, 6, 13]
print(Solution().decrypt([5, 7, 1, 4], 3)) # [12, 10, 16, 13]
