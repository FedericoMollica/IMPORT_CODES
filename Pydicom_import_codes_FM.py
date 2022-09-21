'''
PYDICOM_import_codes_FM Notebook

https://pydicom.github.io/
#pydicom documentation

pip install pydicom
python -m pip install pydicom
#codici per installare pydicom

import pydicom
pydicom.__version__
#codice per verificare la versione di pydicom
#result:
#2.3.0
'''

from pydicom import dcmread
from dicom_csv import join_tree
import pandas as pd
import os
from datetime import date

today = date.today()
dt = today.strftime('%Y%m%d')
#code to set the date of today in a format YYMMDD

ds = dcmread('/content/drive/MyDrive/Python_Files/Python_Import/CT_small.dcm')
print(ds)
#codice per caricare il file dicom e leggere i tag

df = join_tree('C:/Users/048252/Downloads/ASPEN FEDERICO CT TEMP/', relative=False, verbose=1)
df.to_excel('/content/drive/MyDrive/Python_Files/Python_Export/DICOM_TEST.xlsx')

df = join_tree("/Users/048252/Downloads/ASPEN_TEST", relative=False, verbose=1)
#df = join_tree("ADD FOLDER PATH", relative=False, verbose=1)
df = df.drop_duplicates(subset = ['SeriesInstanceUID'], keep= 'first')
#codes to extract all the dicom info and keep only the unique series id

df.to_excel('/Users/048252/Downloads/' + dt + '_DICOM_TAG_ANALYSIS_FM.xlsx')
#df.to_excel('ADD FOLDER PATH' + dt + '_DICOM_TAG_ANALYSIS_FM.xlsx')
#code to save the info as excel file:
#date of today + '_DICOM_TAG_ANALYSIS_FM.xlsx'
