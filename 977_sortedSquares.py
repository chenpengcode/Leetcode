class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return None
        rst = []

        len_a = len(A)
        j = 0
        while j < len_a and A[j] < 0:
            j += 1
        i = j - 1

        while i >= 0 and j < len_a:
            if A[i] * A[i] < A[j] * A[j]:
                rst.append(A[i] * A[i])
                i -= 1
            else:
                rst.append(A[j] * A[j])
                j += 1
        while i >= 0:
            rst.append(A[i] * A[i])
            i -= 1
        while j < len_a:
            rst.append(A[j] * A[j])
            j += 1

        return rst


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    test = Solution()
    print(test.sortedSquares(A))
