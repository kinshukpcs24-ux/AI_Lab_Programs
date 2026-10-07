class EightPuzzleIDS:
    def __init__(self, initial_state, goal_state):
        self.initial_state = tuple(initial_state)
        self.goal_state = tuple(goal_state)
        self.moves = {
            'UP': -3,
            'DOWN': 3,
            'LEFT': -1,
            'RIGHT': 1
        }

    def get_neighbors(self, state):
        neighbors = []
        blank_idx = state.index(0)
        row, col = blank_idx // 3, blank_idx % 3

        for move, shift in self.moves.items():
            if move == 'UP' and row == 0: continue
            if move == 'DOWN' and row == 2: continue
            if move == 'LEFT' and col == 0: continue
            if move == 'RIGHT' and col == 2: continue

            new_idx = blank_idx + shift
            new_state = list(state)
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbors.append((tuple(new_state), move))

        return neighbors

    def depth_limited_search(self, state, depth, path, visited):
        if state == self.goal_state:
            return path

        if depth <= 0:
            return None

        for neighbor, move in self.get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                result = self.depth_limited_search(neighbor, depth - 1, path + [move], visited)
                if result is not None:
                    return result
                visited.remove(neighbor)

        return None

    def solve(self, max_depth=50):
        for depth in range(max_depth):
            visited = {self.initial_state}
            result = self.depth_limited_search(self.initial_state, depth, [], visited)
            if result is not None:
                return result, depth
        return None, None

def print_board(state):
    """Prints the flat 1D tuple formatted beautifully as a 3x3 matrix grid."""
    for i in range(0, 9, 3):
        # Join elements with padding to ensure alignment even if double digits exist
        print("  ".join(map(str, state[i:i+3])))
    print("-" * 12)

def animate_solution(start_state, move_list, moves_dict):
    """Simulates and prints the board state change for each action taken."""
    current_state = list(start_state)

    print("Initial State:")
    print_board(current_state)

    for i, move in enumerate(move_list, 1):
        blank_idx = current_state.index(0)
        shift = moves_dict[move]
        new_idx = blank_idx + shift

        # Swap tiles to progress the board state
        current_state[blank_idx], current_state[new_idx] = current_state[new_idx], current_state[blank_idx]

        print(f"Step {i}: Move Blank '{move}'")
        print_board(current_state)

# Main Execution Script
if __name__ == "__main__":
    # Your 3x3 layout translated to flattened row-major tuples
    initial = (2, 8, 3,
               1, 6, 4,
               0, 7, 5)

    final   = (1, 2, 3,
               8, 0, 4,
               7, 6, 5)

    solver = EightPuzzleIDS(initial, final)
    solution, depth_found = solver.solve()

    if solution is not None:
        print(f"Solution found at depth level: {depth_found} moves!\n")
        # Visualise the grid step by step
        animate_solution(initial, solution, solver.moves)
    else:
        print("No solution found within search parameters.")
