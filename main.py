#from flask import Flask, render_template, request
import pandas as pd
import random
import matplotlib.pyplot as plt

def graphic():
    df=pd.read_csv('new_ds_salaries.csv')

    d = df.groupby('job_title').agg(salary_in_usd=('salary_in_usd', 'max')).reset_index()
    d['salary_in_usd'] = d['salary_in_usd'].apply(lambda x: round(x, 1))
    plt.xlabel('Профессии')
    plt.ylabel('Средняя зарплата в долларах')
    barplot = plt.bar(x=d['job_title'], height=d['salary_in_usd'])
    plt.bar_label(barplot, labels=d['salary_in_usd'])
    plt.xticks(rotation=90)

    df=pd.read_csv('ds_salaries.csv')

    d = df.groupby('job_title').agg(salary_in_usd=('salary_in_usd', 'max')).reset_index()
    d['salary_in_usd'] = d['salary_in_usd'].apply(lambda x: round(x, 1))
    plt.xlabel('Профессии')
    plt.ylabel('Средняя зарплата в долларах')
    barplot = plt.bar(x=d['job_title'], height=d['salary_in_usd'])
    plt.bar_label(barplot, labels=d['salary_in_usd'])
    plt.xticks(rotation=90)
    plt.show()

graphic()

def new_df():
    df=pd.read_csv('ds_salaries.csv')

    for i in range(len(df),round(len(df)*1.1)+1):
        experience_level = df['experience_level'].value_counts().index[random.randint(0,2)]
        employment_type=df['employment_type'].value_counts().index[random.randint(0,2)]
        job_title=df['job_title'].value_counts().index[random.randint(0,2)]
        salary_currency=df['salary_currency'].value_counts().index[random.randint(0,2)]
        employee_residence=df['employee_residence'].value_counts().index[random.randint(0,2)]
        remote_ratio=df['remote_ratio'].value_counts().index[random.randint(0,1)]
        company_location=df['company_location'].value_counts().index[random.randint(0,2)]
        company_size=df['company_size'].value_counts().index[random.randint(0,1)]
        work_year=df['work_year'].value_counts().index[random.randint(0,1)]

        max_salary=df['salary'].max()
        min_salary=df['salary'].min()
        avg_salary=df['salary'].mean()
        new_salary=round(avg_salary + random.uniform(min_salary - avg_salary, max_salary - avg_salary))

        max_salary_usd=df['salary_in_usd'].max()
        min_salary_usd=df['salary_in_usd'].min()
        avg_salary_usd=df['salary_in_usd'].mean()
        new_salary_usd=round(avg_salary_usd + random.uniform(min_salary_usd - avg_salary_usd, max_salary_usd - avg_salary_usd))

        new_row=[i,work_year,experience_level,employment_type,job_title,new_salary,salary_currency,new_salary_usd,employee_residence,remote_ratio,company_location,company_size]
        df.loc[i]=new_row

    df.to_csv('new_ds_salaries.csv',index=False)

#new_df()

# app = Flask(__name__)

# #главная страница
# @app.route('/')
# def index():
#     return render_template("index.html")

# #страница с данными
# @app.route('/data', methods=['get'])
# def data():
#     #данные из input
#     inputVal=request.args

#     #данные из csv
#     salaryData=pd.read_csv('ds_salaries.csv',sep=',')
    
#     #значения строк из input
#     fromStr=int(inputVal['from_str'])
#     toStr=int(inputVal['to_str'])

#     #значения столбцов из input
#     fromStl=int(inputVal['from_stl'])
#     toStl=int(inputVal['to_stl'])

#     #итоговая таблица
#     outputData=salaryData.iloc[fromStr:toStr,fromStl:toStl]

#     #количество пустых ячеек
#     countNone=salaryData.isna().sum()
#     #количество заполненных ячеек
#     countFill=salaryData.count()
#     #количество строк
#     lenStr=len(salaryData.axes[0])
#     #количество столбцов
#     lenStl=len(salaryData.axes[1])
#     #описание набора данных
#     descriptionData='В наборе данных присутствует информация о заработной плате в области DataScience. ' \
#                     'Здесь представлены наиболее полные данные, с помощью которых можно проанализировать заработные платы специалистов в зависимости от различных характеристик. '
#     #информация о столбцах
#     stlInfo=str(salaryData.dtypes)
#     #таблица html
#     tableHtml=outputData.to_html(classes='table table-striped')

#     #проверка диапазона
#     if (fromStr>toStl | fromStl>toStl):
#         return '''<center><h1>Введен некорректный диапазон</h1></center>'''+render_template("index.html")
#     else:
#         return render_template("data.html", countNone=countNone, countFill=countFill, lenStr=lenStr, lenStl=lenStl,
#                             descriptionData=descriptionData, stlInfo=stlInfo) \
#                             + '''<div class="container mt-4"><div class="card"><div class="card-body" style="overflow: auto">'''+ tableHtml + '''</div></div></div>''' 

# if __name__=="__main__":
#     app.run(debug=True, threaded=True)