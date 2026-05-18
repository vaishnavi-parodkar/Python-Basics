CAPACITY_3 = 3
CAPACITY_4 = 4
# Goal
GOAL = 2
def dfs_water_jug():
    visited = set()
    def dfs(jug3, jug4, path):
        # Goal check
        if jug3 == GOAL or jug4 == GOAL:
            print(" Solution Found using DFS \n")
            for step_num, step in enumerate(path, start=1):
                print(f"Step {step_num}: {step}")
            print(f"\nFinal State: (3L={jug3}, 4L={jug4})")
            return True
        # Mark current state visited
        visited.add((jug3, jug4))
        # Generate next possible states
        next_states = []

        # 1. Fill 3L jug
        next_states.append(
            ((CAPACITY_3, jug4), "Fill 3L jug")
        )
        # 2. Fill 4L jug
        next_states.append(
            ((jug3, CAPACITY_4), "Fill 4L jug")
        )
        # 3. Empty 3L jug
        next_states.append(
            ((0, jug4), "Empty 3L jug")
        )
        # 4. Empty 4L jug
        next_states.append(
            ((jug3, 0), "Empty 4L jug")
        )
        # 5. Pour 3L -> 4L
        transfer = min(jug3, CAPACITY_4 - jug4)
        next_states.append(
            (
                (jug3 - transfer, jug4 + transfer),
                "Pour 3L -> 4L"
           )
        )
        # 6. Pour 4L -> 3L
        transfer = min(jug4, CAPACITY_3 - jug3)
        next_states.append(
            (
                (jug3 + transfer, jug4 - transfer),
                "Pour 4L -> 3L" )  )
        # DFS exploration
        for (new_jug3, new_jug4), action in next_states:
            if (new_jug3, new_jug4) not in visited:
                if dfs(
                    new_jug3,
                    new_jug4,
                    path + [action]
                ):
                    return True
        return False
    # Start DFS from (0,0)
    dfs(0, 0, [])
# Run DFS solver
dfs_water_jug()
