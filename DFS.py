def goal_test(node, goal):
    return node == goal


def move_gen(graph, node):
    return graph[node]


def dfs(graph, start, goal):
    open_list = [[start]]   # Stack
    closed = []
    traversal = []   # to store traversal order

    while open_list:
        path = open_list.pop()   # LIFO (Stack behavior)
        node = path[-1]

        if node not in closed:
            closed.append(node)
            traversal.append(node)

            if goal_test(node, goal):
                return path, closed, traversal

            # reverse to maintain input order in DFS
            for child in reversed(move_gen(graph, node)):
                new_path = path + [child]
                open_list.append(new_path)

    return None, closed, traversal


# ---- Input Section ----
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    children = input("Enter neighbours: ").split()
    graph[node] = children

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result, closed, traversal = dfs(graph, start, goal)

# ---- Output Section ----
if result:
    print("\nPath found using DFS:")
    print("Start:", start)
    print("Goal:", goal)
    print("Best Path:", "->".join(result))
    print("Closed List:", "->".join(closed))
    print("Traversal Order:", "->".join(traversal))
else:
    print("\nNo path found from", start, "to", goal)
    print("Closed List:", "->".join(closed))
    print("Traversal Order:", "->".join(traversal))