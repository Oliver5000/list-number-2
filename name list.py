import sys
name = ["Oliver", "Anjali", "Dillara", "Nick","Alex"]
while True:
    print("Press 1 to add a name")
    print("Press 2 to edit a name")
    print("Press 3 to remove a name")
    print("Press 4 to see all names")
    print("Press 5 to exit")
    choice = int(input("Write here:"))
    if choice == 1:
        n = input("What name would you like to add?")
        name.append(n)
        print(name)
    if choice == 2:
        n1 = input("Which name would you like to edit?")
        n2 = input("Edit here:")
        count = 0
        for i in name:
            if i == n1:
                name[count] = n2
            else:
                count += 1
        print(name)
    if choice == 3:
        n = input("What name would you like to remove?")
        name.remove(n)
        print(name)
    if choice == 4:
        print(name)
    if choice == 5:
        print("Exiting")
        sys.exit()