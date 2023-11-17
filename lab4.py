from flask import Flask, request, render_template, Response
import pandas as pd
from datetime import datetime, timedelta
import sys
from bloomfilter import BloomFilter
import csv

app = Flask('__name__')

df = pd.read_csv("ds_salaries.csv")

#read csv, and split on "," the line
csv_file = csv.reader(open('ds_salaries.csv', "r"), delimiter=",")

kaggleArr = ["my", "Жимолостнова Анна (8 вариант) — Заработная плата рабочих мест в области Data Science",
             "https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset", "Базунов Андрей (4 вариант) — Данные по инсультам",
             "https://www.kaggle.com/datasets/mohit2512/jio-mart-product-items", "Цуканова Ирина (23 вариант) — Продукты JIO",
             "https://www.kaggle.com/datasets/nancyalaswad90/yamana-gold-inc-stock-price", "Кашин Максим (13 вариант) — Цены на акции",
             ]

ArrKeyWord = ["salary", "company", "employee",
              "stroke", "glucose", "hypertension",
              "product", "category", "price",
              "yamana", "gold", "finance",
              ]

#начальная страница
@app.route('/')
def home():
    return render_template("home.html")


#справочник
@app.route('/bloom_filter', methods=['GET'])
def search():
    place=0
    data = request.args
    bloom_filter = BloomFilter(200, 100)

    for i in range(len(ArrKeyWord)):
        bloom_filter.add_to_filter(ArrKeyWord[i])

    if not bloom_filter.check_is_not_in_filter(data['keyWord']):
        for i in range(len(ArrKeyWord)):
            if ArrKeyWord[i] == data['keyWord']:
                place = i
                break

        if place // 3 == 0:
            newdf = df.iloc[0: 607]
            table=newdf.to_html(index=False,header=True,table_id="table",classes="table table-striped").replace('<tr style="text-align: right;">', '<tr style="text-align: left;">')
            return render_template('result_my_lab.html',table=table)

        else:
            return render_template("result_other.html", kaggle_link=kaggleArr[(place//3)*2], student_info=kaggleArr[(place//3)*2+1])

    else:
        return render_template("notfound.html")


# запуск HTTP-сервера
if __name__ == '__main__':
    app.run(debug=True, threaded=True)