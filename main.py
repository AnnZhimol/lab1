from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

#главная страница
@app.route('/')
def index():
    return render_template("index.html")

#страница с данными
@app.route('/data', methods=['get'])
def data():
    #данные из input
    inputVal=request.args

    #данные из csv
    salaryData=pd.read_csv('ds_salaries.csv',sep=',')
    
    #значения строк из input
    fromStr=int(inputVal['from_str'])
    toStr=int(inputVal['to_str'])

    #значения столбцов из input
    fromStl=int(inputVal['from_stl'])
    toStl=int(inputVal['to_stl'])

    #итоговая таблица
    outputData=salaryData.iloc[fromStr:toStr,fromStl:toStl]

    #количество пустых ячеек
    countNone=salaryData.isna().sum()
    #количество заполненных ячеек
    countFill=salaryData.count()
    #количество строк
    lenStr=len(salaryData.axes[0])
    #количество столбцов
    lenStl=len(salaryData.axes[1])
    #описание набора данных
    descriptionData='В наборе данных присутствует информация о заработной плате в области DataScience. ' \
                    'Здесь представлены наиболее полные данные, с помощью которых можно проанализировать заработные платы специалистов в зависимости от различных характеристик. '
    #информация о столбцах
    stlInfo=str(salaryData.dtypes)

    #проверка диапазона
    if (fromStr>toStl | fromStl>toStl):
        return '''<center><h1>Введен некорректный диапазон</h1></center>'''+render_template("index.html")
    else:
        return render_template("data.html", countNone=countNone, countFill=countFill, lenStr=lenStr, lenStl=lenStl,
                            descriptionData=descriptionData, stlInfo=stlInfo) \
                                + "<div align='center' class='table table-bordered'>" + outputData.to_html() + "</div>"

if __name__=="__main__":
    app.run(debug=True, threaded=True)