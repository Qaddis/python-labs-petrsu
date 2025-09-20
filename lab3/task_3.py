file = open("./lab3/t3.csv", "r")

output = open("./lab3/t3.html", "a+")

lines = [
    "<!DOCTYPE html>",
    '<html lang="ru">',
    "<head>",
    '\t<meta charset="UTF-8">',
    '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    "\t<title>Задание 3 | Лабораторная работа 3</title>",
    "</head>",
    "<body>",
    "<table>",
]

for line in file:
    line_out = "<tr>"

    for value in line.split(";"):
        line_out += f"<td>{value}</td>"

    line_out += "</tr>"

    lines.append(line_out)

lines += ["</table>", "</body>", "</html>"]

output.writelines(lines)

file.close()
output.close()
