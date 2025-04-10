import heapq


class SeatManager:

    def __init__(self, n: int):
        self.seats = [0] * n
        self.un_reserve = []
        self.pointer = 0

    def reserve(self) -> int:
        if self.un_reserve:
            seat = heapq.heappop(self.un_reserve)
        else:
            seat = self.pointer
            self.pointer += 1
            self.seats[seat] = 1
        return seat + 1

    def unreserve(self, seatNumber: int) -> None:
        self.seats[seatNumber - 1] = 0
        heapq.heappush(self.un_reserve, seatNumber - 1)


obj = SeatManager(5)
param_1 = obj.reserve()
obj.unreserve(1)