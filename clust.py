import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Генерация случайных данных о размере площадей n квартир
n = 200
square = np.random.randint(15, 100, n)

# Инициализация переменных
k = 3  # количество кластеров
m = 2  # параметр нечёткости
max_iterations = 100 # кол-во итераций алгоритма
tolerance = 1e-4 # параметр сходимости алгоритма

# Инициализация центров кластеров случайным образом
centers = np.random.randint(min(square), max(square), size=k)
centers.sort()

for _ in range(max_iterations):
    membership_matrix = np.zeros((n, k)) # заполнение матрицы принадлежности нулевыми значениями
    # Вычисление функций принадлежности
    for i in range(n):
        x = square[i]
        for j in range(k):
            if np.abs(x - centers[j]) == 0:
                membership_matrix[i][j] = 1
            else:
                membership_matrix[i][j] = 1 / sum((np.abs(x - centers[j]) / np.abs(x - centers)) ** (2 / (m - 1) + 1e-8))

    # Обновление центров кластеров
    new_centers = np.dot(membership_matrix.T, square) / np.sum(membership_matrix, axis=0)

    # Проверка на сходимость
    if np.sum(np.abs(new_centers - centers)) < tolerance:
        break
    
    centers = new_centers

# Определение принадлежности каждого объекта к кластеру
clusters = np.argmax(membership_matrix, axis=1)

# Вывод результатов
print("Размеры площадей квартир:")
print(square)
print("\nЦентры кластеров:")
print(centers)
print("\nПринадлежность к кластерам:")
print(clusters)

# Вывод результатов на трехмерный график
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']

for idx, cluster_id in enumerate(clusters):
    ax.scatter(membership_matrix[idx][0], membership_matrix[idx][1], membership_matrix[idx][2],
               color=colors[cluster_id], s=50, alpha=0.5)

ax.set_xlabel('Маленькая')
ax.set_ylabel('Средняя')
ax.set_zlabel('Большая')
ax.set_title('Нечеткая кластеризация в трехмерном пространстве. Площадь квартиры')
plt.show()