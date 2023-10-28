from roman_arabic_numerals import conv

task = int(input("Enter task number: "))

"""
3.1
######
x = 2; y = 3;
if (x > y):
    result = x;        sredniki są zbedne
else:
    result = y;
######
for i in "axby": if ord(i) < 100: print (i)
######

"""

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
            print("Please, enter the number!")
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
        if i < 9:
            print(str(i) + "    ", end="")
        elif i >= 9 and i < 99:
            print(str(i) + "   ", end="")
        elif i >= 99:
            print(str(i) + "  ", end="")

if task == 6:
    def draw():
        if i % 2 == 0 and not(x == 0):
            for j in range(y):
                print("+---", end="")
            print("+")
        elif not(x == 0):
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

    """
    Method I
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    Method II
    roman_to_arabic = {}
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabic_numerals = [1, 5, 10, 50, 100, 500, 1000]
    
    for i in range(len(roman_numerals)):
        roman_to_arabic[roman_numerals[i]] = arabic_numerals[i]
        
    Method III
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabic_numerals = [1, 5, 10, 50, 100, 500, 1000]

    roman_to_arabic = dict(zip(roman_numerals, arabic_numerals))
    """

    roman_number = input("Enter the roman numeral: ")
    conv.rom_arab(roman_number)
