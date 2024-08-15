import pandas as pd
import numpy as np

# создание датасета
dates = pd.date_range(start='2022-07-26', periods=10, freq='D')

# создание случайных значений
values = np.random.rand(10)  # 10 случайных значений

# создание датафрейма
df = pd.DataFrame({'dates': dates, 'values': values})
df.set_index('dates', inplace=True)
print(df)

# создание результирующего датафрейма
month = df.resample('ME').mean()  # ME - месяц

print(month)
