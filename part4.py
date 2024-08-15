import pandas as pd
import matplotlib.pyplot as plt

# создание датафрейма
data = {'value': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)

# print(df.describe())

# построение гистограммы
# df['value'].hist()

# отображение гистограммы
# plt.show()

# построение боксплота
df.boxplot(column='value')
plt.show()

# вычисление межквартильного размаха
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

# вычисление верхней и нижней границы
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

# создание нового датафрейма
df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]

df_new.boxplot(column='value')
plt.show()