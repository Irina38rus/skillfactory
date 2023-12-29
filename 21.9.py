# Задание 1:
# Создайте метод, который возвращает атрибуты прямоугольника как строку (магический метод __str__)
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'
#
# rect_1 = Rectangle(5, 10, 50,100)
# print(rect_1)

# Задание 2:
# На выходе в консоли вам необходимо получить площадь данной фигуры.
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def get_area(self):
#         return self.width * self.height
#
# rect_1 = Rectangle(5, 10, 50,100)
# print(rect_1.get_area())

# Задание 3:
# Сделайте вывод о клиентах в консоль в формате: «Иван Петров. Москва. Баланс: 50 руб.»
# class Client:
#     def __init__(self, name, surname, city, balance):
#         self.name = name
#         self.surname = surname
#         self.city = city
#         self.balance = balance
#
#     def __str__(self):
#             return f'"{self.name} {self.surname}". {self.city}. Баланс: {self.balance} руб."'
#
# client_1 = Client('Иван', 'Петров', 'Москва', 50)
# print(client_1)

# Задание 4:
# составить список гостей (имя, фамилия и город)
class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def get_guest(self):
        return f'{self.name} {self.surname}, {self.city}'


client_1 = Client('Иван','Охлобыстин','Москва',33)
client_2 = Client('Гоша','Куценко','Уфа',10)
client_3 = Client('Марья','Краса','Дерюгино',15)
client_4 = Client('Василиса','Премудрая','Лесное',115)

guest_list=[client_1, client_2, client_3, client_4]

for guest in guest_list:
    print(guest.get_guest())