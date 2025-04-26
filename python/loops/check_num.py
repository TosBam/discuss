# To check if a number is even or odd
def check_num():
    x = int(input("Provide a number: "))
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

check_num()

