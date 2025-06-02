sum = 0
i = 0
def sum_of_digit(no):
    global sum, i
    no = str(no)
    if i < len(no):
        
        sum= sum + int(no[i])
        i = i+1
        sum_of_digit(no)
    return sum

def main():
    n = int(input("Enter the number:"))
    result = sum_of_digit(n)
    print(result)

if __name__ == "__main__":
    
    main()