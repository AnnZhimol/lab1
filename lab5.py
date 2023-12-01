import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
def estimate_coef(x, y):
    # количество наблюдений/точек
    n = np.size(x)
 
    # среднее значение вектора x и y
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # вычисление перекрестного отклонения и отклонения относительно x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # расчет коэффициентов регрессии
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)
 
def plot_regression_line(x, y, b):
    # построение фактических точек в виде точечной диаграммы
    plt.scatter(x, y, color = "m",
               marker = "o", s = 1)
 
    # прогнозируемый вектор ответа
    y_pred = b[0] + b[1]*x
 
    # построение линии регрессии
    plt.plot(x, y_pred, color = "g")
 
    # конфигурация
    plt.xlabel('Размер зарплаты')
    plt.ylabel('Размер компании')
    plt.yticks(np.arange(min(y), max(y)+100, 100.0))
    plt.text(0, 1050, f"Коэффициент наклона: {b[1]}", fontsize=10)
    plt.text(0,1150, f"Коэффициент смещения: {b[0]}", fontsize=10)
 
    # функция для отображения графика
    plt.show()
 
def main():
    # наблюдения/данные
    salaryData=pd.read_csv('ds_salaries.csv',sep=',')
    n=int(len(salaryData)*0.99)
    salaryArray=salaryData['salary_in_usd'].values[:n].tolist()
    companyArray=salaryData['company_size'].replace(['S','M','L'],[50,150,250]).values[:n].tolist()
    x = np.array(salaryArray)
    y = np.array(companyArray)
 
    # оценочные коэффициенты
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
 
    # построение линии регрессии
    plot_regression_line(x, y, b)
 
if __name__ == "__main__":
    main()