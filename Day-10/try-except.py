import sys

# Convert command-line arguments to integers (or floats if needed)
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

try:
    num = num1 / num2
    print("Result:", num)
except ZeroDivisionError:
    print("Don't enter 0")