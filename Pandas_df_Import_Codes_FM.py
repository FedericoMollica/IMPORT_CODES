"""

XXXXXXXX    NOTEBOOK CONTENENTE I PRINCIPALI CODICI PER LAVORARE SU DATASET   XXXXXXXX

author: Federico Mòllica

"""

# -*- coding: utf-8 -*-


'''
#XXXXXX     CODICI PER IMPORTARE LE LIBRERIE PRINCIPALI DI PYTHON      XXXXXXXXX
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import string
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'
plt.rcParams.update({'font.size': 10, 'font.style': 'normal', 'font.family':'serif'})

'''
#XXX GOOGLE COLAB XXX
'''

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
#aggiungere, sheet_name = 'nome del foglio', per aprire uno specifico foglio del documento.
#aggiungere, index_col = 'nome colonna' per impostare una specifica colonna come indice del df

df2.to_excel('/content/drive/MyDrive/Python_Files/Python_Export/20220318_LA_ASPECT_CT_list.xlsx')
#comando per salvare il data frame in formato csv per excel. Il file viene salvato in automatico su google drive.
#mettereto_excel per salvare in excel

'''
UNIRE PIU' EXCEL IN UN UNICO FOGLIO (excel):
Cliccare su Data -> New query -> From File -> From Folder
Add the directory path -> Combine -> Combine & Load
'''

'''
#XXXXXX    LISTE   XXXXX

'''

a = [0, 1 ,2]
b = [0 , 1, 'hello']
#codice base per creare una lista. Posso inserire sia numeri che stringhe

emp_str_1 = 'John-Doe-70000'
#if we want to extract info from a string we can split it and add it into our class
first, last, pay = emp_str_1.split('-')
#codice per dividere le parole di una stringa usando uno specifico carattere
print(first)
#result: 
#John

alphabet_string = string.ascii_lowercase
letters = list(alphabet_string) 
#codice per ottenere tutte le lettere dell'alfabeto
#import string fondamentale.
print(letters)
#result:
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
#'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
#'s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a.append(1)
a.append('bye')
#codice per aggiungere un elemento alla mia lista

a = [13, 12, 'hello']
a.remove('hello')
#codice per eliminare un elemento dalla mia lista

a.pop(2)
#codice per eliminare un elemento dalla mia lista corrispondente all'indice


'''
#XXXXXX    CODICI PER MODIFICARE IL DATAFRAME     XXXXXXXXX


#XXX RIEMPIRE LE CELLE VUOTE XXX
'''

df.fillna('', inplace=True)
#codice per riempire automaticamente tutte le celle vuote del mio df

df.dropna(inplace=True)
#codice per eliminare tutte le celle contenenti valori nulli

'''
#XXX RIGHE XXX
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

df2 = (df1.merge(df, on= ['local id', 'Visit'], how='outer', indicator=True).query('_merge != "both"').drop(columns='_merge'))
#opposto di merge per tenere solo gli elementi non in comune usando piu colonne di due diversi df

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

range(len(s)-3)
#codice 'range(len(lista x))' mi consente di selezionare un elemento in posizione 0 ed altri indici 
#della mia specifica lista (0, 1 al contrario -1, -2, ecc)

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
#XXXXXX AGGREGATE STATISTICS (GROUPBY) XXXXXX
'''

df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False)
#codice per raggruppare gli elementi di una specifica colonna con la difesa media più alta, in questo caso, ordine discendente.

df.groupby(['Type 1']).count()
#comando per raggruppare un elemento di una colonna e contarne le volte che si ripete nel df.
#in questo caso mi conta quanti pkmn ci sono per specifico tipo 1.

df.groupby(['Type 1', 'Type 2']).count()
#comando per raggruppare elementi di colonne diverse e contarne quante volte si ripetono nel df.
#in questo caso ottengo la conta di tutti i pokemon divisi per tipo 1 e tipo 2.

'''
#XXXXXX LOOP E LOGICA FONDAMENTALI XXXXXX
'''


'''
#XXX COUNTING LOOP XXX
'''

#Codice loop base per contare gli eventi o elementi.
a = ['a','a','b', 'c','a','a']

def count(name, letter):
  count = 0
  for letter in name:
     count += 1
  return count 

count(a, 'a')
#result:
#6

count('mucca', 'a')
#result:
#5

#codice per contare le ripetizioni di uno specifico elemento in lista
a = ['a','a','b', 'c','a','a']

def count(name, letter):
  count = 0
  for l in name:
    if l == letter:
     count += 1
  return count 
 
count(a, 'a')
#result:
#4

count('mucca', 'a')
#result:
#1

#codice per contare e printare gli elementi unici in una lista o stringa in due diversi output. 
a = ['a','a','b', 'c','a','a']

def count_different_letters(name):
  unique_el_list = []
  for l in name:
    if l not in unique_el_list:
     unique_el_list.append(l)
  print(len(unique_el_list), unique_el_list)
  return len(unique_el_list), unique_el_list
 
numero, elementi = count_different_letters('ccane_%')
#result:
#6 ['c', 'a', 'n', 'e', '_', '%']

numero
#result:
#6

elementi
#result:
#['c', 'a', 'n', 'e', '_', '%']

#codice veloce per contare e printare gli elementi unici di una lista o stringa.
a = ['a','a','b', 'c','a','a']

def count_different_letters(name):
  return len(set(name)), list(set(name))
#result:
#(3, ['b', 'a', 'c'])

