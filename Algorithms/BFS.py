def goal_test(node, goal):
    return node == goal


def move_gen(graph, node):
    return graph[node]


def bfs(graph, start, goal):
    open_list = [[start]]
    closed = []
    traversal = []   # to store traversal order

    while open_list:
        path = open_list.pop(0)
        node = path[-1]

        if node not in closed:
            closed.append(node)
            traversal.append(node)   # record traversal

            if goal_test(node, goal):
                return path, closed, traversal

            for child in move_gen(graph, node):
                new_path = path + [child]
                open_list.append(new_path)

    return None, closed, traversal


graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    children = input("Enter neighbours: ").split()
    graph[node] = children

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result, closed, traversal = bfs(graph, start, goal)

if result:
    print("\nPath found using BFS:")
    print("Start:", start)
    print("Goal:", goal)
    print("Best Path:", "->".join(result))
    print("Closed List:", "->".join(closed))
    print("Traversal Order:", "->".join(traversal))
else:
    print("\nNo path found from", start, "to", goal)
    print("Closed List:", "->".join(closed))
    print("Traversal Order:", "->".join(traversal))