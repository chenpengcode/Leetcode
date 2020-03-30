from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_dict = dict()

        for i in range(len(nums)):
            n = target - nums[i]
            if n in tmp_dict and i != tmp_dict[n]:
                return [tmp_dict[n], i]
            tmp_dict[nums[i]] = i


if __name__ == '__main__':
    test = Solution()
    a = [2, 7, 11, 15]
    print(test.twoSum(a, 9))
