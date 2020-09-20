import xlsxwriter
import get_info

workbook = xlsxwriter.Workbook("groceries.xlsx")
worksheet = workbook.add_worksheet()

weeks_groceries = get_info.get_weeks_groceries(2020, 9, 1)
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Quantity', bold)
worksheet.write('C1', 'Unit', bold)


row = 1
col = 0

for item, quantity, unit in weeks_groceries:
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, quantity)
    worksheet.write(row, col + 2, unit)
    row += 1

workbook.close()
