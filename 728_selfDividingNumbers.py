class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        rst = []

        for i in range(left, right + 1):
            if self.include_0(i):
                continue
            div = []
            val = i
            while i != 0:
                ele = i % 10
                div.append(ele)
                i //= 10
            flag = True
            for j in range(len(div)):
                if val % div[j] != 0:
                    flag = False
                    break
            if flag:
                rst.append(val)
        return rst

    def include_0(self, i):
        rst = False
        while i != 0:
            if i % 10 == 0:
                rst = True
                break
            i //= 10
        return rst


if __name__ == '__main__':
    left = 1
    right = 22
    test = Solution()
    print(test.selfDividingNumbers(left, right))
