#Перевірка паролю:
password = "password123"
while True:
    inp = input("Введіть пароль: ")
    if inp == password:
        print("Ви увійшли в систему.")
        break
    else:
        print("Неправильний пароль.")

#Визначення днів тижня:
days = {1: "Понеділок", 2: "Вівторок", 3: "Середа", 4: "Четвер", 5: "П'ятниця", 6: "Субота", 7: "Неділя"}
while True:
    inp = int(input("Номер дня тижня(1-7): "))
    if inp < 1 or inp > 7:
        print("Помилка: введіть число від 1 до 7")
    else:
        print("День тижня:", days[inp])

#Таблиця множення:
while True:
    n = int(input("Введіть число від 1 до 10: "))
    if 1 <= n <= 10:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
        break
    else:
        print("Неправильне число, спробуйте ще раз.")

#Сума чисел:
inp = input("Введіть числа через пробіл: ")
num_list = [int(x) for x in inp.split( )]
summation = sum(num_list)
print("Список чисел:", num_list)
print("Сума чисел:", summation)

#Робота із списками:
list = [10, 20]
list.remove(10)
print(list)

#Знаходження суми:
num_list = [2, 11, 5, 4, 3]
summation = sum(num_list)
print("Список чисел:", num_list)
print("Сума чисел:", summation)

#Подвійні значення:
numbers = [2, 5, 8, 11, 14]
doubled = [x * 2 for x in numbers]
print("Початковий список:", numbers)
print("Подвоєний список:", doubled)

#Робота із кортежами:
fruits = ("яблуко", "банан", "апельсин")
print("Перший елемент:", fruits[0])
print("Другий елемент:", fruits[1])
print("Третій елемент:", fruits[2])

#Об'єднання кортежів:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Перший кортеж:", tuple1)
print("Другий кортеж:", tuple2)
print("Об'єднаний кортеж:", combined)

#Робота із словниками:
athlete = {
    "ім'я": "Ліонель Мессі",
    "дата народження": "24 червня 1987",
    "спорт": "футбол",
    "команда": "Інтер Майамі",
    "країна": "Аргентина"
}
print("Інформація про спортсмена:")
for key, value in athlete.items():
    print(f"{key.capitalize()}: {value}")

#Оновлення словника:
books = {
    "1984": 1949,
    "Пригоди Шерлока Холмса": 1892
}
books["Linux From Scratch"] = 1999
print("Мої улюблені книги:")
for title, year in books.items():
    print(f"«{title}» — {year}")

#Пошук значення:
countries = {
    "Україна": "Київ",
    "Франція": "Париж",
    "Німеччина": "Берлін",
    "Італія": "Рим",
    "Японія": "Токіо"
}
while True:
    country = input("Введіть назву країни (або 'вихід' для завершення): ")

    if country.lower() == "вихід":
        print("Програму завершено.")
        break

    if country in countries:
        print(f"Столиця країни {country} — {countries[country]}")
    else:
        print("На жаль, інформації про цю країну немає у словнику.")