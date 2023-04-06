import random
import xlsxwriter

# Create a list of 210 random shuffled numbers between 1 and 210
numbers = list(range(1, 211))
random.shuffle(numbers)

# Create an Excel workbook and worksheet
workbook = xlsxwriter.Workbook('random_numbers.xlsx')
worksheet = workbook.add_worksheet()

# Set the row and column variables
row = 0
col = 0

# Loop through the shuffled list and write each number to a new row in the second column of the Excel worksheet
for number in numbers:
    worksheet.write(row, col, "")
    worksheet.write(row, col + 1, number)
    row += 1

# Close the workbook
workbook.close()
