def factor_of(num):  
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    total = 0
    for i in (factors):
        total += i


    return total

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Sum of factors of {num} are:", factor_of(num))