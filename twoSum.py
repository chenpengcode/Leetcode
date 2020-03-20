from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_dict = dict()
        for i in range(len(nums)):
            num = target - nums[i]
            if num in tmp_dict.keys():
                return [tmp_dict[num], i]
            tmp_dict[nums[i]] = i


if __name__ == '__main__':
    test_list = [2, 7, 11, 16]
    rst = Solution().twoSum(test_list, 9)
    print(rst)
