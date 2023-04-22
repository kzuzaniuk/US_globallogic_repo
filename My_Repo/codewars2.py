def spin_words(sentence):
    temp_list = sentence.split()
    for word in temp_list:
        if len(word) >= 5:
            temp_list[temp_list.index(word)] = word[::-1]
    # Your code goes here
    return " ".join(temp_list)


print(spin_words("Welcome to CodeWars"))