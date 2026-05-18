from collections import deque

# Capacities of jugs
CAPACITY_3 = 3
CAPACITY_4 = 4

# Goal: one jug contains exactly 2 liters
GOAL = 2

def bfs_water_jug():
    # Initial state: (3L jug, 4L jug)
    start = (0, 0)

    # Queue for BFS
    queue = deque()

    # Store: (state, path)
    queue.append((start, []))

    # Visited states
    visited = set()
    visited.add(start)

    while queue:
        (jug3, jug4), path = queue.popleft()

        # Goal check
        if jug3 == GOAL or jug4 == GOAL:
            print("Solution Found using BFS\n")

            for step_num, step in enumerate(path, start=1):
                print(f"Step {step_num}: {step}")

            print(f"\nFinal State: (3L={jug3}, 4L={jug4})")
            return

        # Generate all possible next states
        next_states = []

        # 1. Fill 3L jug
        next_states.append(((CAPACITY_3, jug4), "Fill 3L jug"))

        # 2. Fill 4L jug
        next_states.append(((jug3, CAPACITY_4), "Fill 4L jug"))

        # 3. Empty 3L jug
        next_states.append(((0, jug4), "Empty 3L jug"))

        # 4. Empty 4L jug
        next_states.append(((jug3, 0), "Empty 4L jug"))

        # 5. Pour 3L -> 4L
        transfer = min(jug3, CAPACITY_4 - jug4)
        new_jug3 = jug3 - transfer
        new_jug4 = jug4 + transfer
        next_states.append(
            ((new_jug3, new_jug4), "Pour 3L -> 4L")
        )

        # 6. Pour 4L -> 3L
        transfer = min(jug4, CAPACITY_3 - jug3)
        new_jug4 = jug4 - transfer
        new_jug3 = jug3 + transfer
        next_states.append(
            ((new_jug3, new_jug4), "Pour 4L -> 3L")
        )

        # Process next states
        for state, action in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [action]))

# Run BFS solver
bfs_water_jug()

