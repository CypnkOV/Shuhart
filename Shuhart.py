import matplotlib.pyplot as plt
import numpy as np
import random as rand
import pandas as pd

mesh1 = [rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100)]
pepe1 = pd.DataFrame({'x': mesh1})
razmah = [abs(mesh1[0]-mesh1[1]), abs(mesh1[1]-mesh1[2]), abs(mesh1[2]-mesh1[3]), abs(mesh1[3]-mesh1[4]), abs(mesh1[4]-mesh1[5]), abs(mesh1[5]-mesh1[6]), abs(mesh1[6]-mesh1[7]), abs(mesh1[7]-mesh1[8])]
pepe2 = pd.DataFrame({'x': razmah})

m = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
X = 0
R = 0
UCL1 = 0
LCL1 = 0
UCL2 = 0
u1 = 0
u11 = 0
U1 = 0
U11 = 0
l1 = 0
l11 = 0
L1 = 0
L11 = 0

while len(mesh1) != 10:
    X = np.nanmean(pepe1.x)  # средняя для Индивид. (nanmean её вычисляет)
    R = np.nanmean(pepe2.x)  # средняя для Размахов
    UCL1 = X + 2.660 * R
    LCL1 = X - 2.660 * R
    UCL2 = 3.267 * R
    u1 = 1 / 3 * (UCL1 - X)
    u11 = 2 / 3 * (UCL1 - X)
    U1 = UCL1 - u11
    U11 = UCL1 - u1
    l1 = 1 / 3 * (X - LCL1)
    l11 = 2 / 3 * (X - LCL1)
    L1 = X - l11
    L11 = X - l1
    m += 1
    if m > UCL1: # Первый критерий
        mesh1.insert(2, m)
        razmah.append(abs(mesh1[8]-mesh1[9]))

while len(mesh1) != 16:
    X = np.nanmean(pepe1.x)
    R = np.nanmean(pepe2.x)
    UCL1 = X + 2.660 * R
    LCL1 = X - 2.660 * R
    UCL2 = 3.267 * R
    u1 = 1 / 3 * (UCL1 - X)
    u11 = 2 / 3 * (UCL1 - X)
    U1 = UCL1 - u11
    U11 = UCL1 - u1
    l1 = 1 / 3 * (X - LCL1)
    l11 = 2 / 3 * (X - LCL1)
    L1 = X - l11
    L11 = X - l1
    a1 += 1
    if a1 > L1:
        mesh1.insert(6, a1)
        razmah.append(abs(mesh1[9] - mesh1[10]))
    if a2 < a1:
        a2 += 1
    else:
        mesh1.insert(7, a2)
        razmah.append(abs(mesh1[10] - mesh1[11]))
        #################################################### Дописать сюда

print(UCL1)
print('индивидуальные значения ->', mesh1)
print('индивидуальные значения ->', razmah)
pepe1 = pd.DataFrame({'x': mesh1}) # таблица индивидуальных значений
pepe2 = pd.DataFrame({'x': razmah}) # таблица размахов

# скрыть ограничения графика

ax = plt.gca()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['bottom'].set_position('center')
plt.xticks([])

# средняя линия, границы

plt.axhline(y = X, color = 'red', linestyle = '-.', label = 'среднее', linewidth = '1') # axhline добавляет гориз линию
plt.axhline(y = UCL1, color = 'red', linestyle = '--', label = 'верхняя', linewidth = '1')
plt.axhline(y = LCL1, color = 'red', linestyle = '--', label = 'нижняя', linewidth = '1')
plt.axhline(y = U1, color = 'red', linestyle = '--', linewidth = '1')
plt.axhline(y = U11, color = 'red', linestyle = '--', linewidth = '1')
plt.axhline(y = L1, color = 'red', linestyle = '--', linewidth = '1')
plt.axhline(y = L11, color = 'red', linestyle = '--', linewidth = '1')

# отображение графика индивид.

plt.plot(pepe1.x, marker = 'o')
plt.show()

# отображение графика размахов

fig, ax = plt.subplots()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.axhline(y = R, color = 'red', linestyle = '--', label = 'среднее', linewidth = '1')
plt.axhline(y = UCL2, color = 'red', linestyle = '--', label = 'верхняя', linewidth = '1')

plt.plot(pepe2.x, marker = 'o')
plt.show()