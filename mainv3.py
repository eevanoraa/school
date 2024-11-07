year = int(input("Ievadi gadu: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Gads ir garais gads")
else:
    print("Gads nav garais gads")