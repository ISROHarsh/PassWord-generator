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
    products.add_row(["1","Gulab Jamun",f"₹{500}"])
    products.add_row(["2","Rasmalai",f"₹{600}"])
    products.add_row(["3","Motichoor Ladoo",f"₹{400}"])
    products.add_row(["4","Boondi",f"₹{200}"])
    products.add_row(["5","Rasgulla",f"₹{300}"])
    products.add_row(["6","Kaju Katli",f"₹{1000}"])
    products.add_row(["7","Jalebi",f"₹{350}"])
    products.add_row(["8","Bareli ki Barfi",f"₹{500}"])
    products.add_row(["9","SoanPapdi",f"₹{600}"])
    products.add_row(["10","Agra ka Petha",f"₹{250}"])
    return print(products)

sr_no = ["1","2","3","4","5","6","7","8","9","10"]
prod_name = ["Gulab Jamun","Rasmalai","Motichoor Ladoo","Boondi","Rasgulla","Kaju Katli","Jalebi","Bareli ki Barfi","SoanPapdi","Agra ka Petha"]
price_kg = [500,600,400,200,300,1000,350,500,600,250]

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
        customer_info()

def purchase():
    while True:
        try:
            product_no = input("Enter the product no. : ")
            if not product_no:
                print(" Please enter a valid choice")
            quan = float(input("Enter Qauntity in Kg : "))
            price = quan * price_kg[int(product_no)]
            i = 0
            bag = input(f' Carry bag ₹10 (Y/N)> ')
            if bag not in ["Y", "N", "YES", "NO"]:
                print(" Please enter a valid choice (Y/N)")
                input("Press ANY KEY to continue" )
                banner()
                # invoice()
                if bag in ["Y","YES","y","yes"]:
                    i += price 
                    total = i + 10
                else:
                    i += price
        except KeyboardInterrupt:
            banner()
            main_menu()
        except Exception as e:
            print(f"[\x1b[31m!\x1b[0m] {e.args}")
            input(f'\u001b[0m[\x1b[\x1b[38;5;63m#\u001b[0m] Press ANY KEY to continue')
            banner()
            purchase()


banner()

while True:
    main_menu()
    choice = int(input("choose a option\x1b[36m>\x1b[0m"))
    if choice == 1:
        products()
    if choice == 2:
        customer_info()
        purchase()
    if choice == 3:
        quit()
