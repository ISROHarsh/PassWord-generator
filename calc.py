import os
os.system("cls")
print("*********Welcome To Calculator********")
print("choose 1 For additon")
print("choose 2 For subtraction")
print("choose 3 For multiplication")
print("choose 4 For division")
print("choose 5 For floor division")
print("choose 6 For exponent")
print("choose 7 To quit the program")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)
    elif choice == 2:
        c = int(input("Enter first number: "))
        d = int(input("Enter second number: "))
        print("Result:", c - d)
    elif choice == 3:
        e = input("Enter first number: ")
        f = input("Enter second number: ")
        print("Result:", e * f)
    elif choice == 4:
        g = int(input("Enter divident: "))
        h = int(input("Enter divisor: "))
        print("Quotient:", g / h)
    elif choice == 5:
        i = int(input("Enter dividend: "))
        j = int(input("Enter divisor: "))
        print("Result:", i // j)
    elif choice == 6:
        k = int(input("\nEnter base value: "))
        l = int(input("Enter exponential power: "))
        print("Result:", k ** l) 
    elif choice == 7:
        print(" Thanks for using the calculator ")
        quit() 
    else:
        print("Please enter a valid choice")
