class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack = []
        array = []
        i = 1
        while array != target:
            array.append(i)
            stack.append('Push')
            if array[-1] not in target:
                array.pop()
                stack.append('Pop')
            i += 1
        return stack
