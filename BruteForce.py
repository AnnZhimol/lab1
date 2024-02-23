from data import products, cost_max, cholesterol_norm, calories_norm, sucrose_norm, dietary_fiber_norm
from GeneticAlgorithm import ration, adapt_func

def brute_force():
    stop = ''
    for _ in products:
        stop += "1"

    k = 0
    min_f = 1000000
    best_variant = []
    while True:
        binary = f'{k:010b}'
        if binary == stop:
            break

        cholesterol, calories, sucrose, dietary_fiber, cost = 0, 0, 0, 0, 0
        variant = []
        for index, c in enumerate(binary):
            variant.append(int(c))
            if c == '1':
                cholesterol += products[index].cholesterol
                calories += products[index].calories
                sucrose += products[index].sucrose
                dietary_fiber += products[index].dietary_fiber
                cost += products[index].cost

        f = (cholesterol - cholesterol_norm) ** 2 + (calories - calories_norm) ** 2 + (sucrose - sucrose_norm) ** 2 + (dietary_fiber - dietary_fiber_norm) ** 2
        if f < min_f and cost <= cost_max:
            min_f = f
            best_variant = variant

        k += 1

    print("Результат полного перебора:")
    print(f'{ration(best_variant)} f = {adapt_func(best_variant)}')