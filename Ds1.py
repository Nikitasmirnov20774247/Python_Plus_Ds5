def tuple_path(data):
    backslash = chr(92)
    try:
        *dir, file = data.split(backslash)
        name, extension = file.split(".")
        return (backslash.join(dir), name, extension)
    except Exception as e:
        print(f'!! Введён некорректный путь до файла !!\n{e}')

data = input('Введите путь до файла: ')
print(tuple_path(data))