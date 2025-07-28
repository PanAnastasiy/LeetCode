import heapq
from math import isqrt


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            number = -heapq.heappop(gifts)
            heapq.heappush(gifts, -isqrt(number))
        return -sum(gifts)


print(Solution().pickGifts([25, 64, 9, 4, 100], 4))
