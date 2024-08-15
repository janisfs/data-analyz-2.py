import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

# создание датафрейма
df = pd.DataFrame(data)

# преобразование типа данных
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

# вывод категорий
# print(df['gender'].cat.categories)
# print(df['department'].cat.categories)

# преобразование категорий
# df['gender'] = df['gender'].cat.codes
# df['department'] = df['department'].cat.codes

# вывод кодов
# print(df['gender'].cat.codes)
# print(df['department'].cat.codes)

# добавление категорий
df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

# удаление категорий
df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)

print(df)
