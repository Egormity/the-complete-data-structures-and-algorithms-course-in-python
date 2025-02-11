def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2): # // = Math.floor()
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # Save top element
            top = matrix[layer][i]

            # Move left element to top
            matrix[layer][i] = matrix[-i - 1][layer]

            # Move bottom element to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # Move right to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # Move top to right
            matrix[i][-layer - 1] = top
    return matrix

print(rotate_matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]))