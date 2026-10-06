# Graph-Search-Algorithms-BFS-DFS-and-UCS
### Task 2: Algorithm Comparison & Theoretical Explanation

#### Summary Table

| Algorithm | Frontier Data Structure | Expansion Strategy | Path Length (Steps) | Optimal? |
| :--- | :--- | :--- | :--- | :--- |
| **BFS** | Queue (FIFO) | Shallowest node first | 9 steps | Yes (unit step costs) |
| **DFS** | Stack (LIFO / Recursion) | Deepest node first | 13 steps | No |
| **UCS** | Priority Queue (by $g(n)$) | Lowest path cost first | 9 steps | Yes |

#### Detailed Explanation

##### Why BFS Returns the Shortest Path:
* **Frontier management:** BFS maintains a FIFO Queue as its frontier.
* **Node expansion:** Nodes are popped and expanded in strict order of their depth level (shallowest first).
* **Cost relationship:** In unweighted grid graphs where all step costs are equal ($c=1$), depth level is directly proportional to path cost $g(n)$.
* **Optimality guarantee:** Therefore, the first time the goal node G is reached by BFS, it is guaranteed to be via the path with minimum depth (fewest edges).

##### Why UCS Returns the Shortest (Optimal) Path:
* **Frontier management:** UCS uses a Priority Queue ordered by accumulated path cost $g(n)$.
* **Node expansion:** Nodes with the lowest cumulative cost are popped and expanded first.
* **Unit cost behavior:** For uniform unit costs ($c=1$), $g(n)$ equals the step count, making node expansion order identical to BFS.
* **Optimality guarantee:** Crucially, UCS performs the goal test when a node is popped from the priority queue (expanded), not when generated. This guarantees that no unvisited path with a lower cumulative cost exists.

##### Why DFS May Return a Non-Optimal Path:
* **Frontier management:** DFS maintains a LIFO Stack (or recursive call stack).
* **Node expansion:** It explores along a single search path as deep as possible before backtracking.
* **Lack of evaluation:** It has no mechanism for evaluating depth or path cost $g(n)$.
* **In-maze behavior:** In this maze, DFS encountered the junction at (2, 4) and proceeded upward into (1, 4) -> (0, 4) -> (0, 5) -> (1, 5) -> (2, 5) before descending to the goal, creating a 13-step loop, whereas BFS/UCS took the direct route (2, 4) -> (2, 5) -> (3, 5) -> (4, 5) (9 steps).
