def main(num1, num2, num3):

    if num1 >= num2:
        if num1 >= num3:
            largest = num1
        else:
            largest = num3
    else:
        if num2 >= num3:
            largest = num2
        else:
            largest = num3

    print("largest number: ", largest)

if __name__ == "__main__":
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    num3 = float(input("Enter 3rd number: "))
    main(num1, num2, num3)
