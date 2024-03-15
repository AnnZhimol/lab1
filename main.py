import numpy as np
import matplotlib.pyplot as plt

# график
def plot():
    x=np.linspace(a-0.1,d+0.1,1000)
    y=[calculate_complement(a, b, c, d, i) for i in x]
    plt.plot(x,y)

    for point in fuzzy_set:
        y_point = calculate_complement(a, b, c, d, point)
        plt.plot(point, y_point, 'ro', label=f'Point ({point}, {y_point:.2f})')

    plt.title("Trapezoidal fuzzy set")
    plt.xlabel("X")
    plt.ylabel("Membership")
    plt.show()

#функция пренадлежности (трапециевидная)
def calculate_complement(a, b, c, d, x):
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return 1
    elif c <= x < d:
        return (d - x) / (d - c)

# параметры функции принадлежности
a = float(input("Введите значение a для функции принадлежности: "))
b = float(input("Введите значение b для функции принадлежности: "))
c = float(input("Введите значение c для функции принадлежности: "))
d = float(input("Введите значение d для функции принадлежности:"))

#нечеткое множество
fuzzy_set = []

# кол-во элементов в нечетком множестве
n = int(input("Введите количество элементов в нечетком множестве: "))

# добавление значений в множество
for i in range(n):
    x = float(input(f"Введите {i+1}-й элемент множества: "))
    fuzzy_set.append(x)

# вычисление функции принадлежности для значений множества
complement = [calculate_complement(a, b, c, d, x) for x in fuzzy_set]

# вывод дополнения нечеткого множества и графика
print("Дополнение нечеткого множества:", [1 - x for x in complement])
plot()

# Вопросы №1 и №3

# №1 Дайте определение нечеткому множеству.
# Нечеткое множество — это математическая модель, 
# которая описывает степень принадлежности числа к данному множеству 
# с помощью функции принадлежности.

# №3 Какую операцию вы реализовали в своей лабораторной работе?
# Была реализована операция дополнение для данного нечеткого множества.
# Дополнение нечеткого множества А определяется как -A = (x,μ-A(x)), где
# μ-A(x) =1−μA(x). График дополнения множества получится перевернутым, 
# относительно исходного.
