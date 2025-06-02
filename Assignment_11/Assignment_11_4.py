i = 1
Result = 1
def Cal_Power(x, n):
    global i, Result
    if i <= n:
        Result = Result * x
        i =i + 1
        Cal_Power(x, n)
    return Result

def main():
    Num = int(input("Enter value: "))
    Power = int(input("Enter power of: "))
    ret = Cal_Power(Num, Power )
    print(ret)
   

if __name__ == "__main__":
    main()