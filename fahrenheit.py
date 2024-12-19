def main():
    tempc = float(input("Enter a temperature in celsius "))
    convert(tempc)

def convert(temp):
    fahrenheit = (9/5) * temp + 32
    print(f"It is {fahrenheit} °F")
    return fahrenheit

main()