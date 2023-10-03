# Начальный шаблон Excel
import xlwt
# импорт формат Дата
from datetime import datetime

# ввод своих фин остатков 
cash = int(input("Введите пожалуйста сколько у вас налички \n"))
bez_nal = int(input("Введите пожалуйста сколько у вас карточки\n"))

# Стиль 1: Имя шрифта - Times New Roman, Цвет красный, Жирный, формат числа “1 000,00”
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
# Стиль 2: Формат Даты 01.05.1989
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
wb = xlwt.Workbook()
# Имя листа “A Test Sheet”
ws = wb.add_sheet('Лист 1')


# ws.write(0, 0, "Месяц", style0)
y = ["Январе", "Феврале", "Марте", "Апреле", "Мае", "Июне", "Июле", "Августе", "Сентябре", "Октябре", "Ноябре",
     "Декабре"]
i = 0
namber = 1

ws.write(0, 0, "Месяца", style0)
ws.write(0, 1, "Налички", style0)
ws.write(0, 2, "На карте", style0)

ws.write(1, 0, "Январь")
ws.write(2, 0, "Февраль")
ws.write(3, 0, "Март")

ws.write(4, 0, "Апрель")
ws.write(5, 0, "Май")
ws.write(6, 0, "Июнь")

ws.write(7, 0, "Июль")
ws.write(8, 0, "Август")
ws.write(9, 0, "Сентябрь")

ws.write(10, 0, "Октябрь")
ws.write(11, 0, "Ноябрь")
ws.write(12, 0, "Декабрь")

x_cash = 1
y_bez_nal = 1

# Функция подсчета финансов
def test():
    global bez_nal, cash, x_cash, y_bez_nal
    counter = 0
    # цикл по месяцам
    while counter < 12:
        cash = int(cash)
        bez_nal = float(bez_nal)
        cash = round(cash, 2)
        bez_nal = round(bez_nal, 2)
        cash = cash + 2000
        bez_nal = bez_nal + bez_nal * 0.30
        ws.write(x_cash, 1, cash)
        ws.write(y_bez_nal, 2, bez_nal)
        x_cash += 1
        y_bez_nal += 1
        cash = str(cash)
        bez_nal = str(bez_nal)

        counter = counter + 1

    return cash, bez_nal



test()

wb.save('example.xls')
# сохранения Файла “example.xls”

