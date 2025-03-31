t = input().strip()  # Подстрока для поиска
s = input().strip()  # Базовая строка
n = int(input())  # Количество повторений

password = s * n  # Пароль как повторение s n раз
count = 0
len_t = len(t)

# Перебираем все возможные подстроки в password и сравниваем с t
for i in range(len(password) - len_t + 1):
    if password[i:i+len_t] == t:
        count += 1

print(count)  # Выводим количество вхождений