import matplotlib.pyplot as plt
import numpy as np
import random as rand
import pandas as pd

mesh1 = [rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100)]
pepe1 = pd.DataFrame({'x': mesh1}) # таблица индивидуальных значений
razmah = [abs(mesh1[0]-mesh1[1]), abs(mesh1[1]-mesh1[2]), abs(mesh1[2]-mesh1[3]), abs(mesh1[3]-mesh1[4]), abs(mesh1[4]-mesh1[5]), abs(mesh1[5]-mesh1[6]), abs(mesh1[6]-mesh1[7]), abs(mesh1[7]-mesh1[8]), abs(mesh1[8]-mesh1[9])]
pepe2 = pd.DataFrame({'x': razmah}) # таблица размахов

X = np.nanmean(pepe1.x) # средняя для Индивид. (nanmean её вычисляет)
R = np.nanmean(pepe2.x) # средняя для Размахов

UCL1 = X + 2.660 * R
LCL1 = X - 2.660 * R
UCL2 = 3.267 * R

print('индивидуальные значения ->', mesh1)

# скрыть ограничения графика

fig, ax = plt.subplots()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# средняя линия, границы

plt.axhline(y = X, color = 'red', linestyle = '--', label = 'среднее', linewidth = '1') # axhline добавляет гориз линию
plt.axhline(y = UCL1, color = 'red', linestyle = '--', label = 'верхняя', linewidth = '1')
plt.axhline(y = LCL1, color = 'red', linestyle = '--', label = 'нижняя', linewidth = '1')

# отображение графика индивид.

plt.plot(pepe1.x, marker = 'o')
plt.show()

# отображение графика размахов

print('индивидуальные значения ->', razmah)

fig, ax = plt.subplots()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.axhline(y = R, color = 'red', linestyle = '--', label = 'среднее', linewidth = '1')
plt.axhline(y = UCL2, color = 'red', linestyle = '--', label = 'верхняя', linewidth = '1')

plt.plot(pepe2.x, marker = 'o')
plt.show()