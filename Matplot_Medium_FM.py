"""

#XXXXX  LEZIONE NUMERO 2 SUI GRAFICI: LINEA, SCATTER PLOT, ISTOGRAMMA, TORTA E BOXES XXXXX

@author: Federico Mòllica

"""

# coding: utf-8

'''
#XXXXX  GRAFICO A LINEA  XXXXX
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_Lessons_import/gas_prices.csv')

plt.figure(dpi = 300)

plt.title('Gas Prices over Time (in USD)', size= 20)
plt.xlabel('Years')
plt.ylabel('US Dollars')


for country in gas:
    if country != 'Year':
     plt.plot(gas['Year'], gas[country], marker = '.')

#codice ciclo di for, per ogni paese in gas se il paese non si trova nella colonna anno
#allora plotta un grafico assex(anni), assey(paesi). marker di linea '.'
#plt.savefig('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_Lessons_import/gas_prices.png', dpi = 300)


plt.plot(gas['Year'], gas['USA'], 'b.-', label = 'USA')
plt.plot(gas['Year'], gas['Canada'], 'r.-', label = 'Canada')
plt.plot(gas['Year'], gas['South Korea'], 'g.-', label = 'South Korea')
gas

plt.xticks(gas['Year'][::3])
#il codice ::'ci indica che gli anni verraano considerati a saltare, in questo caso a gruppi di 3. 

plt.legend()

#plt.savefig('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_Lessons_import/gas_prices_3Countries.png', dpi = 300)

plt.show()


'''
#XXXXX COMPLEX SCATTER PLOT XXXXX 
''''


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


'''
#XXXX  ISTOGRAMMA  XXXX

#XXX USE THE COLOR PICKER ONLINE TO TAKE THE CODE OF THE COLORS XXX
'''

#LOAD FIFA DATA 

fifa = pd.read_csv('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_import/fifa_data.csv')
fifa.head(5)

plt.figure(dpi = 120)

bins = [40,50,60,70,80,90,100]
plt.hist(fifa["Overall"], color = "blue",  bins = bins)
plt.xticks(bins)
plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
plt.title('Distribution of Player Skills in FIFA 2018')

plt.savefig('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_export/Distribution_Player_Skills_FIFA.jpg', dpi = 70)

plt.show()


'''
#XXXX  GRAFICO A TORTA  XXXX
'''


plt.figure(dpi = 120)

left = fifa.loc[fifa["Preferred Foot"] == 'Left'].count()[0]
right = fifa.loc[fifa["Preferred Foot"] == "Right"].count()[0]

print(left)
print(right)

labels = ['Left', "Right"]
colors = ["#abcdef", "#aabbcc"]

plt.pie([left,right], labels = labels, colors = colors, autopct = '%.2f %%')
#codice per plottare un grafico a torta. importante determinare gli elementi da plottare.
#autopct è l'elemento da inserire per inserire le annotazioni in percentuale 
#il codice '%.2f' è per plottare i valori, se aggiungo '%%' plotta pure il simbolo % sui valori.

plt.title("Foot Preference of FIFA Players")

plt.savefig('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_export/Foot_Preference_FIFA_Players.jpg', dpi = 70)

plt.show()


fifa["Weight"].head(3)
#0    159lbs
#1    183lbs
#2    150lbs


fifa["Weight"] = [int(x.strip("lbs")) if type(x) == str else x for x in fifa["Weight"]]
#codice per eliminare la stringa "lbs" dagli elementi della colonna "Weight".
#il codice si legge "elimina (lbs) se l'elemento x corrisponde ad una stringa"
# "per ogni elemento x presente nella colonna "weight".

fifa["Weight"].head(3)
#0        159
#1        183
#2        150

plt.figure(dpi = 120)

light = fifa.loc[(fifa["Weight"] < 125)].count()[0]
light_medium = fifa.loc[(fifa["Weight"] >= 125) & (fifa["Weight"] < 150)].count()[0]
medium = fifa.loc[(fifa["Weight"] >= 150) & (fifa["Weight"] < 175)].count()[0]
medium_heavy = fifa.loc[(fifa["Weight"] >= 175) & (fifa["Weight"] < 200)].count()[0]
heavy = fifa[(fifa["Weight"] >= 200)].count()[0]

weights = [light, light_medium, medium , medium_heavy, heavy]
pesi = [['Under 125', '125-150', '150-175', 'Over 200']]
print(pesi)

plt.pie(weights, autopct = '%.2f %%', pctdistance = 0.9)
plt.title('Weight Distribution of FIFA Players (in lbs)')

plt.savefig('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_export/Weight_Distribution_FIFA_Players.jpg', dpi = 70)

plt.show()


'''
#XXXX  BOX PLOT  XXXX
'''


plt.figure(dpi= 120)

barcelona = fifa.loc[fifa["Club"] == "FC Barcelona"] ["Overall"]
madrid = fifa.loc[fifa["Club"] == "Real Madrid"] ["Overall"]
rev = fifa.loc[fifa["Club"] == "New England Revolution"] ["Overall"]

labels = ["FC Barcelona", "Real Madrid", "New England Revolution"]

boxes = plt.boxplot([barcelona, madrid, rev], labels =labels, patch_artist = True)
#codice base per plottare un grafico a scatola

for box in boxes["boxes"]:
    box.set(color = "blue", linewidth = 2)
    box.set(facecolor = "green")

plt.title("Professional Soccer Team Comparison")
plt.ylabel("FIFA Overall Rating")

plt.savefig('/Users/air/Desktop/PHD/Python/Python_Lessons_FM/Python_export/Professional_Soccer_Team.jpg', dpi = 70)

plt.show()
