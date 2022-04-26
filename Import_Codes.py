# -*- coding: utf-8 -*-
"""
NOTEBOOK CONTENENTE I PRINCIPALI CODICI PER LAVORARE SUI DATAFRAME

"""

'''
#XXXXXX     CODICI PER IMPORTARE LE LIBRERIE PRINCIPALI DI PYTHON      XXXXXXXXX
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'
plt.rcParams.update({'font.size': 10, 'font.style': 'normal', 'font.family':'serif'})
from google.colab import files
import datetime as dt

'''
#XXXXXX    IMPORTARE ED ESPORTARE FILES SU PYTHON   XXXXXX
'''

from google.colab import drive
drive.mount('/content/drive')
#codice per montare google drive.

df = pd.read_excel('/content/drive/MyDrive/Python_Files/Python_Import/Python_CTs_FM.xlsx', header = [0])
#comando per salvare il data frame in formato csv per excel. Il file viene salvato in automatico su google drive.
#mettere read_xslx per aprire excel
#aggiungere sheet_name = 'nome del foglio', per aprire uno specifico foglio del documento.

df2.to_excel('/content/drive/MyDrive/Python_Files/Python_Export/20220318_LA_ASPECT_CT_list.xlsx')
#comando per salvare il data frame in formato csv per excel. Il file viene salvato in automatico su google drive.
#mettereto_excel per salvare in excel

'''
#XXXXXX    CODICI PER MODIFICARE IL DATAFRAME     XXXXXXXXX

#XXX  RIGHE XXX
'''

df.iloc[4]
print(df.iloc[4])
#codice per estrarre una determinata riga

df.drop([0, 1])
#comando per eliminare righe usando un indice

df = df.drop([0])
#comando per eliminare righe usando un indice, settare il nuovo df 

'''
#XXXXX READ MORE ROWS USING FOR CYCLES XXXXX
'''

for index, row in df.iterrows():
  print(index, row)
#in questo modo sto chiedento di printare tutti gli indici per ogni riga

for index, row in df.iterrows():
  print(index, row['Name'])
#in questa variante chiedo solo indice ,nr del pokedex, e nome

for index, row in df.iterrows():
  print(row['Name'])
#così chiedo solo di printare l'elemento della colonna 'Name' per ogni riga

for index, row in df.iterrows():
  print(index, row[['Name', 'Speed']])
#combinando le opzioni posso chiedere di printare l'elemento,pokemon, con numero pokedex, nome e velocità per ogni riga.

'''
#XXX  COLONNE  XXX
'''

df1 = df1.rename(columns = {'Hix number\n':'ciao'})
#comando per rinominare una specifica colonna su pandas

df1 = df1.sort_values('BIRTH DATE')
#comando per sortare tutto il dataframe! rispetto ad una colonna

print(df.loc[df['Name'] == 'Umbreon']) 
#codice per cercare uno specifico eleme in una specifica colonna del DF. In questo caso il pokemon con nome "umbreon".

df1 = df1.drop(['CT-2 ID','CT -2 date'], 1)
#comando per eliminare una o piu colonne da una tabella df

df = df.drop(columns = ['Total'])
#codice per eliminare una determiata colonna dal mio dataframe

df['Total'] = df.iloc[:, 4:10].sum(axis = 1)
#codice veloce per eseguire la creazione colonna con la somma si altre colonne del df. 
#il ':' indica tutte le righe, mentre gli elementi dopo la ',' sono le colonne
#in questo caso dalla 4a alla 9a perchè mettiamo i ':'.        
#axis 1 mi indica che la colonna verrà aggiunta verticalmente

df2 = df1[df1['CT -1 date']!='99/99/9999']
#comando per eliminare una stringa dalla tabella in riferimento ad una determinata colonna

'''
#XXXXX SORTING A SPECIFIC DF'S COLUMN ELEMENTS FOR A SPECIFIC VALUE XXXXX
'''

Speedest = df.sort_values('Speed', ascending = False)
#codice per sortare i dati di una colonna secondo un criterio

df.sort_values(['Type 1', 'Speed'], ascending = False).head(5)
#codice per sortare due colonne contemporaneamente

'''
#XXXXXX   CODICI PER MODIFICARE IL FORMATO DATA TEMPO   XXXXXXX
'''

df1['CT -2 date'] =  pd.to_datetime(df1['CT -2 date'], format='%d/%m/%Y')
#formula per convertire le date in formato stringa in formato data.

df4['CT -1 date'] =  pd.to_datetime(df4['CT -1 date'])
#formula per convertire le date in formato stringa in formato data.

df1["CT DATE"] = pd.to_datetime(df1["CT DATE"]).dt.strftime('%Y')
#comando per cambiare o impostare un diverso formato data tempo ('%Y-%m-%d'). Non compatibile con str, necessaria conversione.

df1['nb_months CT-2'] = round((df1["CT -2 date"] - df1["BIRTH DATE"])/np.timedelta64(1, 'M'),0)
#comando per calcolare la differenza di età tra due colonne espressa in mesi ed arrotondata a due decimali. Per arrotondare inserisco il
#comando round seguito alla fine dalla virgola e dal numero di decimali che voglio ottenere.

def to_int(stringa): # con def definisci le funzioni, la cosa tra parentesi è l'input
    return int(stringa) #ti ritorna il cast ad intero
    # apply applica una funzione ad ogni elemento della colonna
#creo una funzione che trasforma una stringa in intero

df1["CT -2 date"] = df1["CT -2 date"].apply( to_int)
df1["1ST POSTITIVE ASP"] = df1["1ST POSTITIVE ASP"].apply( to_int) # apply applica la funzione a tutti gli elementi
df1['nr_years CT -2'] = df1["1ST POSTITIVE ASP"] - df1["CT -2 date"]
#comando per calcolare la differenza di età tra due colonne espressa in mesi ed arrotondata a due decimali. Per arrotondare inserisco il
#comando round seguito alla fine dalla virgola e dal numero di decimali che voglio ottenere.

'''
#XXXXXX   CODICI PER LAVORARE SU PIU DATAFRAME CONTEMPORANEAMENTE  XXXXXXX
'''

df2 = pd.merge(df, df1, on = 'ciao')
#comando per fare merge di un df su un altro ottenendo solo le linee in comune

df4 = df[~df['CT Date'].isin(df2['CT Date'])]
#codice per eliminare tutti gli elementi di una specifica colonna di un df presenti in un altro df. Opposto di merge.

'''
#XXXXX   CODICI PER OTTENERE INFO DAL DF  XXXXX
'''

df.describe()
#comando per ottenere informazioni statistiche del mio dataframe

'''
#XXXXX READ A SPECIFIC LOCATION (R,C) XXXXX
'''

df.iloc[2,1]
print(df.iloc[2,1])
#Venusaur (risposta)

print(df.iloc[2,2])
#Grass (risposta)
#con questo codice possiamo cercare uno specifico elemento nel nostro df. All'interno delle par. inseriamo [riga, colonna]

df.loc[(df['Type 1'] == 'Grass')]
#solo tipi erba

df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
#solo tipi erba e veleno doppio tipo '&'. Se avessi voluto entrambi erba o veleno avrei potuto usare '|'  

df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') &(df['HP'] >70)]
#solo tipi erba e veleno con hp superiori a 70 punti.

df.loc[df['Name'].str.contains('Pi')]
#codice per localizzare nel database tutti gli elementi che contengono ('elementi str') esempio ('Pi') nella loro str.

df.loc[~df['Name'].str.contains('Pi')]
#inserendo '~' effettuiamo il reverse. otteniamo gli elementi che non contengono la parte della stringa tra gli elementi str.

df.loc[~df['Name'].str.contains('^Pi')]
#aggiungendo '^' ricerchiamo espressamenti gli elementi che iniziano con quella parte di str.

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flame'
#codice per rinominare gli elementi di una colonna in base ad una condizione.
#in questo caso tutti i pkmn con tipo 1 fuoco sono stati rinominati tipo 'Flame'.

df.loc[df['HP'] > 70, ['Generation' , 'Legendary']] = ['Test 1', 'Test 2']
#codice per rinominare gli elementi delle specifiche colonne che soddisfano la condizione.

df.loc[df['Name'].str.contains('saur'), ['Name']] = 'Test 3'
#codice per rinominare gli elementi delle specifiche colonne che contengono elementi della str selezionati.

'''
#XXXXXX AGGREGATE STATISTICS (GROUPBY) XXXXX
'''

df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False)
#codice per raggruppare gli elementi di una specifica colonna con la difesa media più alta, in questo caso, ordine discendente.

df.groupby(['Type 1']).count()
#comando per raggruppare un elemento di una colonna e contarne le volte che si ripete nel df.
#in questo caso mi conta quanti pkmn ci sono per specifico tipo 1.

df.groupby(['Type 1', 'Type 2']).count()
#comando per raggruppare elementi di colonne diverse e contarne quante volte si ripetono nel df.
#in questo caso ottengo la conta di tutti i pokemon divisi per tipo 1 e tipo 2.

