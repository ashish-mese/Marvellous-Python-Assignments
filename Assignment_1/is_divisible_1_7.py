def is_divisible_by_5(num):
    if num % 5 == 0 :
        return True
    else:
        return False

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = is_divisible_by_5(number)
    print("Divisible by 5:", result)
