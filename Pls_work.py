import os

if os.name == "nt":
    import msvcrt

    def clear_console():
        os.system("cls")


    def get_char():
        return chr(msvcrt.getch()[0])

else:
    import tty
    import termios
    import sys

    def clear_console():
        os.system("clear")
    
    def get_char():
        # Gets the file descriptor (an integer handle) for standard input
        file_descriptor = sys.stdin.fileno()

        # Saves the current terminal settings
        old_settings = termios.tcgetattr(file_descriptor)

        # Puts the terminal in raw mode (No echo)
        tty.setraw(file_descriptor)

        # Reads 1 character from the terminal
        charactor = sys.stdin.read(1)

        # Restores the original terminal settings
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)

        # return charactor
        return charactor

your_char = get_char()

print(f"You type {your_char}")