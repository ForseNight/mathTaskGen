import random

glasses = 0
errors = 0

set1 = int(input("Начальное число: "))
set2 = int(input("Конечное чисор: "))

print()

def task():
    try:
        global glasses
        global errors
        num1 = random.randint(set1, set2)
        num2 = random.randint(set1, set2)
        set3 = random.randint(1, 4)
        simbol = "-"

        if set3 == 1:
            simbol = "+"
        if set3 == 2:
            simbol = "-"
        if set3 == 3:
            simbol = "*"
        if set3 == 4:
            simbol = "/"

        if simbol == "+":
            result = num1 + num2
        elif simbol == "-":
            result = num1 - num2
        elif simbol == "/":
            result = num1 / num2
        elif simbol == "*":
            result = num1 * num2

        if num2 < 0:
            reply = input(f"Дай ответ ответ данной задаче: {num1} {simbol} ({num2}) = ?\nОтвет: ")
        else:
            reply = input(f"Дай ответ ответ данной задаче: {num1} {simbol} {num2} = ?\nОтвет: ")

        if int(reply) == result:
            print("Верный ответ !\n")
            glasses += 1
        else:
            print("Вы допустили ошибку !\n")
            errors += 1
    except:
        print(f"\nПравильных: {glasses}\nОшибок: {errors}\n")
        
while True:
    task()

input()