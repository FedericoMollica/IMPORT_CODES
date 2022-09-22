#!/usr/bin/env python
# coding: utf-8

# In[14]:


#AUTHOR: FEDERICO MOLLICA 2022
#SCRIPT: DICOM_TAG_ANALYSIS_FM_v1

#DESCRIPTION: 
#the first part of the code creates an excel file 
#containing all the dicom info from all the CTs present in one folder
#the second part of the code creates a second excel file
#containing only the columns for the selection of CTs for Thirona

#PROS:
#the first excel will be auto saved:'date of today' +'_DICOM_TAG_ANALYSIS_FM.xlsx'
#the second excel will be auto saved:'date of today' +'_AA_CTs_Req_List_FM.xlsx'

from datetime import date
from dicom_csv import join_tree
import pandas as pd
import os

today = date.today()
dt = today.strftime('%Y%m%d')
#code to set the date of today in a format YYMMDD

input_path = '/Users/048252/Downloads/ASPEN_TEST'
output_path = '/Users/048252/Downloads/'
#here we set our input and output folder directory, put the path inside '' 
#copy paste the directory of the folder containing the CTs in input
#copy paste the directory where you want to save the excel file in output

df = join_tree(input_path, relative=False, verbose=1)
#df = join_tree("ADD FOLDER PATH", relative=False, verbose=1)
df = df.drop_duplicates(subset = ['SeriesInstanceUID'], keep= 'first')
#codes to extract all the dicom info and keep only the unique series id

df.to_excel(output_path + dt + '_DICOM_TAG_ANALYSIS_FM.xlsx')
#df.to_excel('ADD FOLDER PATH' + dt + '_DICOM_TAG_ANALYSIS_FM.xlsx')
#code to save the info as excel file:
#date of today + '_DICOM_TAG_ANALYSIS_FM.xlsx'

'''
AA LungQ Method selection
'''

#only keep columns we need for the AA- LungQ analysis
#we can add, remove or sort the columns just changing the order below
df1 = df1[['StudyInstanceUID',
           'PatientID',
           'PatientName',
           'PatientBirthDate',
           'AcquisitionNumber',     
           'AcquisitionTime',
           'ConvolutionKernel',
           'ImageOrientationPatient0',
           'ImageOrientationPatient1',
           'ImageOrientationPatient2',
           'ImageOrientationPatient3',
           'ImageOrientationPatient4',
           'ImageOrientationPatient5',
           'Manufacturer',
           'PatientPosition',
           'PatientSex',
           'SeriesInstanceUID',
           'SeriesNumber',
           'SliceThickness',
           'StudyDate',
           'StudyDescription',
           'StudyID',
           'ImageComments']]

df1.to_excel(output_path + dt + '_AA_CTs_Req_List_FM.xlsx')
#code to save an extra excel for the AA LungQ method analysis
#date of today + '_AA_CTs_Req_List_FM.xlsx'


# In[ ]:




