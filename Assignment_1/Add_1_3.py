def add(a, b):
    sum = a + b
    return sum

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add(num1, num2)
    print("The sum is:", result)
