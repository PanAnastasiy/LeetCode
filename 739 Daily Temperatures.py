class Solution(object):
    @staticmethod
    def dailyTemperatures(temperatures):
        answers = []
        for i in range(1, len(temperatures) + 1):
            flag = False
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i - 1]:
                    answers.append(j - i + 1)
                    flag = True
                    break
            if not flag or i == len(temperatures):
                answers.append(0)
        return answers

print(str(-56)[1::-1])
print(Solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
