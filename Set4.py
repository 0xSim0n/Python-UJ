print("\nTask 2")


def ruler(x):
    line = ""
    for i in range(x):
        line = line + ("|....")
    line += ("|\n")
    for i in range(x+1):
        if i < 9:
            line += (str(i) + "    ")
        elif i >= 9 and i < 99:
            line += (str(i) + "   ")
        elif i >= 99:
            line += (str(i) + "  ")
    return line


def draw(x, y):
    line = ""
    for i in range((x * 2) + 1):
        if i % 2 == 0 and not (x == 0):
            for j in range(y):
                line += ("+---")
            line += ("+\n")
        elif not (x == 0):
            for k in range(y):
                line += ("|" + "   ")
            line += ("|\n")
    return line


print(ruler(7))
print("\n")
print(draw(3, 4))

print("\nTask 3")


def factorial(n):
    i = 1
    s = 1
    while i <= n:
        s *= i
        i += 1
    return s


print(factorial(5))

print("\nTask 4")


def fibonacci(n):
    a, b, c = 0, 1, 0
    if n == 0:
        print(0)
    if n == 1:
        print(1)
    if n > 1:
        for i in range(2, n + 1):
            a = b + c
            c = b
            b = a
        return b


print(fibonacci(2))

print("\nTask 5")


def odwracanie_iteracyjne(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rekurencyjne(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjne(L, left + 1, right - 1)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odwracanie_iteracyjne(L, 4, 8)
odwracanie_rekurencyjne(M, 2, 6)
print(L)
print(M)


print("\n Task 6")


def sum_seq(sequence):
    suma = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            suma += sum(element)
        else:
            suma += element
    return print(suma)


sekwencja = [1, 2, 3, (4, 5), [6, 7, 8], (9, 10)]
sum_seq(sekwencja)

print("\nTask 6")


def flatten(sequence):
    L = []
    F = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            L += element
        else:
            L.append(element)
    for element in L:
        if isinstance(element, tuple):
            F.extend(element)
        else:
            F.append(element)
    return F


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))
