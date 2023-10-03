# Начальный шаблон Excel
import xlwt
# импорт формат Дата
from datetime import datetime

# Стиль 1: Имя шрифта - Times New Roman, Цвет красный, Жирный, формат числа “1 000,00”
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')

# Стиль 2: В формат Даты 01.05.1989
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()

# Имя листа “A Test Sheet”
ws = wb.add_sheet('Лист 1')

x = 0
y = 0

# Запись в ячейки Данные начало 0.0 (столбец, строка, Данные, стиль/формула/прочее)
ws.write(x, y, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

# сохранения Файла “example.xls”
wb.save('example.xls')
