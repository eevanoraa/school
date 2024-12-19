def main():
    string = input("Ievadi vārdu ")
    chars = [*string]

    reverse = chars[::-1]

    if chars == reverse:
        print("Ir palindroms")
    else:
        print("Nav palindroms")


main()