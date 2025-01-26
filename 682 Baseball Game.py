class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for operation in operations:
            if operation.lstrip('-').isdigit():
                record.append(int(operation))
            elif operation == 'C':
                record.pop()
            elif operation == 'D':
                record.append(record[-1] * 2)
            else:
                record.append(record[-1] + record[-2])
        return sum(record)


print(Solution().calPoints(["5", "2", "C", "D", "+"]))
print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(Solution().calPoints(["1", "C"]))
