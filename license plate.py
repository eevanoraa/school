import re

plate = str(input("Ievadi numuru zimi (AB-1234): "))
plate = plate.strip().upper()

    # Regex izskaidrojums:
    # ^                 - String sākums
    # [A-PR-VZ]{2}      - Tieši divi burti (izņemot Q, W, Y)
    # -                 - Svītra starp burtiem un skaitļiem
    # [1-9]\d{0,3}     - 1-4 cipari, sākot ar 1-9 tā, lai numuru zīmes nevarētu sākties ar 0
    # $                 - String beigas
pattern = r'^[A-PR-VZ]{2}-[1-9]\d{0,3}$'

test = (bool(re.match(pattern, plate)))
if test:
    print("Numurs ir derīgs")
else:
    print("Numurs nav derīgs")