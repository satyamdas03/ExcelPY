from openpyxl import Workbook, load_workbook

wb = load_workbook('Grades.xlsx')

# ws = wb.active
# ws['A2'].value = "Test"
# print(wb.sheetnames)
# wb.save('Grades.xlsx')
wb.create_sheet("Test")
print(wb.sheetnames)