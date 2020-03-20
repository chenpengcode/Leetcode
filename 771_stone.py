class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        rst = 0
        # list_j = J.split(',')
        # list_s = S.split(',')
        # print(list_j)
        for j in J:
            for s in S:
                if j == s:
                    rst += 1

        return rst


if __name__ == '__main__':
    J = 'aA'
    S = 'aAAbbbb'
    test = Solution()
    print(test.numJewelsInStones(J, S))
