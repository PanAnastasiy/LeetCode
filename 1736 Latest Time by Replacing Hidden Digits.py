class Solution:
    def maximumTime(self, time: str) -> str:
        dct = {3: '5', 4: '9'}
        if time[:2] == '??':
            time = time.replace('?', '2', 1)
            time = time.replace('?', '3', 1)
        for i in range(len(time)):
            if time[i] == '?':
                if i == 0 and time[1] > '3':
                    time = time.replace('?', '1', 1)
                    continue
                if i == 0 and time[1] < '4':
                    time = time.replace('?', '2', 1)
                    continue
                if i == 1 and time[0] == '2':
                    time = time.replace('?', '3', 1)
                    continue
                if i == 1 and (time[0] == '1' or time[0] == '0'):
                    time = time.replace('?', '9', 1)
                    continue
                time = time.replace('?', dct[i], 1)
        return time


print(Solution().maximumTime("1?:22"))
