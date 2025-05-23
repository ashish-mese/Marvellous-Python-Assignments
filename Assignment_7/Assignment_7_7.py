def isprime(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def main(size):
    data = []
    for i in range (size+1):
        val = int(input("ENter the number: "))
        data.append(val)
    prime = list(filter(isprime, data))
    return prime

if __name__ == "__main__":
    size = int(input("Enter size: "))
    res = main(size)
    print(res)
