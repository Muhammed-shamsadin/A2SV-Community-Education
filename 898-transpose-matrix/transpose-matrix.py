class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = [[0 for i in range(rows)] for i in range(cols)]

        for col in range(rows):
            for row in range(cols):
                res[row][col] = matrix[col][row]

        return res



