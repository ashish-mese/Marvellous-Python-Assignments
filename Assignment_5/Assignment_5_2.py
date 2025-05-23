def main(character):

    if character.lower() in 'aeiou':
        print(character, "is a vowel")
    else:
        print(character, "is a consonant")

if __name__ == "__main__":
    character = input("Enter a single character: ")
    main(character)
