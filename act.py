def find_first_last_index(word_list, target_word):
    first_index = -1
    last_index = -1

    for i, word in enumerate(word_list):
        if word == target_word:
            if first_index == -1:
                first_index = i
            last_index = i

    return first_index, last_index

words = ['apple', 'banana', 'orange', 'banana', 'grape', 'banana']
target = input("Enter Words :")

first, last = find_first_last_index(words, target)

if first != -1:
    print(f"The first occurrence of '{target}' is at index: {first} and len of  {last}")

else:
    print(f"'{target}' is not found in the list.")
