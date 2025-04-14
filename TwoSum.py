class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_nums = []
        indice_dict = {}
        for index, value in enumerate(nums):
            sub_nums.append(target - value )
            indice_dict[value] = index

        for index, value in enumerate(sub_nums):
            if value in indice_dict:
                if indice_dict.get(value) != index:
                    return [index, indice_dict.get(value)]
