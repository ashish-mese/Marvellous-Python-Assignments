def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

if __name__ == "__main__":
    number = float(input("Enter a number: "))
    check_number(number)
