maze = []

# Reading the maze from the input file
with open("input.txt", 'r') as file:
    for line in file:
        row = list(line.strip().split())
        maze.append(row)

maze = [list(row[0]) for row in maze]

def count_x_pattern_mas_in_maze(maze):
    # Dimensions of the maze
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0

    word_forward = "MAS"
    word_backward = "SAM"
    word_len = len(word_forward)
    count = 0

    # Function to check for a word in a diagonal direction
    def check_word_in_diagonal(start_row, start_col, delta_row, delta_col, word):
        for i in range(word_len):
            row = start_row + i * delta_row
            col = start_col + i * delta_col
            if row < 0 or row >= rows or col < 0 or col >= cols or maze[row][col] != word[i]:
                return False
        return True

    # Check for "X" patterns
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # Check if (r, c) can be the center of an "X" formed by two "MAS" or "SAM"
            
            # Check top-left to bottom-right diagonal (forward "MAS")
            diagonal1_forward = (r - 1 >= 0 and c - 1 >= 0 and r + 1 < rows and c + 1 < cols and
                                 check_word_in_diagonal(r - 1, c - 1, 1, 1, word_forward))
            
            # Check top-left to bottom-right diagonal (backward "SAM")
            diagonal1_backward = (r - 1 >= 0 and c - 1 >= 0 and r + 1 < rows and c + 1 < cols and
                                  check_word_in_diagonal(r - 1, c - 1, 1, 1, word_backward))
            
            # Check top-right to bottom-left diagonal (forward "MAS")
            diagonal2_forward = (r - 1 >= 0 and c + 1 < cols and r + 1 < rows and c - 1 >= 0 and
                                 check_word_in_diagonal(r - 1, c + 1, 1, -1, word_forward))
            
            # Check top-right to bottom-left diagonal (backward "SAM")
            diagonal2_backward = (r - 1 >= 0 and c + 1 < cols and r + 1 < rows and c - 1 >= 0 and
                                  check_word_in_diagonal(r - 1, c + 1, 1, -1, word_backward))
            
            # Valid combinations of diagonals forming an "X" pattern:
            # 1. Both diagonals are forward "MAS"
            if diagonal1_forward and diagonal2_forward:
                count += 1
            # 2. Both diagonals are backward "SAM"
            if diagonal1_backward and diagonal2_backward:
                count += 1
            # 3. One diagonal is forward "MAS", the other is backward "SAM"
            if diagonal1_forward and diagonal2_backward:
                count += 1
            if diagonal1_backward and diagonal2_forward:
                count += 1

    return count

# Example usage

result = count_x_pattern_mas_in_maze(maze)
print(f"Number of 'X' patterns with 'MAS': {result}")
