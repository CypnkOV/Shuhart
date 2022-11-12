import matplotlib.pyplot as plt
from numpy import nanmean
from random import randint
import pandas as pd
import sys
import os
from tkinter import Tk, Label, Button
from tabulate import tabulate
from math import ceil
from math import floor

mesh1 = [randint(0, 50), randint(0, 100), randint(0, 1), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
pepe1 = pd.DataFrame({'x': mesh1})
razmah = []

def razschet():
    x = 0
    y = 1
    while x != len(mesh1) - 1:
        n = abs(mesh1[x]-mesh1[y])
        x += 1
        y += 1
        razmah.append(n)

razschet()
pepe2 = pd.DataFrame({'x': razmah})

x = n1 = n2 = m = a1 = X = R = UCL1 = LCL1 = UCL2 = u1 = u11 = U1 = U11 = l1 = l11 = L1 = L11 = LCL2 = 0

while len(mesh1) != 24 and n2 < 10:
    X = nanmean(pepe1.x)  # средняя для Индивид. (nanmean её вычисляет)
    R = nanmean(pepe2.x)  # средняя для Размахов
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
    if m < UCL1: #1 критерий
        m = randint(int(UCL1), int(UCL1) + 10)
        mesh1[2] = m
        razmah.clear()
        razschet()
        pepe1 = pd.DataFrame({'x': mesh1})
        pepe2 = pd.DataFrame({'x': razmah})
    if a1 > L1 and len(mesh1) != 15: #2 критерий
        a1 += randint(4, 10)
        mesh1.insert(6, a1)
        razmah.clear()
        razschet()
        pepe1 = pd.DataFrame({'x': mesh1})
        pepe2 = pd.DataFrame({'x': razmah})
    if len(mesh1) == 15: #3 критерий
        mesh1.append(0)
        mesh1.append(0)
        mesh1.append(0)
        mesh1.append(0)
        mesh1.append(0)
        mesh1.append(0)
        mesh1.append(0)
        mesh1.append(0)
        mesh1.append(0)
    for i in mesh1[15:24]:
        if i < L11:
            n1 = randint(ceil(L11), floor(X))
            mesh1.pop(23)
            mesh1.insert(15, n1)
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if i > X:
            n1 = randint(ceil(L11), floor(X))
            mesh1.pop(23)
            mesh1.insert(15, n1)
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})

pepe1 = pd.DataFrame({'x': mesh1}) # таблица индивидуальных значений
pepe2 = pd.DataFrame({'x': razmah}) # таблица размахов

#отображение таблицы в формате SQL

razmah.append(0)
X_sredn = ['']
X_sredn = X_sredn * 24
X_sredn[12] = round(X, 3)
R_sredn = ['']
R_sredn = R_sredn * 24
R_sredn[12] = round(R, 3)
UCL1_poz = ['']
UCL1_poz = UCL1_poz * 24
UCL1_poz[12] = round(UCL1, 3)
LCL1_poz = ['']
LCL1_poz = LCL1_poz * 24
LCL1_poz[12] = round(LCL1, 3)

df = pd.DataFrame({'Индивид. знач' : mesh1,
                   'Размахи' : razmah,
                   '\u0058\u0305': X_sredn,
                   '\u0052\u0305': R_sredn,
                   'UCL': UCL1_poz,
                   'LCL': LCL1_poz,
                   '№': list(range(1,25))})

df = df.set_index('№')
df['Размахи'] = df['Размахи'].shift(1)

print(tabulate(df, headers='keys', tablefmt='psql'))

# скрыть ограничения графика, подпись зон, подписать график

ax = plt.gca()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title("Критерии выявления особых причин на карте индивидуальных значений")
ax.set_xlabel('№ измерения') # подпись X
ax.set_ylabel('Индивид. значения') # подпись Y
y_values = [UCL1, X, LCL1]
labels = ["UCL", '\u0058\u0305', "LCL"]
ax.text(-1, (X + L11) / 2, 'C', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (X + U1) / 2, 'C', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (U1 + U11) / 2, 'B', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (L1 + L11) / 2, 'B', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (U11 + UCL1) / 2, 'A', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (L1 + LCL1) / 2, 'A', horizontalalignment='left', color='black', fontsize=20)
plt.yticks()
plt.yticks(y_values, labels)
plt.xticks(list(range(0, 24)), list(range(1, 25)))

# средняя линия, границы индивид. значений

plt.axhline(y = X, color = 'black', linestyle = '-.', label = 'среднее', linewidth = '1') # axhline добавляет гориз линию
plt.axhline(y = UCL1, color = 'black', linestyle = '--', label = 'верхняя', linewidth = '1')
plt.axhline(y = LCL1, color = 'black', linestyle = '--', label = 'нижняя', linewidth = '1')
plt.axhline(y = U1, color = 'black', linestyle = '--', linewidth = '1')
plt.axhline(y = U11, color = 'black', linestyle = '--', linewidth = '1') # 2 по счету линия
plt.axhline(y = L1, color = 'black', linestyle = '--', linewidth = '1')
plt.axhline(y = L11, color = 'black', linestyle = '--', linewidth = '1') # 5 по счету линия
plt.axvline(x = 1.5, color = 'r', linestyle = '--', linewidth = '1') # вертикальные линии
plt.axvline(x = 2.5, color = 'r', linestyle = '--', linewidth = '1')
plt.axvline(x = 5.5, color = 'r', linestyle = '--', linewidth = '1')
plt.axvline(x = 11.5, color = 'r', linestyle = '--', linewidth = '1')
plt.axvline(x = 14.5, color = 'r', linestyle = '--', linewidth = '1')
plt.axvline(x = 24, color = 'r', linestyle = '--', linewidth = '1')

# отображение графика индивид.

plt.plot(pepe1.x, marker = 'o')
plt.show()

# отображение графика размахов

fig, ax = plt.subplots()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_title("Критерии выявления особых причин на карте размахов")
ax.set_xlabel('№ измерения') # подпись X
ax.set_ylabel('Размахи') # подпись Y
y_values = [UCL2, X, LCL2]
plt.axhline(y = R, color = 'black', linestyle = '--', label = 'среднее', linewidth = '1')
plt.axhline(y = UCL2, color = 'black', linestyle = '--', label = 'верхняя', linewidth = '1')

plt.plot(pepe2.x, marker = 'o')
plt.show()

# перезапуск
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
clear = lambda: os.system('cls')

root = Tk()

Label(root, text="Перезапустить?").pack()
Button(root, text="Restart", command=restart_program).pack()
clear()
root.mainloop()