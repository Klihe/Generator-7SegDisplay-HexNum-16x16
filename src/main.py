# main.py

# Bit values for 7 segment display
ZERO = ["e", "7"]
ONE = ["2", "1"]
TWO = ["c", "b"]
THREE = ["6", "b"]
FOUR = ["2", "d"]
FIVE = ["6", "e"]
SIX = ["e", "e"]
SEVEN = ["2", "3"]
EIGHT = ["e", "f"]
NINE = ["6", "f"]

A = ["a", "f"]
B = ["f", "f"]
C = ["c", "6"]
D = ["f", "7"]
E = ["c", "e"]
F = ["8", "e"]

# Array of values on display
NUMBERS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, A, B, C, D, E, F]

# Clear the output file
with open('log/output.txt', 'w') as file:
    file.write("")

# Writing displayed values 0-255 (16x16)
for i in NUMBERS:
    for j in NUMBERS:
        # Writing to the output file
        with open('log/output.txt', 'a') as file:
            file.write(f"{j[0]}{i[0]}{i[1]}{j[1]} ")
        # Check the values in the terminal
        print(j[0],i[0],i[1],j[1])

    # Add enter after 16. no
    with open('log/output.txt', 'a') as file:
        file.write("\n")