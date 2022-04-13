#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 01:19:20 2022

@author: Federico
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