import os
os.system("cls")

print('''\t\t\t\t           ______      __           __      __            
         \t\t\t\t  / ____/___ _/ /______  __/ /___ _/ /_____  _____
         \t\t\t\t / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
         \t\t\t\t/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
         \t\t\t\t\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
                                                              ''')

print("Welcome To Calculator")

print("\n\nchoose 1 For additon")
print("choose 2 For subtraction")
print("choose 3 For multiplication")
print("choose 4 For division")
print("choose 5 For floor division")
print("choose 6 For exponent")
print("choose 7 To quit the program")

while True:
    choice = int(input("\n\nEnter your choice: "))

    if choice == 1:
        a = int(input("\nEnter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == 2:
        c = int(input("\nEnter first number: "))
        d = int(input("Enter second number: "))
        print("Result:", c - d)

    elif choice == 3:
        e = input("\nEnter first number: ")
        f = input("Enter second number: ")
        print("Result:", e * f)

    elif choice == 4:
        g = int(input("\nEnter divident: "))
        h = int(input("Enter divisor: "))
        print("Quotient:", g / h)

    elif choice == 5:
        i = int(input("\nEnter dividend: "))
        j = int(input("Enter divisor: "))
        print("Result:", i // j)

    elif choice == 6:
        k = int(input("\nEnter base value: "))
        l = int(input("Enter exponential power: "))
        print("Result:", k ** l) 

    elif choice == 7:
        print(" \nThanks for using the calculator ")
        quit() 

    else:
        print("Please enter a valid choice")
