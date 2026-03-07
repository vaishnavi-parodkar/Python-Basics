def goal_test(node, goal):
    return node == goal


def move_gen(graph, node):
    return graph[node]


def best_first_search(graph, start, goal, heuristic):
    open_list = [[start]]   # stores paths
    closed = []
    traversal = []

    while open_list:

       
        best_path = open_list[0]
        best_index = 0

        for i in range(len(open_list)):
            node = open_list[i][-1]
            if heuristic[node] < heuristic[best_path[-1]]:
                best_path = open_list[i]
                best_index = i

        open_list.pop(best_index)
        node = best_path[-1]

        if node not in closed:
            closed.append(node)
            traversal.append(node)

            if goal_test(node, goal):
                return best_path, closed, traversal

            # Add children
            for child in move_gen(graph, node):
                if child not in closed:
                    new_path = best_path + [child]
                    open_list.append(new_path)

    return None, closed, traversal



graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    children = input("Enter neighbours: ").split()
    h = int(input("Enter heuristic value: "))

    graph[node] = children
    heuristic[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result, closed, traversal = best_first_search(graph, start, goal, heuristic)


if result:
    print("\nPath found using Best First Search:")
    print("Start:", start)
    print("Goal:", goal)
    print("Best Path:", "->".join(result))
    print("Closed List:", "->".join(closed))
    print("Traversal Order:", "->".join(traversal))
else:
    print("\nNo path found from", start, "to", goal)
    print("Closed List:", "->".join(closed))
    print("Traversal Order:", "->".join(traversal))