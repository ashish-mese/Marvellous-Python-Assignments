i = 1
sum = 0
def sum_n(val):
    global sum, i
    if i <= val:
        sum = sum + i
        i += 1
        sum_n(val)
    return sum

def main():
    N = int(input("Enter the Number: "))
    ret = sum_n(N)
    print(ret)
   
if __name__ == "__main__":
    main()
