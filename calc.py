import os
os.system("cls && title[Calculator] ~ Kanika and Nancy")

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
        num_one = int(input("\nEnter first number: "))
        num_two = int(input("Enter second number: "))
        print("Result:", num_one + num_two)

    elif choice == 2:
        num_one = int(input("\nEnter first number: "))
        num_two = int(input("Enter second number: "))
        print("Result:", num_one - num_two)

    elif choice == 3:
        num_one = input("\nEnter first number: ")
        num_two = input("Enter second number: ")
        print("Result:", num_one * num_two)

    elif choice == 4:
        divident = int(input("\nEnter divident: "))
        divisor = int(input("Enter divisor: "))
        print("Quotient:", divident / divisor)

    elif choice == 5:
        divident = int(input("\nEnter dividend: "))
        divisor = int(input("Enter divisor: "))
        print("Result:", divident // divisor)

    elif choice == 6:
        base_value = int(input("\nEnter base value: "))
        exp_power = int(input("Enter exponential power: "))
        print("Result:", base_value ** exp_power) 

    elif choice == 7:
        print(" \nThanks for using the calculator ")
        quit() 

    else:
        print("Please enter a valid choice")