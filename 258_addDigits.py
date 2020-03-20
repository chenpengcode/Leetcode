class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = []
        while True:
            if num:
                res.append(num % 10)
                num //= 10
            else:
                num = sum(res)
                res.clear()
                if num < 10:
                    break
        return num


if __name__ == '__main__':
    test = Solution()
    print(test.addDigits(38))
