from collections import deque

# ==========================================
# LAB 4 - TASK 3: 8-PUZZLE SOLVER USING BFS
# ==========================================

def get_neighbors_8_puzzle(state):
    """
    Generates all valid successor states by moving the blank tile (0) Up, Down, Left, or Right.
    State is represented as a 9-element tuple for 3x3 grid layout.
    """
    blank_idx = state.index(0)
    r, c = blank_idx // 3, blank_idx % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []
    
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            state_list = list(state)
            # Swap blank tile with adjacent number tile
            state_list[blank_idx], state_list[n_idx] = state_list[n_idx], state_list[blank_idx]
            neighbors.append(tuple(state_list))
            
    return neighbors

def solve_8_puzzle_bfs(initial_state, goal_state):
    """
    Solves 8-puzzle using Breadth-First Search (BFS) to guarantee minimum number of moves.
    Returns the sequence of states from start to goal.
    """
    visited = {initial_state}
    queue = deque([[initial_state]])
    
    while queue:
        path = queue.popleft()
        curr_state = path[-1]
        
        if curr_state == goal_state:
            return path
            
        for neighbor in get_neighbors_8_puzzle(curr_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
                
    return None

def print_8_puzzle_state(state):
    """Prints 9-tuple as a 3x3 grid."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else " " for x in state[i:i+3]]
        print(" ".join(row))

def main():
    # Initial State: 2 8 3 / 1 6 4 / 7 _ 5
    initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)
    # Goal State: 1 2 3 / 8 _ 4 / 7 6 5
    goal_state    = (1, 2, 3, 8, 0, 4, 7, 6, 5)

    print("================ 8-PUZZLE SOLVER (TASK 3) ================")
    print("Initial State:")
    print_8_puzzle_state(initial_state)
    print("\nGoal State:")
    print_8_puzzle_state(goal_state)
    print("-" * 50)

    puzzle_path = solve_8_puzzle_bfs(initial_state, goal_state)

    if puzzle_path:
        total_moves = len(puzzle_path) - 1
        print(f"Solution Found via BFS!")
        print(f"Total Number of Moves: {total_moves}\n")
        print("Sequence of States:")
        for step, state in enumerate(puzzle_path):
            print(f"--- Step {step} ---")
            print_8_puzzle_state(state)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
