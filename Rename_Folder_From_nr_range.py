import os
import xlsxwriter

# Set the directory path you want to extract folder names from
path = r"F:\20230224_056_MFup_Checked"

# Create an Excel workbook and worksheet
workbook = xlsxwriter.Workbook('folder_names.xlsx')
worksheet = workbook.add_worksheet()

# Set the row and column variables
row = 0
col = 0

# Loop through the directory and get the folder names
for folder in os.listdir(path):
    if os.path.isdir(os.path.join(path, folder)):
        worksheet.write(row, col, folder)
        row += 1

# Close the workbook
workbook.close()
