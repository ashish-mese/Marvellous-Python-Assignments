def ChkNum(number):
    if number % 2 == 0:
        Ans = "Even number"
    else:
        Ans = "Odd number"
    return Ans

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    Result=ChkNum(num)
    print(Result)
