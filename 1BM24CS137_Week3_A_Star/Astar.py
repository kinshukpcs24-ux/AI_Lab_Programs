import heapq

class PuzzleNode:
    def __init__(self, state, g=0, h=0, parent=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def get_blank_pos(self):
        idx = self.state.index(0)
        return idx // 3, idx % 3

def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        val = state[i]
        if val != 0:
            current_row, current_col = i // 3, i % 3
            goal_idx = goal.index(val)
            goal_row, goal_col = goal_idx // 3, goal_idx % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbors(node, goal):
    neighbors = []
    state = list(node.state)
    r, c = node.get_blank_pos()
    blank_idx = r * 3 + c

    moves = [
        (-1, 0), # Up
        (1, 0),  # Down
        (0, -1), # Left
        (0, 1)   # Right
    ]

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            neighbor_idx = nr * 3 + nc
            new_state = state[:]
            # Swap blank space (0) with neighbor
            new_state[blank_idx], new_state[neighbor_idx] = new_state[neighbor_idx], new_state[blank_idx]

            t_state = tuple(new_state)
            g = node.g + 1
            h = manhattan_distance(t_state, goal)
            neighbors.append(PuzzleNode(t_state, g, h, node))

    return neighbors

def print_board(state):
    for i in range(0, 9, 3):
        print(f" {state[i]} {state[i+1]} {state[i+2]} ")
    print()

def solve_8_puzzle(start_state, goal_state):
    start_tuple = tuple(start_state)
    goal_tuple = tuple(goal_state)

    start_node = PuzzleNode(start_tuple, 0, manhattan_distance(start_tuple, goal_tuple))

    open_list = []
    heapq.heappush(open_list, start_node)

    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_tuple:
            # Reconstruct path
            path = []
            curr = current_node
            while curr:
                path.append(curr)
                curr = curr.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor in get_neighbors(current_node, goal_tuple):
            if neighbor.state in closed_set:
                continue
            heapq.heappush(open_list, neighbor)

    return None

# Define Start and Goal States (0 represents the empty tile)
# 2 8 3
# 1 6 4
# 7 0 5
start = [2, 8, 3, 1, 6, 4, 7, 0, 5]

# 1 2 3
# 8 0 4
# 7 6 5
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

solution = solve_8_puzzle(start, goal)

if solution:
    print(f"Solved in {len(solution) - 1} steps:\n")
    for step, node in enumerate(solution):
        print(f"--- Step {step} ---")
        print_board(node.state)
        print(f"g (cost so far)  = {node.g}")
        print(f"h (heuristic)    = {node.h}")
        print(f"f (total cost)   = {node.f}")
        print("-" * 20)
else:
    print("No solution found.")
