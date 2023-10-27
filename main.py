task = int(input("Enter task number: "))

if task == 3:
    x = 30
    for i in range(x):
        if not(i % 3 == 0):
            print(i, end=" ")

if task == 4:
    x = ""
    while not(x == "stop"):
        x = input("Enter the number: ")
        nx = x.replace(".", "")
        if not(nx.isnumeric()) and not(x == "stop"):
            print("Please, enter the new number: ")
        elif not(x == "stop"):
            new_x = float(x)
            print(new_x)
            print(new_x**3)

if task == 5:
    x = int(input("Enter the number: "))
    for i in range(x):
        print("|....", end="")
    print("|")
    for i in range(x+1):
        if i < 10:
            print(str(i) + "    ", end="")
        if i >= 10:
            print(str(i) + "   ", end="")

if task == 6:
    def draw():
        if i % 2 == 0:
            for j in range(y):
                print("+---", end="")
            print("+")
        else:
            for k in range(y):
                print("|" + "   ", end="")
            print("|")

    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    for i in range((x * 2) + 1):
        draw()

if task == 8:
    sequence_1 = "sadasd322216>?,',"
    sequence_2 = "fadaqwqcdht5322<>:"
    memory = []
    new_memory = []
    new_sequence_1 = " ".join(sequence_1).split()
    new_sequence_2 = " ".join(sequence_2).split()
    for i in range(len(new_sequence_1)):
        for j in range(len(new_sequence_2)):
            if new_sequence_1[i] == new_sequence_2[j] and not(memory.count(new_sequence_1[i]) > 0):
               memory.append(new_sequence_1[i])
    print("List of same elements in both sequences: " + str(memory))

    for i in range(len(new_sequence_1)):
        if not(new_memory.count(new_sequence_1[i]) > 0):
            new_memory.append(new_sequence_1[i])
    for i in range(len(new_sequence_2)):
        if not(new_memory.count(new_sequence_2[i]) > 0):
            new_memory.append(new_sequence_2[i])
    print("List of all elements from both sequences: " + str(new_memory))

if task == 9:
    sequence_1 = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
    sums = []
    for subsequence in sequence_1:
        sum_of_subsequence = sum(subsequence)
        sums.append(sum_of_subsequence)
    print(sums)

if task == 10: