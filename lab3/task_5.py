ALPH = sorted("qwertyuiopasdfghjklzxcvbnm")

source = open("./lab3/t5.txt", "r")


def get_mask(key: str, message: str) -> str:
    return (key * (len(message) // len(key))) + key[: (len(message) % len(key))]


# Шифр Виженера
def encoder():
    key = str(input("Ключ: "))
    filename = str(input("Имя итогового файла: "))

    output = open(f"./lab3/{filename}", "a+")

    for line in source:
        encoded_line = ""
        mask = get_mask(key, line)

        for i in range(len(line)):
            if ALPH.count(line[i]):
                encoded_line += ALPH[
                    (ALPH.index(line[i]) + ALPH.index(mask[i])) % len(ALPH)
                ]
            elif ALPH.count(line[i].lower()):
                encoded_line += ALPH[
                    (ALPH.index(line[i].lower()) + ALPH.index(mask[i])) % len(ALPH)
                ].upper()
            else:
                encoded_line += line[i]

        output.write(encoded_line)

    output.close()


def decoder():
    filename = str(input("Зашифрованный файл: "))
    key = str(input("Ключ: "))

    target = open(f"./lab3/{filename}", "r")

    for line in target:
        decoded_line = ""
        mask = get_mask(key, line)

        for i in range(len(line)):
            if ALPH.count(line[i]):
                decoded_line += ALPH[
                    (ALPH.index(line[i]) - ALPH.index(mask[i])) % len(ALPH)
                ]
            elif ALPH.count(line[i].lower()):
                decoded_line += ALPH[
                    (ALPH.index(line[i].lower()) - ALPH.index(mask[i])) % len(ALPH)
                ].upper()
            else:
                decoded_line += line[i]

        print(decoded_line, end="")

    target.close()


mode = int(input("Выберите режим (1. шифратор, 2. дешифратор): "))

if mode == 1:
    encoder()
elif mode == 2:
    decoder()
else:
    print("Читать умеешь? Тебе какие варианты предложили?")
