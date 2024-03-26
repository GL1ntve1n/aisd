import re

def file(filename):
    with open(filename, 'r') as file:
        data = file.read()

    print("Все числа из файла")
    print(data)

    # Рег выражение
    proverka = r'\b\d9\d*9[02468]\b'
    numbers = re.findall(proverka, data)

    print("Числа из файла подходящие под условия:")
    for num in numbers:
        print(num, end=" ")
    print(" ")

    if numbers:
        min_number = min(map(int,numbers))
        count = len(list(filter(lambda x:int(x)==min_number,numbers)))
    else:
        min_number = None
        count = 0

    return min_number, count

filename = 'numbers.txt'
min_number, count = file(filename)
if min_number is not None:
    print(f"Минимальное число: {min_number}")
    print(f"Количество подходящих чисел: {count}")
else:
    print("В файле нет подходящих чисел")
