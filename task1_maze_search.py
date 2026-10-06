import heapq
from collections import deque

# ==========================================
# LAB 4 - TASK 1 & TASK 2: MAZE PATHFINDING
# Algorithms: BFS, DFS, UCS
# ==========================================

maze = [
    "S . . # . .",
    ". # . # . .",
    ". # . . . .",
    ". # # # # .",
    ". . . . # G",
]

def maze_to_graph(maze):
    """
    Converts a grid maze into an adjacency list graph representation.
    Nodes are (row, col) tuples for open path cells.
    """
    rows = [row.split() for row in maze]
    graph = {}
    start = None
    goal = None
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell == "#":
                continue
            if cell == "S":
                start = (r, c)
            elif cell == "G":
                goal = (r, c)
            neighbors = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(rows) and 0 <= nc < len(rows[0]) and rows[nr][nc] != "#":
                    neighbors.append((nr, nc))
            graph[(r, c)] = neighbors
    return graph, start, goal

# 1. Breadth-First Search (Queue - FIFO)
def bfs(graph, start, goal):
    visited = {start}
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

# 2. Depth-First Search (Stack / Recursion - LIFO)
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result
    return None

# 3. Uniform-Cost Search (Priority Queue - Min Heap by g(n))
def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    visited = {}
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal:
            return path, cost
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        for neighbor in graph.get(node, []):
            step_cost = 1  # Unit step cost
            heapq.heappush(frontier, (cost + step_cost, neighbor, path + [neighbor]))
    return None, float("inf")

def main():
    graph, start, goal = maze_to_graph(maze)
    print("================ MAZE SEARCH ================")
    print(f"Start State (S): {start}")
    print(f"Goal State  (G): {goal}\n")

    # BFS
    bfs_path = bfs(graph, start, goal)
    print("1. Breadth-First Search (BFS):")
    print(f"   Path: {bfs_path}")
    print(f"   Nodes in Path: {len(bfs_path) if bfs_path else 0}")
    print(f"   Path Length (Steps): {len(bfs_path) - 1 if bfs_path else 0}\n")

    # DFS
    dfs_path = dfs(graph, start, goal)
    print("2. Depth-First Search (DFS):")
    print(f"   Path: {dfs_path}")
    print(f"   Nodes in Path: {len(dfs_path) if dfs_path else 0}")
    print(f"   Path Length (Steps): {len(dfs_path) - 1 if dfs_path else 0}\n")

    # UCS
    ucs_path, ucs_cost = ucs(graph, start, goal)
    print("3. Uniform-Cost Search (UCS):")
    print(f"   Path: {ucs_path}")
    print(f"   Nodes in Path: {len(ucs_path) if ucs_path else 0}")
    print(f"   Path Cost (Steps): {ucs_cost}\n")


if __name__ == "__main__":
    main()
