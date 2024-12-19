def main():
    eur, valuta = eur_to_float(input("Cik maksāja pusdienas? "))
    procenti = procenti_to_float(input("Cik procentus maksāsi viesmīlim dzeramnaudā? "))
    dzeramnauda = eur * procenti
    print(f"Jāatstāj {dzeramnauda:.2f} {valuta}")

def eur_to_float(eur_value):
    number = None
    currency = None
    for word in eur_value.split():
        try:
            number = float(word)
        except ValueError:
            currency = word
    return number, currency

def procenti_to_float(procent_value):
    percentage = None
    for word in procent_value.split():
        try:
            percentage = float(word)
        except ValueError:
            pass
    return percentage / 100


if __name__ == "__main__":
    main()
