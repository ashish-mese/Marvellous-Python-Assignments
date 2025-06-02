i = 1
def Numbers(no):
    global i
    if i <= no:
        print (i, end = " ")
        i = i+1   
        Numbers(no)
    
def main():
    n = int(input("Enter the size:"))
    Numbers(n)

if __name__ == "__main__":
    
    main()