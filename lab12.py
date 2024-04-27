class FuzzySet:
    def __init__(self, values):
        self.values = values

    def triangular(self, value):
        a, b, c = self.values
        if a <= value <= b:
            return round((value - a) / (b - a), 3)
        elif b < value <= c:
            return round((c - value) / (c - b), 3)
        elif value < a or value > c:
            return 0

    def trapezoid(self, value):
        a, b, c, d = self.values
        if a <= value <= b:
            return round((value - a) / (b - a), 3)
        elif b < value < c:
            return 1
        elif c <= value <= d:
            return round((d - value) / (d - c), 3)
        elif value < a or value > d:
            return 0

class FuzzyLogic:
    def __init__(self):
        self.imt = {
            'deficiency': FuzzySet([0, 0, 16, 19]),
            'normal': FuzzySet([17, 22, 26]),
            'excess': FuzzySet([24, 28, 31]),
            'obesity': FuzzySet([29, 32, 50, 50])
        }

        self.glucose = {
            'low': FuzzySet([0, 0, 3.2, 3.5]),
            'normal': FuzzySet([3.1, 4.2, 5.7]),
            'high': FuzzySet([5.3, 5.5, 10, 10])
        }

        self.diabetes_probability = {
            'low': [0, 0, 10, 40],
            'medium': [30, 55, 80],
            'high': [75, 100, 100, 100]
        }

        self.rules = [
            ['deficiency', 'low', 'low'],
            ['deficiency', 'normal', 'low'],
            ['deficiency', 'high', 'medium'],
            ['normal', 'low', 'low'],
            ['normal', 'normal', 'low'],
            ['normal', 'high', 'medium'],
            ['excess', 'low', 'medium'],
            ['excess', 'normal', 'medium'],
            ['excess', 'high', 'high'],
            ['obesity', 'low', 'medium'],
            ['obesity', 'normal', 'high'],
            ['obesity', 'high', 'high']
        ]

    def defuz_trapezoid(param1,param2):
        return (param1 + param2) / 2

    def run(self, input_imt, input_glucose):
        res_impl = []
        for item in self.rules:
            # степень принадлежности для значения "индекс массы тела"
            first = self.imt[item[0]].triangular(input_imt) if len(self.imt[item[0]].values) == 3 \
            else self.imt[item[0]].trapezoid(input_imt)

            # степень принадлежности для значения "уровень глюкозы"
            second = self.glucose[item[1]].triangular(input_glucose) if len(self.glucose[item[1]].values) == 3 \
            else self.glucose[item[1]].trapezoid(input_glucose)

            # нечеткое И (минимальное) = имитация моделируется через минимум
            res_impl.append(min(first, second))

        agr = max(res_impl)
        # полученное нечеткое значение вероятности диабета
        res_str = self.rules[res_impl.index(agr)][2]
        print(res_str)
        # полученное четкое значение вероятности диабета
        return self.diabetes_probability.get(res_str)[1] if len(self.diabetes_probability.get(res_str)) == 3 \
            else (self.diabetes_probability.get(res_str)[1]+self.diabetes_probability.get(res_str)[2])/2


logic = FuzzyLogic()
input_imt = float(input("Введите индекс массы тела [0, 50]: "))
input_glucose = float(input("Введите уровень глюкозы [0, 10]: "))

diabetes_probability = logic.run(input_imt, input_glucose)

print(f'Вероятность диабета: {diabetes_probability}%')