from product import Product

cholesterol_norm = 100
calories_norm = 600
sucrose_norm = 10
dietary_fiber_norm = 10
cost_max = 400

max_diff_cholesterol=50
max_diff_calories=100
max_diff_sucrose=2
max_diff_dietary_fiber=2

products = [
    Product('Горошек зелёный вареный без соли', 120, 84, 0, 5, 6),
    Product('Бифштекс из говядины', 300, 216, 95, 0, 0),
    Product('Молоко 1,5% жирности стерилизованное', 65, 45, 4, 2, 0),
    Product('Груша', 80, 57, 0, 1, 3),
    Product('Газированный напиток кола без кофеина', 59, 41, 0, 5, 0),
    Product('Винегрет', 120, 130, 1, 3, 2),
    Product('Горбуша', 205, 140, 60, 0, 0),
    Product('Агава сушеная', 200, 341, 0, 5, 16),
    Product('Торт Зебра', 200, 271, 107, 10, 2),
    Product('Леденцовая карамель', 150, 384, 0, 83, 0),
    Product('Биточки паровые из курицы', 180, 176, 33, 1, 1)
]
