class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        answer = 0
        boxTypes.sort(key=lambda x: -x[1])
        for boxType in boxTypes:
            if truckSize > boxType[0]:
                truckSize -= boxType[0]
                answer += boxType[0] * boxType[1]
            else:
                answer += truckSize * boxType[1]
                break
        return answer


print(Solution().maximumUnits([[1,3],[2,2],[3,1]], 4))
print(Solution().maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))


