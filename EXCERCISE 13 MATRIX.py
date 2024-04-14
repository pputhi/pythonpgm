row1 = ['1', '1', '1']
row2 = ['1', '1', '1']
row3 = ['1', '1', '1']
print(f"{row1}\n{row2}\n{row3}")

# Create a list of lists representing the grid
grid = [row1, row2, row3]

position = input("Enter the position: ")

row_position = int(position[0]) - 1
column_position = int(position[1]) - 1

# Set the selected position in the grid to 'X'
grid[row_position][column_position] = 'X'

print(f"{row1}\n{row2}\n{row3}")

grid [2][2]='Z'
print(f"{row1}\n{row2}\n{row3}")
