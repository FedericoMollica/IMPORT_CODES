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

    
