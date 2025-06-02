count = 0
i = 0
def count_zeros(N):
    global count, i
    if i < len(N):
        value = N[i]
        if value == "0":
            count += 1
        i += 1
        count_zeros(N)
    return count
    
def main():
    Num = input("Enter the Number: ")
    ret = count_zeros(Num)
    print(ret)
   

if __name__ == "__main__":
    main()