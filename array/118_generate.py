from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(ans[i - 1][j] + ans[i - 1][j - 1])
            tmp.append(1)
            ans.append(tmp)
        return ans

    def generate_2(self, numRows: int) -> List[List[int]]:
        ans = []

        for row_num in range(numRows):
            row = [0 for i in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = ans[row_num - 1][j - 1] + ans[row_num - 1][j]
            ans.append(row)

        return ans


if __name__ == '__main__':
    test = Solution()
    num = 5
    print(test.generate(num))
