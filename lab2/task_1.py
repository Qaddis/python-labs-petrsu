inp = str(input("Строка: ")).replace(" ", "").lower()

r_inp = inp[::-1]

if inp == r_inp:
    print("Палиндром")
else:
    print("Не палиндром")
