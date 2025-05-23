def CheckNum(num):

    if num % 2 == 0:
        return True
    else:
       return False


if __name__ == "__main__":
    N = int(input("Enter the number\n"))
    
    Res = CheckNum(N)
    if Res == True:
        print(f"{N} is Even.")
    else:
        print(f"{N} is Odd.")