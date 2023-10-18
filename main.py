from flask import Flask, render_template, request
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def graphic(category,val):
    df_One=pd.read_csv('new_ds_salaries.csv').groupby(category).agg(salary_in_usd=('salary_in_usd', val)).reset_index()
    df_Two=pd.read_csv('ds_salaries.csv').groupby(category).agg(salary_in_usd=('salary_in_usd', val)).reset_index()
    df_One['salary_in_usd'] = df_One['salary_in_usd'].apply(lambda x: round(x, 1))
    df_Two['salary_in_usd'] = df_Two['salary_in_usd'].apply(lambda x: round(x, 1))

    fig, ax = plt.subplots()

    index = np.arange(len(df_One[category]))
    bar_width = 0.35
    opacity = 0.8

    pps=ax.bar(index, df_One['salary_in_usd'], color='r', align='edge', width=bar_width, label = 'Новая таблица')
    for p in pps:
        height = p.get_height()
        ax.annotate('{}'.format(height),
        xy=(p.get_x() + p.get_width() / 2, height),
        xytext=(0, 3), # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom')
    
    pps2=ax.bar(index, df_Two['salary_in_usd'], color='b', align='edge', width=-bar_width,label = 'Старая таблица')
    for p in pps2:
        height = p.get_height()
        ax.annotate('{}'.format(height),
        xy=(p.get_x() + p.get_width() / 2, height),
        xytext=(0, 3), # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom')

    # Assign the tick labels
    ax.set_xticks(index)
    ax.set_xticklabels(df_One[category], rotation=90)

    plt.xlabel(category)
    plt.ylabel(val)
    plt.legend()
    plt.show()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data', methods=['get'])
def data():
    
    valueForGroup = request.args.get('flexRadioDefault')
    valueForVal = request.args.get('flexRadioDefault2')
    graphic(valueForGroup,valueForVal)
    
    return render_template("data.html") 

if __name__=="__main__":
    app.run(debug=True, threaded=True)

def new_df():
    df=pd.read_csv('ds_salaries.csv')

    for i in range(len(df),round(len(df)*1.1)+1):
        experience_level = df['experience_level'].value_counts().index[random.randint(0,2)]
        employment_type=df['employment_type'].value_counts().index[random.randint(0,2)]
        job_title=df['job_title'].value_counts().index[random.randint(0,2)]
        salary_currency=df['salary_currency'].value_counts().index[random.randint(0,2)]
        employee_residence=df['employee_residence'].value_counts().index[random.randint(0,2)]
        remote_ratio=df['remote_ratio'].value_counts().index[random.randint(0,2)]
        company_location=df['company_location'].value_counts().index[random.randint(0,2)]
        company_size=df['company_size'].value_counts().index[random.randint(0,2)]
        work_year=df['work_year'].value_counts().index[random.randint(0,2)]

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
