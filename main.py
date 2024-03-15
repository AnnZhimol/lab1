import numpy as np
import matplotlib.pyplot as plt

class LinguisticScale:
    def __init__(self, num_labels=5):
        self.num_labels = num_labels
        self.label_names = [f'Label {i+1}' for i in range(self.num_labels)] 
        self.membership_functions = []
        self.colors = ['r', 'g', 'b', 'y', 'm']
    
    def set_label_names(self, names):
        self.label_names = names

    def set_membership_functions (self, functions): 
        self.membership_functions=functions

    def plot_scale(self):
        x = np.linspace(0, 24, 1000)
        for i, func in enumerate(self.membership_functions):
            y = func(x)
            plt.plot(x, y, label=self.label_names[i], color=self.colors[i]) 
        plt.title('Оценка загруженности сервера и сети')
        plt.xlabel("Время суток") 
        plt.ylabel('Коэффициент загруженности сервера и сети')
        plt.legend() 
        plt.show()

    def membership_degree(self, value):
        degrees = []
        for func in self.membership_functions:
            degrees.append(func(value))
        return degrees

def triangular_function(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

def trapezoidal_function(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)))

def main():
    scale = LinguisticScale()
    
    label_names = []
    membership_functions=[]
    
    # Запрашиваем у пользователя количество и названия меток 
    num_labels = int(input("Введите количество меток на шкале: "))
    
    if num_labels > 5:
        num_labels = 5
        print("К сожалению, макисмальное количество отметок = 5") 
    
    for i in range(num_labels):
        name = input(f"Введите название метки {i+1}: ")
        label_names.append(name)

    # Устанавливаем названия меток
    scale.set_label_names(label_names)

    # Запрашиваем у пользователя параметры функций принадлежности
    print("Выберите тип функции принадлежности: ")
    print("1. Треугольная функция")
    print("2. Трапециевидная функция")
    for i in range(num_labels):
        choice = int(input(f"Выберите тип функции для метки '{label_names[i]}': "))
        if choice == 1:
            a = float(input("Введите а: "))
            b = float(input("Введите b: "))
            c = float(input("Введите с: "))
            membership_functions.append(lambda x, a=a, b=b, c=c: triangular_function(x, a, b, c)) 
        elif choice == 2:
            a = float(input("Введите а: "))
            b = float(input("Введите b: "))
            c = float(input("Введите с: "))
            d = float(input("Введите d: "))
            membership_functions.append(lambda x, a=a, b=b, c=c, d=d: trapezoidal_function(x, a, b, c, d))

    # Устанавливаем функции принадлежности
    scale.set_membership_functions(membership_functions)
    # Отображаем шкалу
    scale.plot_scale()
    # Пользователь вводит значение для оценки степени принадлежности
    while(True):
        degrees = scale.membership_degree(float(input("Введите значение для оценки степени принадлежности: "))) 
        load = (float(input("Введите коэффициент загруженности сети и сервера: ")))
        for i, degree in enumerate(degrees):
            print(f"Степень принадлежности к метке '{scale.label_names[i]}': {degree}")
            if (degree > load):
                print(f'Загруженность к метке "{scale.label_names[i]}" является высокой')
            else:
                print(f'Загруженность к метке "{scale.label_names[i]}" является низкой')

main()