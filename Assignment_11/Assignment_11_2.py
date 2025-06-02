ret = 1
def fact(no):
    global ret
    
    if no >= 1:

        ret = no*ret
        no = no-1
        fact(no)
    return ret
    
def main():
    n = int(input("Enter the number:"))
    result = fact(n)
    print(result)

if __name__ == "__main__":
    
    main()