class Solution:
    def bit_square_sum(self, n):
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n //= 10
        return sum

    def isHappy(self, n: int) -> bool:
        tmp = set()

        while n != 1 and n not in tmp:
            tmp.add(n)
            n = self.bit_square_sum(n)

        return n == 1

    def isHappy_2(self, n: int) -> bool:
        slow, fast = n, self.bit_square_sum(n)
        while fast != 1 and slow != fast:
            slow = self.bit_square_sum(slow)
            fast = self.bit_square_sum(self.bit_square_sum(fast))

        return fast == 1


if __name__ == '__main__':
    n = 19
    test = Solution()
    print(test.isHappy_2(n))
