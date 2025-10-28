import math
import msvcrt
import os
import time

"""
|==============================================
|              Console commmand
|==============================================
"""


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_char():
    return chr(msvcrt.getch()[0])


"""
|==============================================
|                Primitive test
|==============================================
"""


def trial_division_primitive_test(number):
    if number <= 1:
        return False

    for index in range(2, int(math.sqrt(number))):
        if number % index == 0:
            return False

    return True


def is_prime(number):
    pass


"""
|==============================================
|                User Interface
|==============================================
"""


def UI(page, input_data=None):
    if page == "menu":
        print("""RSA encryption system menu
press the following keys to select an option:
(1) Checking for primality
(2) Generating a pair of RSA keys
(3) Encrypting a message
(4) Decrypting a message
(Q) Quit program\
""")
    elif page == "primality_test_1":
        print("Primality Test")
        print("Enter an integer to test for primality: ")
    elif page == "primality_test_2":
        print(f"The number {input_data[0]} is {input_data[1]}")
        print(f"The program took {input_data[2]:.6f} to complete.\n")
        print(f"(R) to do primality test again or\n\
(M) to return to main menu.")

"""
|==============================================
|                 Main function
|==============================================
"""

while True:
    clear_console()
    UI("menu")
    choice = get_char().lower()
    if choice == "1":

        while True:

            clear_console()
            UI("primality_test_1")

            number = int(input())
            print("Processing... please wait.")
            start_time = time.time()
            result = trial_division_primitive_test(number)
            end_time = time.time()
            elapsed_time = end_time - start_time
            clear_console()

            if result:
                UI("primality_test_2", (number, "prime", elapsed_time))
            else:
                UI("primality_test_2", (number, "coprime", elapsed_time))

            choice = get_char().lower()

            if choice == "r":
                continue
            elif choice == "m":
                clear_console()
                break
            else:
                print("Invalid input, returning to main menu.")
                time.sleep(1)
                clear_console()
                break

        continue

    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        pass

    elif choice == "q":
        break

