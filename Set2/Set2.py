task = int(input("Enter task number: "))

line = "Lorem ipsum dolor sit amet GvR,\nconsectetur adipiscing elit,\nsed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

if task == 10:
    new_line = line.replace(".", "").replace(",", "")
    word_count = len(new_line.split())
    print("Number of captions: " + str(word_count))

if task == 11:
    word = "word"
    new_word = "_".join(word)
    print(new_word)

if task == 12:
    new_line = line.replace(".", "").replace(",", "")
    words = new_line.split()
    first_letter =''.join(word[0] for word in words)
    last_letter = ''.join(word[-1] for word in words)
    print("First letters: " + str(first_letter))
    print("Last letters: " + str(last_letter))

if task == 13:
    new_line = line.replace(".", "").replace(",", "").replace(" ","")
    total_sum = len(new_line)
    print("The total length of words: " + str(total_sum))

if task == 14:
    length = 0
    longest_word = ""
    new_line = line.replace(".", "").replace(",", "")
    words = new_line.split()

    for i in range(len(words)):
        if len(words[i]) >= length:
            length = len(words[i])
    print("Size of the largest word: " + str(length))
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print("Longest word/words: " + longest_word, end=" ")
    for word in words:
        if len(word) == len(longest_word):
            if not word == longest_word:
                print(word, end=" ")

if task == 15:
    L = [1, 2, 3, 4, 5, 6, 7, 8]
    word = "".join([str(number) for number in L])
    print(word)

if task == 16:
    new_line = line.replace("GvR", "Guido van Rossum")
    print(new_line)

if task == 17:
    words = line.lower().split()
    words.sort()
    print("Sorted alphabetically:\n" + str(words))
    words_len = sorted(words, key=len)
    print("Sorted depending on the length:\n" + str(words_len))

if task == 18:
    x = 43420002130
    new_x = str(x)
    how_many = new_x.count("0")
    print("The number 0 occurs " + str(how_many) + " times")

if task == 19:
    L = [1, 3, 7, 19, 40, 43, 603, 424, 654]
    new_L = [str(number) for number in L]
    for i in range(len(new_L)):
            new_L[i] = new_L[i].zfill(3)
    print(new_L)