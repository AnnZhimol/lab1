from data import cholesterol_norm,calories_norm,sucrose_norm,dietary_fiber_norm,cost_max
from GeneticAlgorithm import genetic_algorithm
from BruteForce import brute_force

print()
print(f"Норма холестерина: {cholesterol_norm}")
print(f"Норма калорий: {calories_norm}")
print(f"Норма сахарозы: {sucrose_norm}")
print(f"Норма пищевых волокон: {dietary_fiber_norm}")
print(f"Максимальная стоимость: {cost_max}")
print()
genetic_algorithm(15, 1500)
print()
brute_force()
print()
