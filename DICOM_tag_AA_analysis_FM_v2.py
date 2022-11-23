
#AUTHOR: FEDERICO MOLLICA 2022
#SCRIPT: DICOM_TAG_ANALYSIS_FM_v2

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
import numpy as np

#######################################################
#1st step:
#Creating the date of today and select input and output directory
#######################################################

today = date.today()
dt = today.strftime('%Y%m%d')
#code to set the date of today in a format YYMMDD

input_path = r'F:\Federico\FORMAT\Unzipped_CTs'
output_path = r'F:\Federico\FORMAT\Unzipped_CTs'
#here we set our input and output folder directory, put the path inside '' 
#copy paste the directory of the folder containing the CTs in input
#copy paste the directory where you want to save the excel file in output

#######################################################
#2nd step:
#Extracting all DICOM info from DICOM files in one directory
#Grouping the reconstructions using the unique series instance UID
#######################################################

df = join_tree(input_path, relative=False, verbose=1)
#this takes all the dicom tags information from all the dicom slices
df1 = df.drop_duplicates(subset = ['SeriesInstanceUID'], keep= 'first')
#codes to extract all the dicom info and keep only the unique series id

df2 = df[['SeriesInstanceUID','CTDIvol', 'XRayTubeCurrent', 'SliceThickness' ]]
series = df2['SeriesInstanceUID'].unique()

#######################################################
#3rd step:
#Calculate the CTDIvol_mean and the XRayTubeCurrent_mean (df1)
#Delete all the duplicates ID from the main df
#Merging the CTDIvol_mean and the XRayTubeCurrent_mean in a new df (df2) with the other DICOM info
#######################################################

CTDI_mean = []
Xray_tube_mean = []
SliceThickness_mean = []

for s in series:
    df3 = df2[df2['SeriesInstanceUID']==s]
    CTDI_avg = np.mean(df3['CTDIvol'])
    Xray_tube_avg = np.mean(df3['XRayTubeCurrent'])
    SliceThickness_avg = np.mean(df3['SliceThickness'])
    CTDI_mean.append(CTDI_avg)
    Xray_tube_mean.append(Xray_tube_avg)
    SliceThickness_mean.append(SliceThickness_avg)

df1['CTDIvol_mean'] = CTDI_mean
df1['XRayTubeCurrent_mean'] = Xray_tube_mean
df1['SliceThickness_mean'] = SliceThickness_mean

df1 = df1.drop(columns = ['CTDIvol'])
df1 = df1.drop(columns = ['XRayTubeCurrent'])
#code to delete the columns we do not need anymore

#######################################################
#4th step:
#Saving the (df2) as an excel file in the selected directory
#######################################################

df1.to_excel(output_path + dt + '_DICOM_TAG_ANALYSIS_FM.xlsx')
#df.to_excel('ADD FOLDER PATH' + dt + '_DICOM_TAG_ANALYSIS_FM.xlsx')
#code to save the info as excel file:
#date of today + '_DICOM_TAG_ANALYSIS_FM.xlsx'

'''
AA LungQ Method selection
'''

#######################################################
#5th step:
#Creating a new df (df3) with only the columns we need for the AA-analysis
#Saving the new df (df3) as an excel file in the selected directory
#######################################################

#only keep columns we need for the AA- LungQ analysis
#we can add, remove or sort the columns just changing the order below
df4 = df1[['PathToFolder',
           'SeriesInstanceUID',
           'SeriesNumber',
           'PatientID',
           'AcquisitionNumber',     
           'AcquisitionTime',
           'ConvolutionKernel',
           'CTDIvol_mean',
           'Manufacturer',
           'ManufacturerModelName',
           'PatientPosition',
           'PatientSex',
           'SliceThickness',
           'SliceThickness_mean',
           'XRayTubeCurrent_mean']]

df4.to_excel(output_path + dt + '_AA_CTs_Req_List_FM.xlsx')
#code to save an extra excel for the AA LungQ method analysis
#date of today + '_AA_CTs_Req_List_FM.xlsx'
