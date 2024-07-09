from typing import List


class Solution(object):

    @staticmethod
    def averageWaitingTime(customers: List) -> float:
        time, total_time = [],  customers[0][0]
        for index in range(len(customers)):
            if total_time < customers[index][0]:
                total_time = customers[index][0]
            time.append(total_time + customers[index][1] - customers[index][0])
            total_time += customers[index][1]
        return sum(time) / len(time)


print(Solution.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))

