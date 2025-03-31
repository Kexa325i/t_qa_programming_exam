import sys

def main():
    input = sys.stdin
    n, q = map(int, input.readline().split())  # Размер сетки и количество запросов
    grid = []
    # Читаем сетку
    for _ in range(n):
        line = input.readline().strip()
        grid.append(list(line))
    
    changes = []
    # Читаем координаты изменяемых клеток (переведены в 0-based)
    for _ in range(q):
        x, y = map(int, input.readline().split())
        changes.append((x-1, y-1))

    half = n // 2
    group_counts = [[0]*half for _ in range(half)]  # Счётчики для симметричных групп
    
    # Заполняем счётчики для каждой группы
    for x in range(n):
        for y in range(n):
            i = min(x, n-1-x)  # Группа по оси X
            j = min(y, n-1-y)  # Группа по оси Y
            if i >= half or j >= half:
                continue
            if grid[x][y] == '#':
                group_counts[i][j] += 1
    
    # Вычисляем начальное суммарное минимальное количество изменений
    total = 0
    for i in range(half):
        for j in range(half):
            cnt = group_counts[i][j]
            total += min(cnt, 4 - cnt)  # Минимум между текущим и необходимым
    
    print(total)  # Начальный результат
    
    # Обрабатываем запросы
    for x, y in changes:
        i = min(x, n-1-x)
        j = min(y, n-1-y)
        
        prev_cnt = group_counts[i][j]
        
        # Меняем цвет клетки и обновляем счётчик группы
        if grid[x][y] == '#':
            group_counts[i][j] -= 1
            grid[x][y] = '.'
        else:
            group_counts[i][j] += 1
            grid[x][y] = '#'
        
        # Пересчитываем вклад группы в общий результат
        new_cnt = group_counts[i][j]
        prev_contrib = min(prev_cnt, 4 - prev_cnt)
        new_contrib = min(new_cnt, 4 - new_cnt)
        total = total - prev_contrib + new_contrib
        
        print(total)  # Выводим обновлённый результат

if __name__ == "__main__":
    main()