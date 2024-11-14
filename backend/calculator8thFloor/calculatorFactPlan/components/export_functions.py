from ..models import Data


def create_fact_excel_table(worksheet):
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

    row = 2
    for row_name in row_names:
        worksheet.write(row, 0, row_name)
        row += 1

    # Объединение ячеек для дневных машин
    worksheet.merge_range('C3:C5', 0)
    worksheet.merge_range('F3:F5', 0)

    # Объединение ячеек для ночных и праздничных машин
    worksheet.merge_range('B6:B7', 0)
    worksheet.merge_range('D6:D7', 0)
    worksheet.merge_range('E6:E7', 0)
    worksheet.merge_range('G6:G7', 0)

    row = 2
    # заполнение таблицы значениями
    for machine in Data.objects.all():
        worksheet.write(row, 1, machine.month_files)
        worksheet.write(row, 2, machine.avg_fact_files_per_month)
        worksheet.write(row, 3, machine.cnt_machines)
        worksheet.write(row, 4, machine.max_files)
        worksheet.write(row, 5, machine.load_fact)
        worksheet.write(row, 6, machine.scarcity_fact)

        row += 1


def create_plan_excel_table(worksheet):
    worksheet.merge_range('A1:I1', 'ПЛАН')

    column_names = ['Машина', 'Максимальное кол-во файлов в месяц',
                    'Факт среднее кол-во файлов в месяц', 'Кол-во новых УЗ',
                    'Среднее кол-во файлов с учетом новых УЗ в месяц',
                    'Факт кол-во машин', 'Факт максимальное кол-во файлов',
                    'Планируемая нагрузка в %', 'Планируемая нехватка машин']
    col = 0
    for column_name in column_names:
        worksheet.write(1, col, column_name)
        col += 1

    row_names = ['180 часов', '168 часов', '79 часов',
                 '180 часов праздники/вых', '180 часов ночь']
    row = 2
    for row_name in row_names:
        worksheet.write(row, 0, row_name)
        row += 1

    # Ячейка для 'Кол-во новых УЗ'
    worksheet.merge_range('D3:D7', 0)

    # Объединение ячеек для дневных машин
    worksheet.merge_range('C3:C5', 0)
    worksheet.merge_range('E3:E5', 0)
    worksheet.merge_range('H3:H5', 0)

    # Объединение ячеек для ночных и праздничных машин
    worksheet.merge_range('B6:B7', 0)
    worksheet.merge_range('F6:F7', 0)
    worksheet.merge_range('G6:G7', 0)
    worksheet.merge_range('I6:I7', 0)

    row = 2
    # заполнение таблицы значениями
    for machine in Data.objects.all():
        worksheet.write(row, 1, machine.month_files)
        worksheet.write(row, 2, machine.avg_fact_files_per_month)
        worksheet.write(row, 3, machine.cnt_UZ)
        worksheet.write(row, 4, machine.avg_fact_files_with_new)
        worksheet.write(row, 5, machine.cnt_machines)
        worksheet.write(row, 6, machine.max_files)
        worksheet.write(row, 7, machine.load_plan)
        worksheet.write(row, 8, machine.scarcity_plan)

        row += 1


def create_fact_plan_excel_table(worksheet):
    create_fact_excel_table(worksheet)

    worksheet.merge_range('H1:M1', 'ПЛАН')

    column_names = ['Кол-во новых УЗ',
                    'Среднее кол-во файлов с учетом новых УЗ в месяц',
                    'Факт кол-во машин', 'Факт максимальное кол-во файлов',
                    'Планируемая нагрузка в %', 'Планируемая нехватка машин']
    col = 7
    for column_name in column_names:
        worksheet.write(1, col, column_name)
        col += 1

    # Ячейка для 'Кол-во новых УЗ'
    worksheet.merge_range('H3:H7', 0)

    # Объединение ячеек для дневных машин
    worksheet.merge_range('I3:I5', 0)
    worksheet.merge_range('L3:L5', 0)

    # Объединение ячеек для ночных и праздничных машин
    worksheet.merge_range('J6:J7', 0)
    worksheet.merge_range('K6:K7', 0)
    worksheet.merge_range('M6:M7', 0)

    row = 2
    # заполнение таблицы значениями
    for machine in Data.objects.all():
        worksheet.write(row, 7, machine.cnt_UZ)
        worksheet.write(row, 8, machine.avg_fact_files_with_new)
        worksheet.write(row, 9, machine.cnt_machines)
        worksheet.write(row, 10, machine.max_files)
        worksheet.write(row, 11, machine.load_plan)
        worksheet.write(row, 12, machine.scarcity_plan)

        row += 1
