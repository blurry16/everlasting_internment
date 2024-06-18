characters = {
    "Рома": "rm",
    "Вика": "vi",
    "Андрей": "le",
    "Соня": "sa",
    "…": "dreamgirl",
    "...": "dreamgirl",
}

with open(
    r"D:\Everlasting Summer\game\mods\everlasting_internment\src\input.txt",
    "r",
    encoding="UTF-8",
) as file:
    data = file.readlines()

for index, i in enumerate(data):
    if "~" == data[index][0]:
        data[index] = f'th "{i[2:-3]}"\n'
    elif ":" in i.split()[0]:
        character = i.split()[0][:-1]
        if character in characters:
            data[index] = f'{characters[character]} "{i[len(character) + 2:-1]}"\n'
        else:
            print(f"Unknown character! -> {character}")
    else:
        data[index] = f'"{i[:-1]}"\n'

print("".join(data))
