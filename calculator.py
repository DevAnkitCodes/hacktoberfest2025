import sys

def calculator(c,a,b):

    if c ==1:
        print(f"Sum of {a} & {b} is = {a + b}")

    elif c == 2:
        print(f"Subtraction of {a} & {b} is = {a - b}")

    elif c == 3:
        print(f"Multiplication of {a} & {b} is = {a * b}")

    elif c == 4:
        if b != 0:
            print(f"Division of {a} & {b} is = { a / b }")
        else:
            print("Error: We Cannot Divide by 0")
            sys.exit()



print("---Welcome To the Calculator---\n----------------------------------\nChoose the operation!")

print("1. Sum")
print("2.Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

c = int(input("Enter the Option(1/2/3/4/5):"))

if c == 5:
    print("You are Exiting Now!")
    sys.exit()

elif c >= 1 and c <= 4:
    a = int(input("Enter 1st Number:"))
    b = int(input("Enter 2nd Number:"))

else:
    print("Invalid Input!")
    sys.exit()

calculator(c, a, b)
