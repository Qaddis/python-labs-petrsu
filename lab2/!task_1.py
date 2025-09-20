inp = str(input("Строка: "))

r_inp = inp[::-1]

print(r_inp)

if inp.lower() == r_inp.lower():
    print("Палиндром")
else:
    print("Не палиндром")
