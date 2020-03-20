class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        num = []
        for i in range(len(S) + 1):
            num.append(i)

        l = 0
        r = len(S)

        rst = list()
        for s in list(S):
            if s == 'I':
                rst.append(num[l])
                l += 1
            if s == 'D':
                rst.append(num[r])
                r -= 1
        rst.append(num[r])
        return rst


if __name__ == '__main__':
    S = "IDID"
    test = Solution()
    print(test.diStringMatch(S))
