import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())  # Длина последовательности
    a = list(map(int, sys.stdin.readline().split()))  # Входной массив
    
    freq = defaultdict(int)  # Частота элементов в массиве
    present = [0] * (n + 1)  # Отметка наличия чисел 0..n
    
    # Заполняем частоты и отмечаем присутствующие числа
    for num in a:
        freq[num] += 1
        if num <= n:
            present[num] = 1
    
    # Вычисляем префиксную сумму отсутствующих чисел
    missing_prefix = [0] * (n + 1)
    missing_prefix[0] = 0 if present[0] else 1
    for i in range(1, n + 1):
        missing_prefix[i] = missing_prefix[i-1] + (0 if present[i] else 1)
    
    res = []
    # Для каждого x вычисляем минимальное требуемое количество операций
    for x in range(n + 1):
        if x == 0:
            res.append(freq.get(0, 0))
        else:
            required_missing = missing_prefix[x-1] if x-1 <= n else 0
            count_x = freq.get(x, 0)
            ans = max(required_missing, count_x)  # Выбираем максимум из требуемых отсутствующих и текущей частоты
            res.append(ans)
    
    # Выводим результат
    for num in res:
        print(num)

if __name__ == "__main__":
    main()