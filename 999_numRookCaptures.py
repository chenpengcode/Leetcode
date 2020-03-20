class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = col = 0
        list_row = list()
        list_col = list()

        for i in board:
            if 'R' in i:
                row = board.index(i)
                list_row = list(i)
                for j in list(i):
                    if j == 'R':
                        col = i.index(j)
        for i in board:
            list_col.append(list(i)[col])

        cnt = 0

        i = col - 1
        while i >= 0:
            if list_row[i] == 'B':
                break
            if list_row[i] == 'P':
                cnt += 1
                break
            i -= 1
        j = col + 1
        while j < len(list_row):
            if list_row[j] == 'B':
                break
            if list_row[j] == 'P':
                cnt += 1
                break
            j += 1

        i = row - 1
        while i >= 0:
            if list_col[i] == 'B':
                break
            if list_col[i] == 'P':
                cnt += 1
                break
            i -= 1

        j = row + 1
        while j < len(list_col):
            if list_col[j] == 'B':
                break
            if list_col[j] == 'P':
                cnt += 1
                break
            j += 1
        return cnt


if __name__ == '__main__':
    test = Solution()
    board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

    print(test.numRookCaptures(board))
