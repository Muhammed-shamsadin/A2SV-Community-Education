class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        X , Y ---> (Y , M - 1 - X)

        [0 0  1 , 0 0  2 , 0 0  0]

        FOR X:
            FOR Y:
                X,Y
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # ans = [[0 for i in range(cols)] for i in range(rows)]

        # for row in range(rows):
        #     for col in range(cols):
        #         ans[col][rows-1-row] = matrix[row][col]
                
        # for row in range(rows):
        #     for col in range(cols):
        #         matrix[row][col] = ans[row][col]

        # After transposing a ROW, inorder to avoid transposing it again. we should start
        # our inner loop from the next row and not again from the beginning

        for row in range(rows):
            for col in range(row, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(rows):
            matrix[row].reverse()
        
        