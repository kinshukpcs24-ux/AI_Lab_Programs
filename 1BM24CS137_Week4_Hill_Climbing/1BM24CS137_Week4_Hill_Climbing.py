import random

def get_h_score(state):
    """Calculate number of attacking pairs of queens."""
    n = len(state)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == (j - i):
                attacks += 1
    return attacks

def get_best_neighbor_with_logging(state):
    """Find the best neighbor state by swapping pairs of rows (nC2 combinations)."""
    n = len(state)
    current_h = get_h_score(state)
    best_neighbor = list(state)
    best_h = None
    
    print("\n  --- Evaluating all neighbors (nC2 swaps) ---")
    # Generate neighbors by swapping the columns of two rows (i and j)
    for i in range(n):
        for j in range(i + 1, n):
            temp = list(state)
            # Swap columns of row i and row j
            temp[i], temp[j] = temp[j], temp[i]
            temp_h = get_h_score(temp)
            print(f"  Candidate: Swap Row {i} and Row {j} -> State {temp} | Cost = {temp_h}")
            
            # Track the absolute best neighbor found in this neighborhood
            if best_h is None or temp_h < best_h:
                best_h = temp_h
                best_neighbor = temp
                    
    return best_neighbor, best_h

def hill_climbing_detailed(n, initial_state):
    """Runs hill climbing on a state using nC2 swaps. Returns (final_state, final_cost, best_neighbor_to_carry_over)."""
    state = list(initial_state)
    current_h = get_h_score(state)
    step = 0
    
    print(f"Starting State = {state} | Cost = {current_h}")
    
    while True:
        neighbor, neighbor_h = get_best_neighbor_with_logging(state)
        
        # If the best neighbor does not strictly improve current state, we are stuck.
        # We stop climbing, but we return this 'neighbor' as the best state to carry over.
        if neighbor_h >= current_h:
            print(f"\nNo better neighbor found (Best neighbor cost: {neighbor_h} >= Current cost: {current_h}).")
            return state, current_h, neighbor
            
        state = neighbor
        current_h = neighbor_h
        step += 1
        print(f"\nStep {step}: Selected State = {state} | Cost = {current_h}")

def solve_n_queens_with_carry_over(n, initial_state, max_attempts=10):
    """Run hill climbing. If stuck, use the best evaluated swap neighbor as the next start state."""
    current_start_state = list(initial_state)
    
    for attempt in range(1, max_attempts + 1):
        print(f"\n=== ATTEMPT {attempt} ===")
        final_state, cost, best_neighbor = hill_climbing_detailed(n, current_start_state)
        
        if cost == 0:
            print(f"\nSolution successfully found on Attempt {attempt}!")
            return final_state
            
        # Carry over the best overall neighbor evaluated in this attempt as the next start state
        print(f"Carrying over the best evaluated neighbor {best_neighbor} (Cost = {get_h_score(best_neighbor)}) to Attempt {attempt + 1}.")
        current_start_state = best_neighbor
        
    print("\nCould not find a solution within the maximum number of attempts.")
    return None

# Input variables
n = 4
initial_state = [3, 1, 2, 0]

solve_n_queens_with_carry_over(n, initial_state)
