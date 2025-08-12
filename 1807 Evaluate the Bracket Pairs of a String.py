class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dct = dict(knowledge)
        pointer = 0
        answer = ''
        key = ''
        flag = False
        while pointer < len(s):
            if s[pointer] == '(':
                flag = True
            elif s[pointer] == ')':
                answer += dct.get(key, '?')
                key = ''
                flag = False
            elif flag:
                key += s[pointer]
            else:
                answer += s[pointer]
            pointer += 1
        return answer






print(Solution().evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]))