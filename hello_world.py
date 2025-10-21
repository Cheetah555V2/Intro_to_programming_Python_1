import string
import time
import os


word = "Hello World"
curr_word = ""
index = 0

os.system("cls")

while curr_word != word:
    for i in " " + string.ascii_letters:
        time.sleep(0.03)
        print(curr_word + i)
        if i == word[index]:
            curr_word += i
            index += 1
            break


os.system("cls")
print(curr_word)
