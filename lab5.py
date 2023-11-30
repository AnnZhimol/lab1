import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 1)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('Размер зарплаты')
    plt.ylabel('Размер компании')
    plt.yticks(np.arange(min(y), max(y)+1, 1.0))
    plt.text(0, 2.15, f"Коэффициент наклона: {b[1]}", fontsize=10)
    plt.text(0,2.25, f"Коэффициент смещения: {b[0]}", fontsize=10)
 
    # function to show plot
    plt.show()
 
def main():
    # observations / data
    salaryData=pd.read_csv('ds_salaries.csv',sep=',')
    n=int(len(salaryData)*0.99)
    salaryArray=salaryData['salary_in_usd'].values[:n].tolist()
    companyArray=salaryData['company_size'].replace(['S','M','L'],[0,1,2]).values[:n].tolist()
    x = np.array(salaryArray)
    y = np.array(companyArray)
 
    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
 
    # plotting regression line
    plot_regression_line(x, y, b)
 
if __name__ == "__main__":
    main()