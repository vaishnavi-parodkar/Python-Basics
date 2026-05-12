contains3 = 0
contains4 = 0
steps = 0
MIN_STEPS = 6


def show_jars():
    global contains3, contains4

    display3 = contains3 if contains3 in [0, 3] else "?"
    display4 = contains4 if contains4 in [0, 2, 4] else "?"

    print("\nCurrent State: ")
    print("3 Gallon jar:")
    print("|        |")
    print("|  ", display3, "   |")
    print("|________|")

    print("\n4 Gallon jar:")
    print("|        |")
    print("|        |")
    print("|  ", display4, "   |")
    print("|________|")


show_jars() #initially empty jars

while True:

    if contains4 == 2:
        if steps == MIN_STEPS:
            print("You achieved solution with minimum steps!!", MIN_STEPS)
        else:
            print("Solution found, but not with minimum steps.")
            print("4 Gallon jar contains 2 gallons.")
            print("Total steps = ", steps)
        break

    print("\n==== Water Jug Menu ====")
    print("1. Fill 3 gallon fully")
    print("2. Fill 4 gallon fully")
    print("3. Empty 3 Gallon")
    print("4. Empty 4 Gallon")
    print("5. Transfer 3 to 4")
    print("6. Transfer 4 to 3")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if contains3 < 3:
            contains3 = 3
            steps += 1
        else:
            print("3 Gallon jar is already full!!")

    elif choice == 2:
        if contains4 < 4:
            contains4 = 4
            steps += 1
        else:
            print("4 Gallon jar is already full!!")

    elif choice == 3:
        if contains3 > 0:
            contains3 = 0
            steps += 1
        else:
            print("3 Gallon jar is already empty!!")

    elif choice == 4:
        if contains4 > 0:
            contains4 = 0
            steps += 1
        else:
            print("4 Gallon jar is already empty!!")

    elif choice == 5:
        if contains3 > 0:
            space = 4 - contains4
            transfer = min(contains3, space)

            contains3 -= transfer
            contains4 += transfer
            steps += 1
        else:
            print("Transfer not possible!! 3 Gallon jar has no water.")

    elif choice == 6:
        if contains4 > 0:
            space = 3 - contains3
            transfer = min(contains4, space)

            contains4 -= transfer
            contains3 += transfer
            steps += 1
        else:
            print("Transfer not possible!! 4 Gallon jar has no water.")

    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice!!")

    show_jars()