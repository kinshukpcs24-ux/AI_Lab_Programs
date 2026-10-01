
def solve_dfs(start_state, goal_state):
    # Stack stores tuples of (current_board, path_of_moves)
    stack = [(start_state, [])]
    visited = set()
    
    while stack:
        current_board, path = stack.pop()
        
        # Check if we reached the goal
        if current_board == goal_state:
            return path + [current_board]
            
        board_tuple = tuple(current_board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        
        # Find the index of the blank space (0)
        zero_index = current_board.index(0)
        row, col = divmod(zero_index, 3)
        
        # Possible movements: Up, Down, Left, Right
        moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
        
        # Generate neighbors (reverse order or normal order depending on desired branch preference)
        for dr, dc, move_name in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero_index = new_row * 3 + new_col
                
                # Swap 0 with the adjacent tile
                new_board = list(current_board)
                new_board[zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[zero_index]
                
                if tuple(new_board) not in visited:
                    stack.append((new_board, path + [current_board]))
                    
    return None

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

# Example usage:
# 0 represents the empty tile
initial_state = [2, 8, 3, 
                 1, 6, 4, 
                 0, 7, 5]

goal_state = [1, 2, 3, 
              8, 0, 4, 
              7, 6, 5]

solution = solve_dfs(initial_state, goal_state)

if solution:
    print(f"Solution found in {len(solution) - 1} moves!\n")
    for step, board in enumerate(solution):
        print(f"Step {step}:")
        print_board(board)
else:
    print("No solution found.")
