n = int(input())
attacks = input().strip()  # Строка атак (A, B, C)

# Счётчики для каждого типа атак
count_a = 0
count_b = 0
count_c = 0

# Счётчики неприятных моментов для каждого типа
unpleasant_a = 0
unpleasant_b = 0
unpleasant_c = 0

for attack in attacks:
    # Обновляем счётчики текущих атак
    if attack == 'A':
        count_a += 1
    elif attack == 'B':
        count_b += 1
    elif attack == 'C':
        count_c += 1
    
    # Определяем текущий максимальный счётчик
    max_count = max(count_a, count_b, count_c)
    
    # Увеличиваем неприятные моменты для лидирующих типов
    if count_a == max_count:
        unpleasant_a += 1
    if count_b == max_count:
        unpleasant_b += 1
    if count_c == max_count:
        unpleasant_c += 1

# Выводим максимальное количество неприятных моментов
max_unpleasant = max(unpleasant_a, unpleasant_b, unpleasant_c)
print(max_unpleasant)