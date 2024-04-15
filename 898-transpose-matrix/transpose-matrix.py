class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Approach: 
        column = len(matrix[0])
        row = len(matrix)

        transposed = []

        for i in range(column):
            temp_row = []
            for j in range(row):
                temp_row.append(matrix[j][i])
            transposed.append(temp_row)
            
        return transposed
                 