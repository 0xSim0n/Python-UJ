print("\nTask 3")


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print(factorial(8))

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


def odwracanie(L, left, right):
    new_list = L[right:left - 1:-1]
    for i in range(0, right-left+1):
        L.insert(left, new_list[len(new_list) - 1 - i])
        L.pop(right + 1)
    return L


print(odwracanie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 4))

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