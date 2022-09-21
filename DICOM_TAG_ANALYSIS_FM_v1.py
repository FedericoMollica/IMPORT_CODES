
#AUTHOR: FEDERICO MOLLICA 2022
#SCRIPT: DICOM_TAG_ANALYSIS_FM_v1

#DESCRIPTION: 
#code to obtain an excel file containing all the dicom info from
#all the CTs present in one folder

#PROS:
#the file will be auto saved:'date of today' +'_DICOM_TAG_ANALYSIS_FM.xlsx'

from pydicom import dcmread
from dicom_csv import join_tree
import pandas as pd
import os
from datetime import date

today = date.today()
dt = today.strftime('%Y%m%d')
#code to set the date of today in a format YYMMDD

df = join_tree("/Users/048252/Downloads/ASPEN_TEST", relative=False, verbose=1)
#df = join_tree("ADD FOLDER PATH", relative=False, verbose=1)
df = df.drop_duplicates(subset = ['SeriesInstanceUID'], keep= 'first')
#codes to extract all the dicom info and keep only the unique series id

df.to_excel('/Users/048252/Downloads/' + dt + '_DICOM_TAG_ANALYSIS_FM.xlsx')
#df.to_excel('ADD FOLDER PATH' + dt + '_DICOM_TAG_ANALYSIS_FM.xlsx')
#code to save the info as excel file:
#date of today + '_DICOM_TAG_ANALYSIS_FM.xlsx'
