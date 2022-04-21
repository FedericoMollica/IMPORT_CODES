# -*- coding: utf-8 -*-
"""PokemonPandas_Lesson.ipynb


"""

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/pokemon_data.csv')
df1 = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/pokemon_data_modified.csv')

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/pokemon_data.csv')
df1 = pd.read_csv('/content/drive/MyDrive/Python_Files/Python_Import/pokemon_data_modified.csv')

'''#XXXXXXX  LEZIONE PANDAS BASIC SU DATABASE POKEMON: COME LAVORARE SU UN DATAFRAME  XXXXXXXXXX '''

#PUOI SEMPRE AGGIUNG. PRINT() AL CODICE PER OTTENERE LE INFO CHE CERCHI. ALTRIMENTI OTTIENI IL DATAFRAME SOTTO FORMA DI TABELLA.

'''#XXXXX READ HEADERS XXXXX'''

df.columns
print(df.columns)


'''#XXXXX READ EACH OR MORE COLUMNS XXXXX'''

df[['Name', 'Type 1']]
print(df[['Name', 'Type 1']])
(df['Name'])
#codice per leggere o printare tutti gli elementi di specifiche colonne.

'''#XXXXX READ EACH ROW XXXXX'''

df.iloc[4]
print(df.iloc[4])
#codice per estrarre una determinata riga

df.loc[df['Type 1'] == 'Fire']
print(df.loc[df['Type 1'] == 'Fire'])
#con questo codice posso estrarre tutti gli elementi che presentano un emelemnto in una determinata colonna.

print(df.loc[df['Name'] == 'Umbreon']) 
#codice per cercare uno specifico elemnto nella mia tabella. In questo caso il pokemon con nome "umbreon".


'''#XXXXX READ MORE ROWS USING FOR CYCLES XXXXX'''

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


'''#XXXXX READ A SPECIFIC LOCATION (R,C) XXXXX'''

df.iloc[2,1]
print(df.iloc[2,1])
#Venusaur (risposta)

print(df.iloc[2,2])
#Grass (risposta)
#con questo codice possiamo cercare uno specifico elemento nel nostro df. All'interno delle par inseriamo [riga, colonna]


'''#XXXXX WORK ON COLUMNS XXXXX'''

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] +df ['Sp. Def'] + df['Speed']
#codice per creare una nuova colonna nel nostro df 'nuovo nome'. In questo caso la colonna creata è una somma di tutte le altre.

df = df.drop(columns = ['Total'])
#codice per eliminare una determiata colonna dal mio dataframe

df['Total'] = df.iloc[:, 4:10].sum(axis = 1)
#codice veloce per eseguire la creazione colonna con la somma si altre colonne del df. 
#il ':' indica tutte le righe, mentre gli elementi dopo la ',' sono le colonne
#in questo caso dalla 4a alla 9a perchè mettiamo i ':'.        
#axis 1 mi indica che la colonna verrà aggiunta verticalmente


'''#XXXXX SORTING A SPECIFIC DF'S COLUMN ELEMENTS FOR A SPECIFIC VALUE XXXXX'''

Speedest = df.sort_values('Speed', ascending = False)
#codice per sortare i dati di una colonna secondo un criterio

df.sort_values(['Type 1', 'Speed'], ascending = False).head(5)
#codice per sortare due colonne contemporaneamente


'''#XXXXXXX SECONDO CAPITOLO XXXXXX'''


'''#ESERCIZI SU DATABASE'''

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


'''#XXXXXXXX TERZO CAPITOLO XXXXXXXXXX'''

'''#AGGREGATE STATISTICS (GROUPBY)'''

df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False)
#codice per raggruppare gli elementi di una specifica colonna con la difesa media più alta, in questo caso, ordine discendente.

df.groupby(['Type 1']).count()
#comando per raggruppare un elemento di una colonna e contarne le volte che si ripete nel df.
#in questo caso mi conta quanti pkmn ci sono per specifico tipo 1.

df.groupby(['Type 1', 'Type 2']).count()
#comando per raggruppare elementi di colonne diverse e contarne quante volte si ripetono nel df.
#in questo caso ottengo la conta di tutti i pokemon divisi per tipo 1 e tipo 2.

df.groupby(['Type 1', 'Type 2']).count()

df

df1

print(df[['Name','Speed']])
#comando per selezionare solamente le colonne della mia tabella

print(df.iloc[6])
#comando per selezionare solamente una riga della mia tabella. Se avessi usato la "," avrei potuto selezionare più righe [2,1]

print(df.loc[df['Name'] == 'Umbreon']) 
#comando per cercare uno specifico elemnto nella mia tabella. In questo caso il pokemon con nome "umbreon".

Speedest = df.sort_values('Speed', ascending = False)
#comando per sortare i dati di una colonna secondo un criterio

df.sort_values(['Type 1', 'Speed'], ascending = False).head(5)
#comando per sortare due colonne contemporaneamente

Speedest

df.describe()
#comando per ottenere informazioni statistiche del mio dataframe

