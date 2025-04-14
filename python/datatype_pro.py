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
    name = input("Enter Your Name: ")
    if name not in account:
        print("Account Not Found")
    else:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Invalid Request")
            else:
                account[name]["balance"] += amount
                print(f"Money deposited successfully. New balance is {account[name]["balance"]}")
        except ValueError:
            print("Invalid! Please enter valid number.")


def withdraw_money():
    name = input("Enter Your Name: ")
    if name not in account:
        print("Account Not found")
    else:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount")
            elif account[name]["balance"] >= amount:
                account[name]["balance"] -= amount
                print(f"Withdrawal successfull, Your balance is {account[name]["balance"]}")
            else:
                print("Insufficient funds, please credit your account")
        except ValueError:
            print("Invalid request")


def check_balance():
    name = input("Enter your name: ")
    if name not in account:
        print("Account not found")
    else:
        print(f"Your account balance is {account[name]["balance"]}")


def exit_app():
    print("Thanks for banking with us")
    exit()








#print(account)

main()