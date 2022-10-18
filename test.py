import matplotlib.pyplot as plt
import numpy as np
import random as rand
import pandas as pd

pepe = pd.DataFrame({'x': [rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100)]})

# скрыть ограничения графика

fig, ax = plt.subplots()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# средняя линия, границы

plt.axhline(y = np.nanmean(pepe.x), color = 'red', linestyle = '--', label = 'srednee') # axhline добавляет гориз линию, nanmean ёё вычисляет

# отображение графика

plt.plot(pepe.x, marker = 'o')
plt.show()
