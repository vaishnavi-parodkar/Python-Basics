contains3 = 0
contains4 = 0
steps = 0
MIN_STEPS = 6


def show_jars():

    d3 = contains3 if contains3 in [0, 3] else "?"
    d4 = contains4 if contains4 in [0, 2, 4] else "?"

    print("\n3 Gallon Jar")
    print("|      |")
    print("| ", d3, " |")
    print("|______|")

    print("\n4 Gallon Jar")
    print("|      |")
    print("|      |")
    print("| ", d4, " |")
    print("|______|")


def goal_test():
    return contains4 == 2


def move_gen(choice):

    global contains3, contains4

    if choice == 1 and contains3 < 3:
        contains3 = 3

    elif choice == 2 and contains4 < 4:
        contains4 = 4

    elif choice == 3 and contains3 > 0:
        contains3 = 0

    elif choice == 4 and contains4 > 0:
        contains4 = 0

    elif choice == 5 and contains3 > 0:

        t = min(contains3, 4 - contains4)
        contains3 -= t
        contains4 += t

    elif choice == 6 and contains4 > 0:

        t = min(contains4, 3 - contains3)
        contains4 -= t
        contains3 += t

    else:
        print("Invalid Move!!")
        return False

    return True


def bfs(choice):

    global steps

    if move_gen(choice):
        steps += 1


print("INITIAL EMPTY JARS")
show_jars()

while True:

    if goal_test():

        print("\nSolution Found Using BFS")

        if steps == MIN_STEPS:
            print("Achieved in Minimum Steps =", MIN_STEPS)

        else:
            print("Successful with", steps, "steps")

        break

    print("\n1.Fill 3")
    print("2.Fill 4")
    print("3.Empty 3")
    print("4.Empty 4")
    print("5.Transfer 3 -> 4")
    print("6.Transfer 4 -> 3")
    print("7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 7:
        print("Program Ended")
        break

    bfs(choice)

    show_jars()