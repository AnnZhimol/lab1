import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из файла
dataset = pd.read_csv('ds_salaries.csv')

# Извлечение зп и размера компании
salary = dataset['salary_in_usd']
sizecompany = dataset['company_size'].replace(['S','M','L'],[50.0,150.0,250.0])

# Преобразование данных в двумерный массив
X = np.array(list(zip(salary, sizecompany)))

def kmeans(X, k, max_iters=100):
    # Инициализация центроидов случайными точками из набора данных
    np.random.seed(42)
    centroids = X[np.random.choice(range(X.shape[0]), size=k, replace=False)]

    for _ in range(max_iters):
        # Расчет расстояний между точками и центроидами
        distances = np.sqrt(np.sum((X[:, np.newaxis] - centroids) ** 2, axis=2))

        # Поиск ближайшего центроида для каждой точки
        labels = np.argmin(distances, axis=1)

        # Обновление центроидов
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # Проверка на сходимость
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return labels, centroids

k = 3
labels, centroids = kmeans(X, k)

# Визуализация результатов кластеризации
plt.scatter(salary, sizecompany, c=labels, cmap='viridis', s=1)

# Настройка внешнего вида графика
plt.xlabel('Зарплата')
plt.ylabel('Размер компании')
plt.title('')

# Вывод позиций центроидов на графике
plt.text(0, 22, f"Центроиды: {centroids}", fontsize=10)

# Отображение графика
plt.show()



