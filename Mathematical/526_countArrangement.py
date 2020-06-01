class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, N: int) -> int:
        nums = [0] * N
        for i in range(N):
            nums[i] = i + 1
        self.permute_2(nums, 0)
        return self.count

    def permute(self, nums, index):
        flag = True
        if index == len(nums) - 1:
            for i in range(1, len(nums) + 1):
                if nums[i - 1] % i != 0 and i % nums[i - 1] != 0:
                    flag = False
                    break
            if flag:
                self.count += 1

        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.permute(nums, index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    def permute_2(self, nums, index):
        if index == len(nums):
            self.count += 1

        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            if nums[index] % (index + 1) == 0 or (index + 1) % nums[index] == 0:
                self.permute_2(nums, index + 1)
            nums[index], nums[i] = nums[i], nums[index]


if __name__ == '__main__':
    N = 2
    test = Solution()
    print(test.countArrangement(N))
