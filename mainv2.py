import math
import os
os.system('cls')
print("\n")


a = float(input("What is a? "))
b = float(input("What is b? "))
c = float(input("What is c? "))


d = (b ** 2 - 4 * a * c) ** 0.5
d = d.real

if d > 0:
    print("Ir divas saknes")
elif d < 0:
    print("Nav saknes")
else:
    print("Ir viena sakne")


x_1 = (-b + d) / (2 * a)
x_2 = (-b - d) / (2 * a)

if d == 0:
    print(f"Ir tikai viena sakne un tā ir {x_1}")
else:
    print(f"x1 is {x_1:.2f}")
    print(f"x2 is {x_2:.2f}")