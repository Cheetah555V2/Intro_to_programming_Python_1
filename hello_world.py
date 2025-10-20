import string
import time
import os
word = "Hello World"
curr_word = ""
index = 0

while curr_word != word:
    for i in " " + string.ascii_letters:
        time.sleep(0.04)
        print(curr_word + i)
        if i == word[index] and word == curr_word + i:
            curr_word += i
            index += 1
            os.system("cls")
            print(curr_word)
            break
        elif i == word[index]:
            curr_word += i
            index += 1
            break