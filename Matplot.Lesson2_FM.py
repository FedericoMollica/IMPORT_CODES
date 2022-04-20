#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 01:19:20 2022

@author: Federico

LEZIONE NUMERO 2 SUI GRAFICI 
GRAFICI A LINEA E SCATTER PLOT

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_Lessons_import/gas_prices.csv')

plt.figure(dpi = 300)

plt.title('Gas Prices over Time (in USD)', size= 20)
plt.xlabel('Years')
plt.ylabel('US Dollars')

"""
for country in gas:
    if country != 'Year':
     plt.plot(gas['Year'], gas[country], marker = '.')

#codice ciclo di for, per ogni paese in gas se il paese non si trova nella colonna anno
#allora plotta un grafico assex(anni), assey(paesi). marker di linea '.'
"""
#plt.savefig('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_Lessons_import/gas_prices.png', dpi = 300)


plt.plot(gas['Year'], gas['USA'], 'b.-', label = 'USA')
plt.plot(gas['Year'], gas['Canada'], 'r.-', label = 'Canada')
plt.plot(gas['Year'], gas['South Korea'], 'g.-', label = 'South Korea')
gas

plt.xticks(gas['Year'][::3])

"""
il codice ::'ci indica che gli anni verraano considerati a saltare, in questo caso a gruppi di 3. 
"""

plt.legend()

#plt.savefig('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_Lessons_import/gas_prices_3Countries.png', dpi = 300)

plt.show()

plt.figure(figsize = (20,15))
plt.scatter(list(range(len(df1['BIRTH DATE']))),df1["CT +2 date"], c = 'purple', s = 70, alpha = 0.6, label = 'CT+2 date')
plt.scatter(list(range(len(df1['BIRTH DATE']))),df1["CT +1 date"], c = 'darkblue', s = 70, alpha = 0.6, label = 'CT+1 date')
plt.scatter(list(range(len(df1['BIRTH DATE']))),df1["ASP IgE DATE +1"], c = 'black', marker = '*', s = 120, alpha = 0.6, label = 'ASP IgE DATE +1')
plt.scatter(list(range(len(df1['BIRTH DATE']))),df1["ASP IgG DATE +1"], c = 'orange', marker = '*', s = 120, alpha = 0.6, label = 'ASP IgG DATE +1')
plt.scatter(list(range(len(df1['BIRTH DATE']))),df1["1ST POSTITIVE ASP"], c = 'RED', s = 150, alpha = 0.6, label = '1ST POSITIVE ASP')
plt.scatter(list(range(len(df1['BIRTH DATE']))),df1["CT -1 date"], c = 'green', s = 70, alpha = 0.6, label = 'CT-1 date')
#plt.scatter(list(range(len(df1['BIRTH DATE']))),df1["CT -2 date"], c = 'DarkBlue', s = 70, alpha = 0.6, label = 'CT-2 date')
plt.scatter(list(range(len(df1['BIRTH DATE']))),df1["BIRTH DATE"], c = 'brown', s = 70, alpha = 0.8, label = 'Birth date')
plt.title('ASPECT PATIENTS', size = 20)
plt.legend() 
plt.xlabel('Patient', size = 20)
plt.ylabel('Year', size = 20)
plt.savefig('/content/drive/MyDrive/Python_Files/Python_Export/20220331_ASPECT_FULL_pos_cohort_graph.png', dpi = 200)
#con questo comando posso plottare in scatter (punti, altrimenti in linea). E' importante definire il range e settare i parametri del plot
