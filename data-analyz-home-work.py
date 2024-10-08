import pandas as pd

# Пример данных
data = {
    'Ученик': ['Анна', 'Борис', 'Виктор', 'Диана', 'Маша', 'Федор', 'Евгений', 'Глеб', 'Иван', 'Юлия'],
    'Математика': [90, 85, 78, 92, 88, 76, 95, 89, 84, 91],
    'Физика': [85, 89, 82, 87, 90, 85, 88, 84, 80, 86],
    'Химия': [80, 78, 85, 92, 88, 91, 83, 87, 84, 86],
    'Литература': [88, 92, 84, 89, 87, 85, 86, 90, 91, 93],
    'История': [91, 88, 90, 85, 87, 89, 84, 86, 90, 92]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Цикл по всем предметам (столбцам, кроме столбца 'Ученик')
for column in df.columns[1:]:  # Пропускаем первый столбец с именами учеников
    q1 = df[column].quantile(0.25)  # Первый квартиль
    q3 = df[column].quantile(0.75)  # Третий квартиль
    iqr = q3 - q1  # Межквартильный размах

    print(f"Предмет: {column}")  # Название предмета
    print(f"Средний балл: {df[column].mean()}")  # Средний балл
    print(f"Медианный балл: {df[column].median()}")  # Медианный балл
    print(f"Q1 (Первый квартиль): {q1}")  # Первый квартиль
    print(f"Q3 (Третий квартиль): {q3}")  # Третий квартиль
    print(f"Межквартильный размах: {iqr}")  # Межквартильный размах
    print(f"Стандартное отклонение баллов: {df[column].std()}")  # Стандартное отклонение баллов
    print()  # Пустая строка для разделения выводов по предметам
