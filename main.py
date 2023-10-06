from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

#данные из csv
df=pd.read_csv('ds_salaries.csv')
#группировка по необходимым столбцам
task1_group=df.groupby('experience_level')["salary_in_usd"]
task2_group=df.groupby('job_title')["salary_in_usd"]
task3_group=df.groupby('company_size')["salary_in_usd"]
task4_group=df.groupby('work_year')["salary_in_usd"]

#главная страница
@app.route('/')
def index():

    #task1
    ##Значения из столбца, по которому осуществлялась группировка
    task1_column=df.groupby('experience_level')["experience_level"].first().to_frame().rename(columns={'experience_level': 'Experience Level'})

    ##Получение таблиц с максимальным/минимальным/средним значением, сгруппированных по столбцу, указанному в задании
    task1_min_table=task1_group.min().to_frame().rename(columns={'salary_in_usd': 'Min Salary (USD)'})
    task1_max_table=task1_group.max().to_frame().rename(columns={'salary_in_usd': 'Max Salary (USD)'})
    task1_mean_table=task1_group.mean().round(2).to_frame().rename(columns={'salary_in_usd': 'Mean Salary (USD)'})

    ##Получение итоговой таблицы из 4-ех предыдущих
    data=pd.concat([task1_column,task1_min_table,task1_mean_table,task1_max_table],sort=False,axis=1)

    ##Преобразование итоговой таблицы в html
    task1_table=data.to_html(index=False,header=True,table_id="table",classes="table table-striped").replace('<tr style="text-align: right;">', '<tr style="text-align: left;">')

    ##Краткий анализ полученных данных
    task1_about="По проанализированным данным можно сделать вывод, что минимальная заработная плата наблюдалась у уровня опыта " \
    + str(data[data['Min Salary (USD)'] == data['Min Salary (USD)'].min()]['Experience Level'].values[0]) \
    +", максимальная – у уровня опыта "+ str(data[data['Max Salary (USD)'] == data['Max Salary (USD)'].max()]['Experience Level'].values[0])  \
    +". Минимальная средняя заработная плата была у уровня опыта "+ str(data[data['Mean Salary (USD)'] == data['Mean Salary (USD)'].min()]['Experience Level'].values[0]) \
    +", максимальная - у уровня опыта "+ str(data[data['Mean Salary (USD)'] == data['Mean Salary (USD)'].max()]['Experience Level'].values[0])

    #task2
    ##Значения из столбца, по которому осуществлялась группировка
    task2_column=df.groupby('job_title')["job_title"].first().to_frame().rename(columns={'job_title': 'Post'})

    ##Получение таблиц с максимальным/минимальным/средним значением, сгруппированных по столбцу, указанному в задании
    task2_min_table=task2_group.min().to_frame().rename(columns={'salary_in_usd': 'Min Salary (USD)'})
    task2_max_table=task2_group.max().to_frame().rename(columns={'salary_in_usd': 'Max Salary (USD)'})
    task2_mean_table=task2_group.mean().round(2).to_frame().rename(columns={'salary_in_usd': 'Mean Salary (USD)'})

    ##Получение итоговой таблицы из 4-ех предыдущих
    data=pd.concat([task2_column,task2_min_table,task2_mean_table,task2_max_table],sort=False,axis=1)

    ##Преобразование итоговой таблицы в html
    task2_table=data.to_html(index=False,header=True,table_id="table",classes="table table-striped").replace('<tr style="text-align: right;">', '<tr style="text-align: left;">')
    
    ##Краткий анализ полученных данных
    task2_about="По проанализированным данным можно сделать вывод, что минимальная заработная плата наблюдалась у должности " \
    + str(data[data['Min Salary (USD)'] == data['Min Salary (USD)'].min()]['Post'].values[0]) \
    +", максимальная – у должности "+ str(data[data['Max Salary (USD)'] == data['Max Salary (USD)'].max()]['Post'].values[0])  \
    +". Минимальная средняя заработная плата была у должности "+ str(data[data['Mean Salary (USD)'] == data['Mean Salary (USD)'].min()]['Post'].values[0]) \
    +", максимальная - у должности "+ str(data[data['Mean Salary (USD)'] == data['Mean Salary (USD)'].max()]['Post'].values[0])

    #task3
    ##Значения из столбца, по которому осуществлялась группировка
    task3_column=df.groupby('company_size')["company_size"].first().to_frame().rename(columns={'company_size': 'Company Size'})

    ##Получение таблиц с максимальным/минимальным/средним значением, сгруппированных по столбцу, указанному в задании
    task3_min_table=task3_group.min().to_frame().rename(columns={'salary_in_usd': 'Min Salary (USD)'})
    task3_max_table=task3_group.max().to_frame().rename(columns={'salary_in_usd': 'Max Salary (USD)'})
    task3_mean_table=task3_group.mean().round(2).to_frame().rename(columns={'salary_in_usd': 'Mean Salary (USD)'})

    ##Получение итоговой таблицы из 4-ех предыдущих
    data=pd.concat([task3_column,task3_min_table,task3_mean_table,task3_max_table],sort=False,axis=1)

    ##Преобразование итоговой таблицы в html
    task3_table=data.to_html(index=False,header=True,table_id="table",classes="table table-striped").replace('<tr style="text-align: right;">', '<tr style="text-align: left;">')
    
    ##Краткий анализ полученных данных
    task3_about="По проанализированным данным можно сделать вывод, что минимальная заработная плата наблюдалась у компании размером " \
    + str(data[data['Min Salary (USD)'] == data['Min Salary (USD)'].min()]['Company Size'].values[0]) \
    +", максимальная – у компании размером "+ str(data[data['Max Salary (USD)'] == data['Max Salary (USD)'].max()]['Company Size'].values[0])  \
    +". Минимальная средняя заработная плата была у компании размером "+ str(data[data['Mean Salary (USD)'] == data['Mean Salary (USD)'].min()]['Company Size'].values[0]) \
    +", максимальная - у компании размером "+ str(data[data['Mean Salary (USD)'] == data['Mean Salary (USD)'].max()]['Company Size'].values[0])

    #task4
    ##Значения из столбца, по которому осуществлялась группировка
    task4_column=df.groupby('work_year')["work_year"].first().to_frame().rename(columns={'work_year': 'Work Year'})

    ##Получение таблиц с максимальным/минимальным/средним значением, сгруппированных по столбцу, указанному в задании
    task4_min_table=task4_group.min().to_frame().rename(columns={'salary_in_usd': 'Min Salary (USD)'})
    task4_max_table=task4_group.max().to_frame().rename(columns={'salary_in_usd': 'Max Salary (USD)'})
    task4_mean_table=task4_group.mean().round(2).to_frame().rename(columns={'salary_in_usd': 'Mean Salary (USD)'})

    ##Получение итоговой таблицы из 4-ех предыдущих
    data=pd.concat([task4_column,task4_min_table,task4_mean_table,task4_max_table],sort=False,axis=1)

    ##Преобразование итоговой таблицы в html
    task4_table=data.to_html(index=False,header=True,table_id="table",classes="table table-striped").replace('<tr style="text-align: right;">', '<tr style="text-align: left;">')
    
    ##Краткий анализ полученных данных
    task4_about="По проанализированным данным можно сделать вывод, что минимальная заработная плата наблюдалась в " \
    + str(data[data['Min Salary (USD)'] == data['Min Salary (USD)'].min()]['Work Year'].values[0]) \
    +" году, максимальная – в "+ str(data[data['Max Salary (USD)'] == data['Max Salary (USD)'].max()]['Work Year'].values[0])  \
    +" году. Минимальная средняя заработная плата была в "+ str(data[data['Mean Salary (USD)'] == data['Mean Salary (USD)'].min()]['Work Year'].values[0]) \
    +" году, максимальная - в "+ str(data[data['Mean Salary (USD)'] == data['Mean Salary (USD)'].max()]['Work Year'].values[0]) +" году."

    return render_template("index.html",task1_table=task1_table,task2_table=task2_table,task3_table=task3_table,task4_table=task4_table,task1_about=task1_about,task2_about=task2_about,task3_about=task3_about,task4_about=task4_about)

if __name__=="__main__":
    app.run(debug=True, threaded=True)