import math
import msvcrt
import os
import time
import random

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


def miller_rabin_primitive_test(number, k=10):
    if number <= 2 or number % 2 == 0:
        return False
    
    s = 0
    d = number - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    

    for _ in range(k):
        a = random.randint(2, number - 2)
        x = pow(a, d, number)
        if x == 1 or x == number - 1:
            continue

        for _ in range(s):
            y = (x * x) % number
            if (y == 1) and x != 1 and x != number - 1:
                return False
            x = y

        if y != 1:
            return False
    
    return True

def is_prime(number):
    if number > 10**12:
        return miller_rabin_primitive_test(number, 20)

    return trial_division_primitive_test(number)
    

"""
|==============================================
|                 Main function
|==============================================
"""

while True:
    clear_console()
    print("""RSA encryption system menu
press the following keys to select an option:
(1) Checking for primality
(2) Generating a pair of RSA keys
(3) Encrypting a message
(4) Decrypting a message
(Q) Quit program""")
    
    while True:
        choice = get_char().lower()
        if choice in ["1", "2", "3", "4", "q"]:
            break
    
    if choice == "1":

        while True:

            clear_console()
            print("Primality Test\nEnter an integer to test for primality: ")

            number = int(input())
            
            clear_console()

            if number > 2*(10**12): #point where sqrt(number) = 20log^3(number)
                # Use Miller-Rabin for large numbers
                print("""Miller-Rabin Primality Test Selected for this number.
Please provide a accuracy level that you want in positive integer (1-20) (defa\
lut = 10): """)
                accuracy_level = input()
                if accuracy_level.isdigit():
                    accuracy_level = int(accuracy_level)
                else:
                    accuracy_level = 10
                
                print("Processing... please wait.")

                start_time = time.time()
                result = miller_rabin_primitive_test(number, accuracy_level)
                end_time = time.time()
                elapsed_time = end_time - start_time
                accuracy = max(0, (1 - (1 / (4**accuracy_level))) * 100) #in %
                
                clear_console()

                if result:
                    print(f"""The number {number}\nis Probabliy Prime with \
{accuracy}% confidence""")
                    print(f"The program took {elapsed_time:.6f} to complete.")
                    print("""Do you want to check if it's definitely prime? Th\
is might take up a lot of time (use trial division up to √number) (Y/N):""")
                    while True:
                        choice = get_char().lower()
                        if choice == "y" or choice == "n":
                            break
                    
                    clear_console()

                    if choice == "y":
                        clear_console()

                        print("Processing... please wait.")
                        start_time = time.time()
                        result = trial_division_primitive_test(number)
                        end_time = time.time()
                        elapsed_time = end_time - start_time

                        clear_console()

                        if result:
                            print(f"The number {number} is Prime")
                        else:
                            print(f"The number {number} is Coprime")
        
                        print(f"The program took {elapsed_time:.6f} to complete.")


                else:
                    print(f"The number {number} is Coprime")
                    print(f"The program took {elapsed_time:.6f} to complete.")

            
            else:
                # Use trial division for small numbers
                print("Processing... please wait.")
                start_time = time.time()
                result = trial_division_primitive_test(number)
                end_time = time.time()
                elapsed_time = end_time - start_time

                clear_console()

                if result:
                    print(f"The number {number} is Prime")
                else:
                    print(f"The number {number} is Coprime")

                print(f"The program took {elapsed_time:.6f} to complete.")
                

            print("(R) to do primality test again")
            print("(M) to return to main menu.")

            while True:
                choice = get_char().lower()
                if choice == "r" or choice == "m":
                    break
            
            if choice == "r":
                continue
            elif choice == "m":
                break

        continue
    

    elif choice == "2":
        clear_console()

        print("How many digits of primes do you want to generate? (more digits\
means more secure keys, but slower generation) (do not input value more than 1\
000, python might crash): ", end="")        

        digits = int(input())

        clear_console()

        print("Generating... please wait.")

        prime_1 = random.randint(10**(digits-1), 10**(digits)-1)
        prime_2 = random.randint(10**(digits-1), 10**(digits)-1)

        while not is_prime(prime_1):
            prime_1 = random.randint(10**(digits-1), 10**(digits)-1)
        
        while not is_prime(prime_2):
            prime_2 = random.randint(10**(digits-1), 10**(digits)-1)
        
        clear_console()

        confidence = (1 - (pow(1/4, 20) * (2 - pow(1/4, 20)))) * 100 # in %

        if digits >= 12:
            print(f"Generated primes keys with {confidence}% confidence that b\
oth is prime:\np = {prime_1}\nq = {prime_2}")
        else:
            print(f"Generated primes keys:\np = {prime_1}\nq = {prime_2}")
        
        print("Press any key to return to main menu.")
        get_char()
    

    elif choice == "3":
        pass

    elif choice == "4":
        pass

    elif choice == "q":
        break