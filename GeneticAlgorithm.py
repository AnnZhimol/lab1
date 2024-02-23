from random import randint, choice,choices
from data import products, cost_max, cholesterol_norm, calories_norm, sucrose_norm, dietary_fiber_norm

# мутация обращением индивида.
# случайным образом выбирается индекс, от которого отсчитываются 3 элемента, после чего получившаяся строка инвертируется.
def mutation_individ(individ: list[int]) -> list[int]:
    index = randint(0, len(individ) - 3)

    for _ in range(3):
        reverse_part=individ[index:index+3][::-1]
        individ[index:index+3]=reverse_part

    return individ

# Двухточечное скрещивание
def crossover(population: list) -> list:
    p_size = len(population)

    for _ in range(p_size):
        parent1_id = randint(0, p_size - 1)
        parent1 = population[parent1_id]

        parent2_id = randint(0, p_size - 1)
        while parent2_id == parent1_id:
            parent2_id = randint(0, p_size - 1)

        parent2 = population[parent2_id]
        child = []

        point1 = randint(1, len(products) - 1)
        point2 = randint(1, len(products) - 1)
        while abs(point2-point1)<2:
            point2 = randint(1, len(products) - 1)
        
        if(point1>point2):
            temp=point1
            point1=point2
            point2=temp

        for j in range(0, point1):
            child.append(parent1[j])

        for j in range(point1, point2):
            child.append(parent2[j])

        for j in range(point2, len(products)):
            child.append(parent1[j])

        # мутация
        if choice([True, False]):
            child = mutation_individ(child)

        population.append(child)

    return population


# подсчет характеристик каждой особи
def individ_prop(individ: list[int]):
    cholesterol = 0
    calories = 0
    sucrose = 0
    dietary_fiber = 0
    cost = 0

    for i in range(len(individ)):
        if individ[i] == 1:
            cholesterol += products[i].cholesterol
            calories += products[i].calories
            sucrose += products[i].sucrose
            dietary_fiber += products[i].dietary_fiber
            cost += products[i].cost

    return cholesterol, calories, sucrose, dietary_fiber, cost

# получить список рациона в виде строки
def ration(individ: list[int]):
    res = 'Рацион: '
    for i in range(len(individ)):
        if individ[i] == 1:
            res += products[i].name + ',  '

    return res

# функция приспособленности
def adapt_func(individ: list[int]):
    cholesterol, calories, sucrose, dietary_fiber, cost = individ_prop(individ)
    if cost <= cost_max:
        return (cholesterol - cholesterol_norm) ** 2 + (calories - calories_norm) ** 2 + (sucrose - sucrose_norm) ** 2 + (dietary_fiber - dietary_fiber_norm) ** 2
    else:
        return 10000000

# отбор ранговым методом
def selection(population: list):
    f = []
    for individ in population:
        f.append(adapt_func(individ))

    new_population = []
    for el in [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:int(len(population)/2)]]:
        new_population.append(population[el])

    best_id = [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:1]][0]
    return new_population, population[best_id], f[best_id]

# мутации в популяции
def mutation_population(population: list) -> list:
    for i in range(len(population)):
        population[i] = mutation_individ(population[i])

    return population

# заполнение популяции
def fill_population(population_size: int) -> list:
    return [choices([0, 1], k=len(products)) for _ in range(population_size)]

def genetic_algorithm(p_size: int, generations: int):
    population = fill_population(p_size)
    f = 0
    best_variant = []
    # критерий остановки - кол-во шагов эволюции
    for _ in range(generations):
        # скрещивание
        population_after_crossover = crossover(population)

        # отбор (возвращает отобранную популяцию, лучший вариант из нее,
        # значение функции приспособленности этого варианта)
        population, best_variant, f = selection(population_after_crossover)

    print("Результат генетического алгоритма:")
    print(f'{ration(best_variant)} f = {f}')