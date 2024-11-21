from ..models import Data


class typography():
    title_format = {'text_wrap': True, 'align': 'center', 'fg_color': 'yellow',
                    'font_size': 14, 'bold': True, 'border': 5}
    column_title_format = {'text_wrap': True, 'align': 'center', 'border': 5,
                           'bg_color': 'yellow', 'bold': True}
    cell_format = {'align': 'center'}


def create_fact_excel_table(workbook, worksheet):
    # установление ширины столбцов
    worksheet.set_column('A:A', 23)
    worksheet.set_column('B:G', 14)

    # Подготовка стилей ячеек
    title_format = workbook.add_format(typography.title_format)
    column_name_format = workbook.add_format(typography.column_title_format)
    cell_format = workbook.add_format(typography.cell_format)

    worksheet.merge_range('B1:G1', 'ФАКТ', title_format)
    column_names = ['Машина', 'Максимальное кол-во файлов в месяц',
                    'Факт среднее кол-во файлов в месяц', 'Факт кол-во машин',
                    'Факт максимальное кол-во файлов', 'Факт нагрузка в %',
                    'Факт нехватка машин']
    row_names = ['180 часов', '168 часов', '79 часов',
                 '180 часов праздники/вых', '180 часов ночь']

    col = 0
    for column_name in column_names:
        worksheet.write(1, col, column_name, column_name_format)
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
        worksheet.write(row, 1, machine.month_files, cell_format)
        worksheet.write(row, 2, machine.avg_fact_files_per_month, cell_format)
        worksheet.write(row, 3, machine.cnt_machines, cell_format)
        worksheet.write(row, 4, machine.max_files, cell_format)
        worksheet.write(row, 5, machine.load_fact, cell_format)
        worksheet.write(row, 6, machine.scarcity_fact, cell_format)

        row += 1


def create_plan_excel_table(workbook, worksheet):
    # установление ширины столбцов
    worksheet.set_column('A:A', 23)
    worksheet.set_column('B:J', 14)

    # Подготовка стилей ячеек
    title_format = workbook.add_format(typography.title_format)
    column_name_format = workbook.add_format(typography.column_title_format)
    cell_format = workbook.add_format(typography.cell_format)

    worksheet.merge_range('B1:I1', 'ПЛАН', title_format)

    column_names = ['Машина', 'Максимальное кол-во файлов в месяц',
                    'Факт среднее кол-во файлов в месяц', 'Кол-во новых УЗ',
                    'Количество файлов новых УЗ в месяц',
                    'Среднее кол-во файлов с учетом новых УЗ в месяц',
                    'Факт кол-во машин', 'Факт максимальное кол-во файлов',
                    'Планируемая нагрузка в %', 'Планируемая нехватка машин']
    col = 0
    for column_name in column_names:
        worksheet.write(1, col, column_name, column_name_format)
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
    worksheet.merge_range('F3:F5', 0)
    worksheet.merge_range('I3:I5', 0)

    # Объединение ячеек для ночных и праздничных машин
    worksheet.merge_range('B6:B7', 0)
    worksheet.merge_range('G6:G7', 0)
    worksheet.merge_range('H6:H7', 0)
    worksheet.merge_range('J6:J7', 0)

    row = 2
    # заполнение таблицы значениями
    for machine in Data.objects.all():
        worksheet.write(row, 1, machine.month_files, cell_format)
        worksheet.write(row, 2, machine.avg_fact_files_per_month, cell_format)
        worksheet.write(row, 3, machine.cnt_UZ, cell_format)
        worksheet.write(row, 4, machine.new_users_files, cell_format)
        worksheet.write(row, 5, machine.avg_fact_files_with_new, cell_format)
        worksheet.write(row, 6, machine.cnt_machines, cell_format)
        worksheet.write(row, 7, machine.max_files, cell_format)
        worksheet.write(row, 8, machine.load_plan, cell_format)
        worksheet.write(row, 9, machine.scarcity_plan, cell_format)

        row += 1


def create_fact_plan_excel_table(workbook, worksheet):
    # установление ширины столбцов
    worksheet.set_column('A:A', 23)
    worksheet.set_column('B:N', 14)

    # Подготовка стилей ячеек
    title_format = workbook.add_format(typography.title_format)
    column_name_format = workbook.add_format(typography.column_title_format)
    cell_format = workbook.add_format(typography.cell_format)

    worksheet.merge_range('B1:E1', 'Общие Данные', title_format)
    worksheet.merge_range('F1:G1', 'ФАКТ', title_format)
    worksheet.merge_range('H1:L1', 'ПЛАН', title_format)

    column_names = ['Машина', 'Максимальное кол-во файлов в месяц',
                    'Факт среднее кол-во файлов в месяц', 'Факт кол-во машин',
                    'Факт максимальное кол-во файлов', 'Факт нагрузка в %',
                    'Факт нехватка машин', 'Кол-во новых УЗ',
                    'Количество файлов новых УЗ в месяц',
                    'Среднее кол-во файлов с учетом новых УЗ в месяц',
                    'Планируемая нагрузка в %', 'Планируемая нехватка машин']
    col = 0
    for column_name in column_names:
        worksheet.write(1, col, column_name, column_name_format)
        col += 1

    row_names = ['180 часов', '168 часов', '79 часов',
                 '180 часов праздники/вых', '180 часов ночь']
    row = 2
    for row_name in row_names:
        worksheet.write(row, 0, row_name)
        row += 1

    # Ячейка для 'Кол-во новых УЗ'
    worksheet.merge_range('H3:H7', 0)

    # Объединение ячеек для дневных машин
    worksheet.merge_range('C3:C5', 0)
    worksheet.merge_range('F3:F5', 0)
    worksheet.merge_range('I3:I5', 0)
    worksheet.merge_range('J3:J5', 0)
    worksheet.merge_range('K3:K5', 0)

    # Объединение ячеек для ночных и праздничных машин
    worksheet.merge_range('B6:B7', 0)
    worksheet.merge_range('D6:D7', 0)
    worksheet.merge_range('E6:E7', 0)
    worksheet.merge_range('G6:G7', 0)
    worksheet.merge_range('L6:L7', 0)

    row = 2
    # заполнение таблицы значениями
    for machine in Data.objects.all():
        worksheet.write(row, 1, machine.month_files, cell_format)
        worksheet.write(row, 2, machine.avg_fact_files_per_month, cell_format)
        worksheet.write(row, 3, machine.cnt_machines, cell_format)
        worksheet.write(row, 4, machine.max_files, cell_format)
        worksheet.write(row, 5, machine.load_fact, cell_format)
        worksheet.write(row, 6, machine.scarcity_fact, cell_format)
        worksheet.write(row, 7, machine.cnt_UZ, cell_format)
        worksheet.write(row, 8, machine.new_users_files, cell_format)
        worksheet.write(row, 9, machine.avg_fact_files_with_new, cell_format)
        worksheet.write(row, 10, machine.load_plan, cell_format)
        worksheet.write(row, 11, machine.scarcity_plan, cell_format)

        row += 1


def get_context_dictionary():
    machine_180h_day = Data.objects.get(machine_type='180h_day')
    machine_168h = Data.objects.get(machine_type='168h')
    machine_79h = Data.objects.get(machine_type='79h')
    machine_180h_night = Data.objects.get(machine_type='180h_night')
    machine_180h_weekend = Data.objects.get(machine_type='180h_weekend')

    sum_max_files = sum(x.max_files for x in Data.objects.all())
    context = {
        'sum_max_files': sum_max_files,
        'avg_day_files': machine_180h_day.avg_fact_files_per_month,
        'avg_night_weekend_files': machine_180h_night.avg_fact_files_per_month + machine_180h_weekend.avg_fact_files_per_month,
        'machines_180h': machine_180h_day.cnt_machines,
        'machines_168h': machine_168h.cnt_machines,
        'machines_79h': machine_79h.cnt_machines,
        'fact_day_workload': machine_180h_day.load_fact,
        'fact_night_workload': machine_180h_night.load_fact,
        'fact_scarcity_180h': machine_180h_day.scarcity_fact,
        'fact_scarcity_168h': machine_168h.scarcity_fact,
        'fact_scarcity_79h': machine_79h.scarcity_fact,
        'new_users': machine_180h_day.cnt_UZ,
        'new_day_files': machine_180h_day.new_users_files,
        'new_night_weekend_files': machine_180h_night.new_users_files + machine_180h_weekend.new_users_files,
        'new_day_avg_files': machine_180h_day.avg_fact_files_with_new,
        'new_night_weekend_avg_files': machine_180h_night.avg_fact_files_with_new + machine_180h_weekend.avg_fact_files_with_new,
        'plan_day_workload': machine_180h_day.load_plan,
        'plan_night_workload': machine_180h_night.load_plan,
        'plan_scarcity_180h': machine_180h_day.scarcity_plan,
        'plan_scarcity_168h': machine_168h.scarcity_plan,
        'plan_scarcity_79h': machine_79h.scarcity_plan
    }

    return context
