n = int(input())  # Количество ресторанов
restaurants = []

# Считываем координаты всех ресторанов
for _ in range(n):
    x, y = map(int, input().split())
    restaurants.append((x, y))

max_distance_sq = 0  # Максимальный квадрат расстояния между парой ресторанов

# Перебираем все пары ресторанов для поиска максимального расстояния
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = restaurants[i]
        x2, y2 = restaurants[j]
        distance_sq = (x2 - x1)**2 + (y2 - y1)**2  # Квадрат расстояния для оптимизации вычислений
        if distance_sq > max_distance_sq:
            max_distance_sq = distance_sq

print(max_distance_sq)  # Выводим результат