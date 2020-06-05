from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, cols = len(matrix), len(matrix[0])

        visited = [[False] * cols for _ in range(rows)]

        total = rows * cols
        ans = [0] * total
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

        row = col = index = 0
        for i in range(total):
            ans[i] = matrix[row][col]
            visited[row][col] = True
            next_row = row + direction[index][0]
            next_col = col + direction[index][1]
            if not (0 <= next_row < rows and 0 <= next_col < cols and not visited[next_row][
                next_col]):
                index = (index + 1) % 4

            row += direction[index][0]
            col += direction[index][1]
        return ans

    def spiralOrder_2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test = Solution()
    print(test.spiralOrder(matrix))
