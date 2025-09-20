h = int(input("h: "))
a = int(input("a: "))
b = int(input("b: "))

day = 1

if b > a:
    print("Улитка обречена. Увы!")

while True:
    h -= a

    if h <= 0:
        break

    h += b
    day += 1

print(day)
