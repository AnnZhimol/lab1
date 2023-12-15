from flask import Flask, request, render_template, Response
import pandas as pd
import lab6 as tr
import csv

app = Flask(__name__)

@app.route('/result')
def tree():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def tree_result():
    data = pd.read_csv('ds_salaries.csv')
    if request.method == 'POST':
        train_size = int(request.form['train_size'])
        test_size = int(request.form['test_size'])

        # Признаки для разбиения
        attributes = ['experience_level', 'job_title']

        # Целевая переменная
        target_column = 'salary_in_usd'

        # Выборка данных для обучения
        train_data = data.head(train_size)

        # Выборка данных для проверки
        test_data = data.tail(test_size)

        # Построение дерева решений
        decision_tree = tr.build_decision_tree(train_data, target_column, attributes)

        # Вывод дерева решений
        result_tree = tr.print_decision_tree(decision_tree)

        # Прогнозирование и вывод результатов проверки
        results = []
        for index, row in test_data.iterrows():
            prediction = tr.predict(decision_tree, row, data['salary_in_usd'].mode().iloc[0])
            results.append(f"Actual: {row[target_column]}, Predicted: {prediction}")

    return render_template('index.html', result_tree=result_tree, results=results)

if __name__=="__main__":
    app.run(debug=True)