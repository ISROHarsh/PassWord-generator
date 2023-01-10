import os
try:
    from prettytable import PrettyTable
except:
    os.system("python -m pip install -U prettytable" )
os.system("cls & mode 200,20 && title[Billing System] ~ github.com/ISROHarsh")

def banner():
    banner = '''\t\t\t\t\x1b[32m                 ███████████\x1b[0m\x1b[36m   ███  ████  ████   ███     \x1b[0m   \x1b[32m                  █████████\x1b[0m\x1b[36m                      █████            \x1b[0m                
                \t\t\t\t\x1b[32m░░███░░░░░███\x1b[0m\x1b[36m ░░░  ░░███ ░░███  ░░░                      \x1b[0m   \x1b[32m ███░░░░░███\x1b[0m\x1b[36m                    ░░███                             \x1b[0m
                \t\t\t\t\x1b[32m ░███    ░███\x1b[0m\x1b[36m ████  ░███  ░███  ████  ████████    ███████\x1b[0m   \x1b[32m░███    ░░░ \x1b[0m\x1b[36m █████ ████  █████  ███████    ██████  █████████████  \x1b[0m
                \t\t\t\t\x1b[32m ░██████████ \x1b[0m\x1b[36m░░███  ░███  ░███ ░░███ ░░███░░███  ███░░███\x1b[0m   \x1b[32m░░█████████ \x1b[0m\x1b[36m░░███ ░███  ███░░  ░░░███░    ███░░███░░███░░███░░███ \x1b[0m
                \t\t\t\t\x1b[32m ░███░░░░░███\x1b[0m\x1b[36m ░███  ░███  ░███  ░███  ░███ ░███ ░███ ░███\x1b[0m   \x1b[32m ░░░░░░░░███\x1b[0m\x1b[36m ░███ ░███ ░░█████   ░███    ░███████  ░███ ░███ ░███ \x1b[0m
                \t\t\t\t\x1b[32m ░███    ░███\x1b[0m\x1b[36m ░███  ░███  ░███  ░███  ░███ ░███ ░███ ░███\x1b[0m   \x1b[32m ███    ░███\x1b[0m\x1b[36m ░███ ░███  ░░░░███  ░███ ███░███░░░   ░███ ░███ ░███ \x1b[0m
                \t\t\t\t\x1b[32m ███████████ \x1b[0m\x1b[36m █████ █████ █████ █████ ████ █████░░███████\x1b[0m   \x1b[32m░░█████████ \x1b[0m\x1b[36m ░░███████  ██████   ░░█████ ░░██████  █████░███ █████\x1b[0m
                \t\t\t\t\x1b[32m░░░░░░░░░░░  \x1b[0m\x1b[36m░░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░███\x1b[0m   \x1b[32m ░░░░░░░░░  \x1b[0m\x1b[36m  ░░░░░███ ░░░░░░     ░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░ \x1b[0m
                \t\t\t\t\x1b[32m             \x1b[0m\x1b[36m                                    ███ ░███\x1b[0m   \x1b[32m            \x1b[0m\x1b[36m  ███ ░███                                            \x1b[0m
                \t\t\t\t\x1b[32m             \x1b[0m\x1b[36m                                   ░░██████ \x1b[0m   \x1b[32m            \x1b[0m\x1b[36m ░░██████                                             \x1b[0m
                \t\t\t\t\x1b[32m             \x1b[0m\x1b[36m                                    ░░░░░░  \x1b[0m   \x1b[32m            \x1b[0m\x1b[36m  ░░░░░░                                              \x1b[0m '''                                     
    return print(banner)

def products():
    products = PrettyTable(["Product No.","Product Name","Price per Kg"])
    products.add_row(["1","Gulab Jamun","₹500"])
    products.add_row(["2","Rasmalai","₹600"])
    products.add_row(["3","Motichoor Ladoo","₹400"])
    products.add_row(["4","Boondi","₹200"])
    products.add_row(["5","Rasgulla","₹300"])
    products.add_row(["6","Kaju Katli","₹1000"])
    products.add_row(["7","Jalebi","₹350"])
    products.add_row(["8","Bareli ki Barfi","₹500"])
    products.add_row(["9","SoanPapdi","₹600"])
    products.add_row(["10","Agra ka Petha","₹250"])
    return print(products)

def main_menu():
    print('''\n\n
\u001b[0m[\x1b[\x1b[38;5;63m#\u001b[0m] Main menu
\u001b[0m[\x1b[\x1b[38;5;63m1\u001b[0m] Show Products
\u001b[0m[\x1b[\x1b[38;5;63m2\u001b[0m] Purchase
\u001b[0m[\x1b[\x1b[38;5;63m3\u001b[0m] Exit''')

def customer_info():
    name = input("Enter the Customer name: >")
    mobile_no = input("Enter the mobile no. >")
    Adress = input("Enter Address: >")
    if len(mobile_no) < 10 or len(mobile_no) > 10:
        print("[\x1b[31m!\x1b[0m] The Phone no. you have entered is not of 10 digits , Please Try Again.")
def purchase():
    print("If you want to see the prducts again type Y if not then type N to go for the purchase")
    choose = input("Enter Your choice \x1b[36m>\x1b[0m ")
    if choose == "Y" or "y":
        products()
        print("")





banner()

while True:
    main_menu()
    choice = int(input("choose a option\x1b[36m>\x1b[0m"))
    if choice == 1:
        products()
    if choice == 2:
        customer_info()
    if choice == 3:
        quit()