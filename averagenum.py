def main():
    numbers = []

    while True:
        value = (input("Ievadi skaitļus (q lai beigtu) "))
        if value == "q":
            break
        value = float(value)
        numbers.append(value)
    
    avg = average(numbers)
    print(avg)

def average(list_of_n):
    length = len(list_of_n)
    total = sum(list_of_n)

    return total / length


main()