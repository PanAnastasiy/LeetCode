

class Solution(object):

    @staticmethod
    def two_indices_sum(lst_nums, target):
        for index_1 in range(len(lst_nums)):
            for index_2 in range(index_1 + 1, len(lst_nums)):
                if lst_nums[index_1] + lst_nums[index_2] == target:
                    return [index_1, index_2]


print(Solution.two_indices_sum([3, 2, 4, 15], 6))
