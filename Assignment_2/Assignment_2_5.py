def is_prime(n):
    if n <= 1:
        print("It is not prime number")
        return
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            print ("It is not prime number")
            return
        
    print("it is prime number")

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    is_prime(n)
