
def main(val1, val2):

    addition = val1 + val2
    diff = val1 - val2
    prod =  val1* val2
    division = val1 / val2

    print("Sum: ", addition)
    print("Difference: ", diff)
    print("Product: ", prod)
    print("Division: ", division)


if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    main(num1, num2)
