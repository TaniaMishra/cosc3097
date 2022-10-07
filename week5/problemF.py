from operator import indexOf


word = input("Word: ")
seq = input("Sequence: ")

working_word = word
for letter in seq:
    index = working_word.find(letter)
    print(letter)
    if index == -1:
        print("not found")
        break
    print(index)
    working_word = working_word[index+1:]
    print(working_word)