s = input().strip()  # Получаем входную строку без пробелов

# Проверяем, является ли строка одним из ключевых слов "quality" или "security"
if s == "quality" or s == "security":
    print("YES")
else:
    print("NO")