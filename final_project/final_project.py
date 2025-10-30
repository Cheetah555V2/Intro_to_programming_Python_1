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
        # math.sqrt() is faster then x ** (1/2), I read the c and assembly code
        # it's like 20 times faster and more accurate
        # math.sqrt() is just 1 instruction in x86 (modern CPU with SSE2)

        if number % index == 0:
            return False

    return True


def miller_rabin_primitive_test(number, k=10):
    if number == 2:
        return True

    if number <= 1 or number % 2 == 0:
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


def is_prime(number, accuracy_level=10):
    if number > 10**12:
        return miller_rabin_primitive_test(number, accuracy_level)

    return trial_division_primitive_test(number)


"""
|==============================================
|                 Math function
|==============================================
"""    

def RSA_encryption(unicode, public_exponent, modulus):
    return pow(unicode,public_exponent,modulus)

def semiprime_euler_totient(prime_1, prime_2):
    return (prime_1) * (prime_2)

def modular_multiplicative_inverse(multiplyer, modulus_base):
    # multiplyer*number ≡ 1 (mod modulus_base)
    # return multiplyer^(-1)


    return inverse

"""
|==============================================
|            Sub-Sub-Main function
|==============================================
"""    

def generating_prime(digits):
    prime = random.randint(10**(digits-1),10**(digits)-1)
    while not is_prime(prime):
        prime = random.randint(10**(digits-1),10**(digits)-1)
    
    return prime


def wait_for_right_input_receiver(*wanted_input):
    choice = get_char().lower()
    while choice not in wanted_input:
        choice = get_char().lower()
    
    return choice


def public_exponent_generator(euler_totient, modulus):
    if modulus > 65537:
        public_exponent = 65537
    else:
        public_exponent = random.randint(2, modulus-1)

    while math.gcd(public_exponent, euler_totient) != 1:
        public_exponent = random.randint(2, modulus-1)

    return public_exponent


def private_exponent_generator():
    asdasd
    return private_exponent


"""
|==============================================
|               Sub-Main function
|==============================================
"""

def check_for_primality_flow():
    while True:

        clear_console()
        print("Primality Test\nEnter an integer to test for primality: ")

        number = int(input())
        
        clear_console()

        if number > 10**12:
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
            result = is_prime(number, accuracy_level)
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
                
                choice = wait_for_right_input_receiver("y", "n")
                
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

        choice = wait_for_right_input_receiver("r", "m")
        
        if choice == "r":
            continue
        elif choice == "m":
            break


def generating_a_pair_of_RSA_keys_flow():
    clear_console()

    print("How many digits of primes do you want to generate? (more digits mea\
ns more secure keys, but slower generation) (do not input value more than 1000\
, python might crash): ", end="")        

    digits = int(input())

    clear_console()

    print("Generating... please wait.")

    prime_1 = generating_prime(digits)
    prime_2 = generating_prime(digits)
    
    clear_console()

    if digits >= 12:
        confidence = (1 - (pow(1/4, 20) * (2 - pow(1/4, 20)))) * 100 # in %

        # To P'Ve or P'Dew reading my code
        # I double check the confidence level
        # No need to check again. It's just P(not prime) = (1/4)**k
        # And P(at least 1 out of 2 is not prime) is just
        # P(not prime) + P(not prime) - (P(not prime))**2
        # which is what I write above before turn it into percentage 

        print(f"Generated primes keys with {confidence}% confidence that b\
oth is prime:\np = {prime_1}\nq = {prime_2}")

    else:
        print(f"Generated primes keys:\np = {prime_1}\nq = {prime_2}")
    print(f"Your semiprime (n) is {prime_1*prime_2}")

    print("Press any key to return to main menu.")
    get_char()


def encrypting_a_massage_flow():
    clear_console()

    print("What is your massage that you want to encrypt?: ")
    massage = input()

    clear_console()

    print("Do you have a public key? (e and n) (Y/N)\nExplaination: let n \
(modulus) be semiprime number, n = p*q.\nϕ(x) is Euler's totient function\nϕ(n\
) = (p-1)*(q-1)\ne (public exponent) is a number we choose such that e is copr\
ime with ϕ(n)\n\nPlease use n greater than 1,200,000 (if it's lower it might c\
ause decryption problem and error)")
    
    choice = wait_for_right_input_receiver("y", "n")
    
    clear_console()

    if choice == "y":
        print("Please input your public key (in positive integer of course\
) with n > 1200000 and n must be semiprime, also e must be coprime with ϕ(n)")
        public_exponent = int(input("e (public exponent) = "))
        modulus = int(input("n (modulus) = "))

    else:
        print("How many digits of prime (p and q) that you will use for en\
cryption? (please use more than 4 digits, or it might cause error when decrypt\
ion): ",end="")
        digits = int(input())

        prime_1 = generating_prime(digits)
        prime_2 = generating_prime(digits)
        modulus = prime_1 * prime_2

        euler_totient_n = semiprime_euler_totient(prime_1,prime_2)



        public_exponent = public_exponent_generator(euler_totient_n,
                                                    modulus)
        
        private_exponent = pri

        print(f"This is your prime p, q, n (modulus), e (public exponent) and \
d (private exponent)\np = {prime_1}\nq = {prime_2}\nn = {modulus}\ne = \
{public_exponent}")


    clear_console()
    print("Encrypting... please wait")
    
    encrypt_list = []

    for charactor in massage:
        unicode = ord(charactor)
        encrypt_charactor = RSA_encryption(unicode, public_exponent,
                                            modulus)
        encrypt_list.append(encrypt_charactor)
    
    clear_console()

    print("This is your encrypt massage\n")
    print(str(encrypt_list).removeprefix("[").removesuffix("]") + "\n")
    print("Press any key to return to menu")

    get_char()


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
    
    choice = wait_for_right_input_receiver("1", "2", "3", "4", "q")
    
    if choice == "1":
        check_for_primality_flow()

    elif choice == "2":
        generating_a_pair_of_RSA_keys_flow()
    
    elif choice == "3":
        encrypting_a_massage_flow()

    elif choice == "4":
        pass

    else:
        break