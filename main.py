

class Solution(object):

    @staticmethod
    def backspace_compare(s, t):
        first_pointer, second_pointer = 0, 0
        while '#' in s or '#' in t:
            if '#' in s and s[first_pointer] == '#':
                s = s.replace(s[first_pointer - 1:first_pointer + 1], '')
                first_pointer -= 1
            else:
                first_pointer += 1
            if '#' in t and t[second_pointer] == '#':
                t = t.replace(s[second_pointer - 1:second_pointer + 1], '')
                print(s[second_pointer - 1:second_pointer + 1])
                second_pointer -= 1
            else:
                second_pointer += 1
                print(t)
        return s == t


print(Solution.backspace_compare("ab##", "c#d#"))
