class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            row.reverse()

        for i in range(len(A)):
            for j in range(len(A[0])):
                # print(A[i][j])
                if A[i][j] == 0:
                    A[i][j] = 1
                elif A[i][j] == 1:
                    A[i][j] = 0
        return A


if __name__ == '__main__':
    test = Solution()
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(test.flipAndInvertImage(A))
