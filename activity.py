
words = "cowcatdogsnake"

search_word = input("Enter word to find: ")

first_index = words.find(search_word)

if first_index != -1:
    print(f"The first index of '{search_word}' in the string '{words}' is {first_index}")


    last_index = first_index + len(search_word) - 1

    print(f"The last index of '{search_word}' in the string '{words}' is {last_index}")
else:
    print(f"Error: '{search_word}' not found in the string '{words}'.")
