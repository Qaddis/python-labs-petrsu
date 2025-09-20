proc_text = open("./lab3/t1.txt", "r").read().replace("\t", " ").replace("\n", " ")

print(f"Кол-во строк: {len(list(open("./lab3/t1.txt", "r")))}")
print(f"Кол-во слов: {len(proc_text.split(' '))}")
print(f"Кол-во символов: {len(proc_text.replace(' ', ''))}")
