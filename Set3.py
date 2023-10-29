from roman_arabic_numerals import conv

#Task 1
# a) Kod jest prawidłowy, średniki są zbędne
# b) Brakuje wcięcia po pętli for
# c) Cała instrukcja warunkowa musi być w osobnej linii i odpowiednio wcięta

#Task 2
# a) L zostaje zmienione na None, funkcja sort nie tworzy nowej listy
# b) Dwie zmienne, a trzy wartości
# c) Nie można zmieniac wartości elementu w krotce
# d) Indeks 3 jest poza zakresem listy
# e) Funkcja append działa dla tablic
# f) Funkcja pow nie ma podanych argumentów

print("Task 3")
x = 30
for i in range(x):
    if not (i % 3 == 0):
        print(i, end=" ")

print("\nTask 4")
x = ""
while not (x == "stop"):
    x = input("Enter the number: ")
    nx = x.replace(".", "")
    if not (nx.isnumeric()) and not (x == "stop"):
        print("Please, enter the number!")
    elif not (x == "stop"):
        new_x = float(x)
        print(new_x)
        print(new_x ** 3)

print("\nTask 5")
x = int(input("Enter the number: "))
lower_ruler = ""
if x > 0:
    upper_ruler = x * "|...." + "|"
    for i in range(x + 1):
        if i < 9:
            lower_ruler += (str(i) + "    ")
        elif 99 > i >= 9:
            lower_ruler += (str(i) + "   ")
        elif i >= 99:
            lower_ruler += (str(i) + "  ")
    ruler = upper_ruler + "\n" + lower_ruler
    print(ruler)
else:
    print("Wrong input")

print("\nTask 6")


def draw():
    drawing = ""
    if i % 2 == 0 and not (x == 0):
            line_1 = y * "+---" + "+"
            drawing += line_1
    elif not (x == 0):
            line_2 = y * "|   " + "|"
            drawing += line_2
    print(drawing)


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

for i in range((x * 2) + 1):
    draw()

print("\nTask 8")
sequence_1 = "sadasd322216>?,',"
sequence_2 = "fadaqwqcdht5322<>:"
memory = []
new_memory = []
new_sequence_1 = " ".join(sequence_1).split()
new_sequence_2 = " ".join(sequence_2).split()
for i in range(len(new_sequence_1)):
    for j in range(len(new_sequence_2)):
        if new_sequence_1[i] == new_sequence_2[j] and not (memory.count(new_sequence_1[i]) > 0):
            memory.append(new_sequence_1[i])
print("List of same elements in both sequences: " + str(memory))

for i in range(len(new_sequence_1)):
    if not (new_memory.count(new_sequence_1[i]) > 0):
        new_memory.append(new_sequence_1[i])
for i in range(len(new_sequence_2)):
    if not (new_memory.count(new_sequence_2[i]) > 0):
        new_memory.append(new_sequence_2[i])
print("List of all elements from both sequences: " + str(new_memory))

print("\nTask 9")
sequence_1 = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
sums = []
for subsequence in sequence_1:
    sum_of_subsequence = sum(subsequence)
    sums.append(sum_of_subsequence)
print(sums)

print("\nTask 10")

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
print(conv.rom_arab(roman_number))
