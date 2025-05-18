def Factorial(n):
    result = 1

    for i in range (n,1,-1):
        result*=i

    return result

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    result = Factorial(n)
    print(f"Factorial of {n} is:", result)



