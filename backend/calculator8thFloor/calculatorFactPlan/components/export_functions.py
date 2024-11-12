import xlsxwriter
from ..models import Data


def fact_export():
    workbook = xlsxwriter.Workbook('fact.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.merge_range('A1:G1', 'ФАКТ')
    column_names = ['Машина', 'Максимальное кол-во файлов в месяц',
                    'Факт среднее кол-во файлов в месяц', 'Факт кол-во машин',
                    'Факт максимальное кол-во файлов', 'Факт нагрузка в %',
                    'Факт нехватка машин ']
    row_names = ['180 часов', '168 часов', '79 часов',
                 '180 часов праздники/вых', '180 часов ночь']
    
    col = 0
    for column_name in column_names:
        worksheet.write(1, col, column_name)
        col += 1
    
    row = 1
    for row_name in row_names:
        worksheet.write(row, 0, row_name)
        row += 1
    
    day_180h = Data.objects.filter
    


