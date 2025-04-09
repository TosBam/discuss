# This file is a practicing file and it's all about using datatypes to a create simple banking program
account = {}

def main():
    while True:
        print("\n... Your Bank App ...")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("6. Exit")
        #print(account)
        choice = input("Choose an Option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        #elif choice == "5"
        elif choice == '6':
            exit_app()
        else:
            print("Oops, Invalid Input")

def create_account():
    name = input("Enter your name: ")
    address = input("Provide your Address: ")
    if name in account:
        print("Name already exist")
    else:
        account[name] = {
            "address": address,
            "balance": 0
        }

    print(f"Your account has been successfully created with the name {name} and Address {address}")
    print("Registered Account", account)

def deposit_money():
    name = input("Enter your Name")
    if name not in account:
        print("Name Not Found")
    else:
        amount = float(input("Amount"))







#print(account)

main()