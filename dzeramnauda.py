def main():
    eur = eur_to_float(input("Cik maksāja pusdienas? "))
    valuta = ""
    eur = valuta
    procenti = procenti_to_float(input("Cik procentus maksāsi viesmīlim dzeramnaudā? "))
    dzeramnauda = eur * procenti
    print(f"Jāatstāj {valutas} {dzeramnauda:.2f}")

def eur_to_float(eur_value):
    for word in eur_value.split():
        try:
            number = (float(word))
        except ValueError:
            pass
    
    return number

def valutas(teikums):
    for word in teikums.split():
        try:
            pass
        except ValueError:
            valuta = 

# valutas funkcija atrast no teikuma to valutu ko ievada.


def procenti_to_float(procent_value):
    for word in procent_value.split():
        try:
            percentage = (float(word))
        except ValueError:
            pass
    return percentage / 100
    

main()