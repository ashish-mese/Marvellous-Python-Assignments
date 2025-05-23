def Palindrome(A):
    return A == A[::-1]

if __name__ == "__main__":
    
    Word = input("Enter the String: ")
    
    if Palindrome(Word):
        print(Word, "is a Palindrome")
    else:
        print(Word, "is not a Palindrome")