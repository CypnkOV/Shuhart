import matplotlib.pyplot as plt
import numpy as np
import random as rand
import pandas as pd
import sys
import os
from tkinter import Tk, Label, Button
from tabulate import tabulate

mesh1 = [rand.randint(0, 50), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100), rand.randint(0, 100)]
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

x = 0
n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = -98989
m = 0
a1 = 0
a2 = 0
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

# 1 критерий

while len(mesh1) != 9:
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
    if m > UCL1:
        mesh1.insert(2, m)
        razmah.clear()
        razschet()
        pepe1 = pd.DataFrame({'x': mesh1})
        pepe2 = pd.DataFrame({'x': razmah})

# 2 критерий

while len(mesh1) != 15:
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
    a1 += rand.randint(4, 10)
    if a1 > L1:
        mesh1.insert(6, a1)
        razmah.clear()
        razschet()
        pepe1 = pd.DataFrame({'x': mesh1})
        pepe2 = pd.DataFrame({'x': razmah})

# 3 критерий

while len(mesh1) != 24:
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
    while x != 5:
        x += 1
        if mesh1[1] > UCL1:
            mesh1[1] = int(UCL1 - 50)
        if mesh1[3] > UCL1:
            mesh1[3] = int(UCL1 - 75)
        if mesh1[12] > UCL1:
            mesh1[12] = int(UCL1 - 50)
        if mesh1[13] > UCL1:
            mesh1[13] = int(UCL1 - 50)
        if mesh1[14] > UCL1:
            mesh1[14] = int(UCL1 - 50)
        if m < UCL1:
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
            m = int(UCL1 + 25)
            if m > UCL1:
                mesh1.pop(2)
                mesh1.insert(2, m)
                razmah.clear()
                razschet()
                pepe1 = pd.DataFrame({'x': mesh1})
                pepe2 = pd.DataFrame({'x': razmah})
        if len(mesh1) != 24:
            mesh1.append(0)
            mesh1.append(0)
            mesh1.append(0)
            mesh1.append(0)
            mesh1.append(0)
            mesh1.append(0)
            mesh1.append(0)
            mesh1.append(0)
            mesh1.append(0)
        if n1 < L11:
            n1 = rand.randint(int(L11), int(X))
            mesh1[15] = n1
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n2 < L11:
            n2 = rand.randint(int(L11), int(X))
            mesh1[16] = n2
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n3 < L11:
            n3 = rand.randint(int(L11), int(X))
            mesh1[17] = n3
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n4 < L11:
            n4 = rand.randint(int(L11), int(X))
            mesh1[18] = n4
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n5 < L11:
            n5 = rand.randint(int(L11), int(X))
            mesh1[19] = n5
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n6 < L11:
            n6 = rand.randint(int(L11), int(X))
            mesh1[20] = n6
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n7 < L11:
            n7 = rand.randint(int(L11), int(X))
            mesh1[21] = n7
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n8 < L11:
            n8 = rand.randint(int(L11), int(X))
            mesh1[22] = n8
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n9 < L11:
            n9 = rand.randint(int(L11), int(X))
            mesh1[23] = n9
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n1 > X:
            n1 = rand.randint(int(L11), int(X))
            mesh1[15] = n1
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n2 > X:
            n2 = rand.randint(int(L11), int(X))
            mesh1[16] = n2
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n3 > X:
            n3 = rand.randint(int(L11), int(X))
            mesh1[17] = n3
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n4 > X:
            n4 = rand.randint(int(L11), int(X))
            mesh1[18] = n4
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n5 > X:
            n5 = rand.randint(int(L11), int(X))
            mesh1[19] = n5
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n6 > X:
            n6 = rand.randint(int(L11), int(X))
            mesh1[20] = n6
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n7 > X:
            n7 = rand.randint(int(L11), int(X))
            mesh1[21] = n7
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n8 > X:
            n8 = rand.randint(int(L11), int(X))
            mesh1[22] = n8
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
            razmah.clear()
            razschet()
            pepe1 = pd.DataFrame({'x': mesh1})
            pepe2 = pd.DataFrame({'x': razmah})
        if n9 > X:
            n9 = rand.randint(int(L11), int(X))
            mesh1[23] = n9
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
                   'LCL': LCL1_poz})

df['Размахи'] = df['Размахи'].shift(1)

print(tabulate(df, headers='keys', tablefmt='psql'))

# скрыть ограничения графика, подпись зон

ax = plt.gca()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['bottom'].set_position('center')
ax.set_title("Критерии выявления особых причин")
y_values = [UCL1, X, LCL1]
labels = ["UCL", '\u0058\u0305', "LCL"]
ax.text(-1, (X + L11) / 2, 'C', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (X + U1) / 2, 'C', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (U1 + U11) / 2, 'B', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (L1 + L11) / 2, 'B', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (U11 + UCL1) / 2, 'A', horizontalalignment='left', color='black', fontsize=20)
ax.text(-1, (L1 + LCL1) / 2, 'A', horizontalalignment='left', color='black', fontsize=20)
plt.yticks(y_values, labels)
plt.xticks([])

# средняя линия, границы

plt.axhline(y = X, color = 'black', linestyle = '-.', label = 'среднее', linewidth = '1') # axhline добавляет гориз линию
plt.axhline(y = UCL1, color = 'black', linestyle = '--', label = 'верхняя', linewidth = '1')
plt.axhline(y = LCL1, color = 'black', linestyle = '--', label = 'нижняя', linewidth = '1')
plt.axhline(y = U1, color = 'black', linestyle = '--', linewidth = '1')
plt.axhline(y = U11, color = 'black', linestyle = '--', linewidth = '1') # 2 по счету линия
plt.axhline(y = L1, color = 'black', linestyle = '--', linewidth = '1')
plt.axhline(y = L11, color = 'black', linestyle = '--', linewidth = '1') # 5 по счету линия
plt.axvline(x = 3.5, color = 'r', linestyle = '--', linewidth = '1')# вертикальная линия
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

plt.axhline(y = R, color = 'red', linestyle = '--', label = 'среднее', linewidth = '1')
plt.axhline(y = UCL2, color = 'red', linestyle = '--', label = 'верхняя', linewidth = '1')

plt.plot(pepe2.x, marker = 'o')
plt.show()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
clear = lambda: os.system('cls')

root = Tk()

Label(root, text="Перезапустить?").pack()
Button(root, text="Restart", command=restart_program).pack()
clear()
root.mainloop()