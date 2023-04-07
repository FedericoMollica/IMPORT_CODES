'''
RENAMING DIRECTORY FILES USING A DF LIST 

'''

import os
import random
import pandas as pd

os.chdir('/Users/air/Downloads/Resize_png')
file_list = os.listdir('/Users/air/Downloads/Resize_png')
file_list.sort(reverse=False)
file_list.pop(0)
df = pd.read_excel('/Users/air/Downloads/pokedex_data_FM.xlsx', header = 0)

Name = []
p = 0

for i in df['Name']:
    Name.append(i)
    
for f in file_list:
    p += 1
    if p <= 250: 
        if p != Name:
            os.rename(f, Name[p] + '.png')

    
    
#RENAMING A LIST OF FOLDERS USING A AN EXCEL COLUMN
    
import os
import random
import pandas as pd

os.chdir(r'D:\Federico_Local_BUP\PCD_2023_test')
file_list = os.listdir(r'D:\Federico_Local_BUP\PCD_2023_test')
file_list.sort(reverse=False)
#file_list.pop(0)
df = pd.read_excel(r'C:\Users\048252\Downloads\folder_names.xlsx', header = 0)

Name = []
p = -1

for i in df['A1']:
    Name.append(i)
    
for f in file_list:
    p += 1
    if p <= 5: 
        if p != Name:
            os.rename(f, Name[p])
