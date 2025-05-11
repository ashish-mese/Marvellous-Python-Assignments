#Display even numbers using while loop:

def even_numbers():
    count = 0
    num = 2
    while count < 10:
        print(num, end=' ')
        num += 2
        count += 1

if __name__ == "__main__":
    even_numbers()

#Display Even numbers using For loop:

'''
def even_numbers():
    for i in range(2,21,2):
        print(i, end=" ")

if __name__ == "__main__":
    even_numbers()
'''