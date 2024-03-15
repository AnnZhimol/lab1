import numpy as np
import matplotlib.pyplot as plt

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

def calculate_complement(a, b, c, d, x):
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return 1
    elif c <= x < d:
        return (d - x) / (d - c)

a = float(input("Введите значение a для функции принадлежности: "))
b = float(input("Введите значение b для функции принадлежности: "))
c = float(input("Введите значение c для функции принадлежности: "))
d = float(input("Введите значение d для функции принадлежности:"))

fuzzy_set = []

n = int(input("Введите количество элементов в нечетком множестве: "))

for i in range(n):
    x = float(input(f"Введите {i+1}-й элемент множества: "))
    fuzzy_set.append(x)

complement = [calculate_complement(a, b, c, d, x) for x in fuzzy_set]

print("Дополнение нечеткого множества:", [1 - x for x in complement])
plot()
