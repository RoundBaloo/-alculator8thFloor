from ..models import Data
from django.db.models import Sum


class typography():
    """
    класс, содержащий стили для ячеек таблицы.
    """
    title_format = {'text_wrap': True, 'align': 'center', 'bg_color': 'F59D0E',
                    'font_size': 14, 'bold': True, 'border': 5}
    column_title_format = {'text_wrap': True, 'align': 'center', 'border': 5,
                           'bg_color': 'F59D0E', 'bold': True}
    cell_format = {'align': 'center'}
    red_format = {'bg_color': 'FF9999', 'font_color': 'red', 'border': 5}
    green_format = {'bg_color': '99FFCC', 'font_color': '00CC00', 'border': 5}


def fill_base_table(workbook, worksheet, column_names,
                    day_merge_columns, night_merge_columns):
    """
    заполняет названия столбцов и строк, задает ширину столбцам,
    объединяет нужные ячейки под общие данные

    Args:
        workbook (xlsxwriter.workbook.Workbook): возвращаемый эксель файл
        worksheet (xlsxwriter.worksheet.Worksheet): заполняемая эксель страница
        column_names (list): список названий столбцов
        day_merge_columns (list): список номеров столбцов, в которых нужно обьединить ячейки для дневных машин
        night_merge_columns (list): список номеров столбцов, в которых нужно обьединить ячейки для ночных машин
    """
    # установление ширины столбцов
    worksheet.set_column(0, 0, 23)
    worksheet.set_column(1, len(column_names) - 1, 14)

    # Заполнение названий столбцов
    column_title_format = workbook.add_format(typography.column_title_format)

    col = 0
    for column_name in column_names:
        worksheet.write(1, col, column_name, column_title_format)
        col += 1

    # Заполнение названий строк
    row_names = ['180 часов', '168 часов', '79 часов',
                 '180 часов праздники/вых', '180 часов ночь']

    row = 2
    for row_name in row_names:
        worksheet.write(row, 0, row_name)
        row += 1

    # Объединение ячеек для общей информации дневных машин
    for column_num in day_merge_columns:
        worksheet.merge_range(2, column_num - 1, 4, column_num - 1, 0)

    # Объединение ячеек для общей информации ночных машин
    for column_num in night_merge_columns:
        worksheet.merge_range(5, column_num - 1, 6, column_num - 1, 0)


def color_green_red_cells(load_column_num, scarcity_column_num,
                          workbook, worksheet):
    """
    проверяет столбцы нагрузка и недостаток машин и красит их в зеленый
    или красный цвет по условию.

    Args:
        load_column_num (int): номер столбца нагрузка
        scarcity_column_num (int): номер столбца недостаток
        worksheet (xlsxwriter.worksheet.Worksheet): заполняемая эксель страница
        red_format (xlsxwriter.format.Format): формат красной ячейки
        green_format (xlsxwriter.format.Format): формат зеленой ячейки
    """
    need_workload = Data.objects.get(machine_type='180h_day').permitted_load

    # Формат для красной и зеленой ячейки
    red_format = workbook.add_format(typography.red_format)
    green_format = workbook.add_format(typography.green_format)

    red_load_condition = {'type': 'cell', 'criteria': '>',
                          'value': need_workload, 'format': red_format}
    worksheet.conditional_format(2, load_column_num - 1,
                                 6, load_column_num - 1, red_load_condition)

    green_load_condition = {'type': 'cell', 'criteria': '<=',
                            'value': need_workload, 'format': green_format}
    worksheet.conditional_format(2, load_column_num - 1,
                                 6, load_column_num - 1, green_load_condition)

    red_scarcity_condition = {'type': 'cell', 'criteria': '>',
                              'value': 0, 'format': red_format}
    worksheet.conditional_format(2, scarcity_column_num - 1,
                                 6, scarcity_column_num - 1, red_scarcity_condition)

    green_scarcity_condition = {'type': 'cell', 'criteria': '==',
                                'value': 0, 'format': green_format}
    worksheet.conditional_format(2, scarcity_column_num - 1,
                                 6, scarcity_column_num - 1, green_scarcity_condition)


def create_fact_excel_table(workbook, worksheet):
    """
    заполняет таблицу ФАКТ.

    Args:
        workbook (xlsxwriter.workbook.Workbook): возвращаемый эксель файл
        worksheet (xlsxwriter.worksheet.Worksheet): заполняемая эксель страница
    """

    # Подготовка стилей ячеек
    title_format = workbook.add_format(typography.title_format)
    cell_format = workbook.add_format(typography.cell_format)

    # Название таблицы
    worksheet.merge_range('B1:G1', 'ФАКТ', title_format)

    column_names = ['Машина', 'Максимальное кол-во файлов в месяц',
                    'Факт среднее кол-во файлов в месяц', 'Факт кол-во машин',
                    'Факт максимальное кол-во файлов', 'Факт нагрузка в %',
                    'Факт нехватка машин']
    day_merge_columns = [3, 6]
    night_merge_columns = [2, 4, 5, 7]

    fill_base_table(workbook, worksheet, column_names,
                    day_merge_columns, night_merge_columns)

    # Заполнение таблицы значениями
    row = 2
    for machine in Data.objects.all():
        worksheet.write(row, 1, machine.month_files, cell_format)
        worksheet.write(row, 2, machine.avg_fact_files_per_month, cell_format)
        worksheet.write(row, 3, machine.cnt_machines, cell_format)
        worksheet.write(row, 4, machine.max_files, cell_format)
        worksheet.write(row, 5, int(machine.load_fact), cell_format)  # Поправить, как изменится тип значения в моделс
        worksheet.write(row, 6, machine.scarcity_fact, cell_format)

        row += 1

    # Раскрашивание ячеек нагрузки и нехватки в красный и зеленый
    color_green_red_cells(6, 7, workbook, worksheet)


def create_plan_excel_table(workbook, worksheet):
    """
    заполняет таблицу ПЛАН.

    Args:
        workbook (xlsxwriter.workbook.Workbook): возвращаемый эксель файл
        worksheet (xlsxwriter.worksheet.Worksheet): заполняемая эксель страница
    """
    # Подготовка стилей ячеек
    title_format = workbook.add_format(typography.title_format)
    cell_format = workbook.add_format(typography.cell_format)

    # Название таблицы
    worksheet.merge_range('B1:J1', 'ПЛАН', title_format)

    column_names = ['Машина', 'Максимальное кол-во файлов в месяц',
                    'Факт среднее кол-во файлов в месяц', 'Кол-во новых УЗ',
                    'Количество файлов новых УЗ в месяц',
                    'Среднее кол-во файлов с учетом новых УЗ в месяц',
                    'Факт кол-во машин', 'Факт максимальное кол-во файлов',
                    'Планируемая нагрузка в %', 'Планируемая нехватка машин']
    day_merge_columns = [3, 5, 6, 9]
    night_merge_columns = [2, 7, 8, 10]

    fill_base_table(workbook, worksheet, column_names,
                    day_merge_columns, night_merge_columns)

    # Ячейка для 'Кол-во новых УЗ'
    worksheet.merge_range('D3:D7', 0)

    # заполнение таблицы значениями
    row = 2
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

    # Раскрашивание ячеек нагрузки и нехватки в красный и зеленый
    color_green_red_cells(9, 10, workbook, worksheet)


def create_fact_plan_excel_table(workbook, worksheet):
    """
    заполняет таблицу ФАКТ и ПЛАН.


    Args:
        workbook (xlsxwriter.workbook.Workbook): возвращаемый эксель файл
        worksheet (xlsxwriter.worksheet.Worksheet): заполняемая эксель страница
    """
    # Подготовка стилей ячеек
    title_format = workbook.add_format(typography.title_format)
    cell_format = workbook.add_format(typography.cell_format)

    # Названия групп столбцов
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
    day_merge_columns = [3, 6, 9, 10, 11]
    night_merge_columns = [2, 4, 5, 7, 12]

    fill_base_table(workbook, worksheet, column_names, day_merge_columns, night_merge_columns)

    # Ячейка для 'Кол-во новых УЗ'
    worksheet.merge_range('H3:H7', 0)

    # заполнение таблицы значениями
    row = 2
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

    # Раскрашивание ячеек нагрузки и нехватки факта в красный и зеленый
    color_green_red_cells(6, 7, workbook, worksheet)

    # Раскрашивание ячеек нагрузки и нехватки плана в красный и зеленый
    color_green_red_cells(11, 12, workbook, worksheet)


def get_context_dictionary():
    """
    Формирует словарь со всеми переменными, нужными в отчете.

    Returns:
        dict: словарь со всей нужной информацией для заполнения отчета
    """
    # Получаем нужные машины из БД
    machine_180h_day = Data.objects.get(machine_type='180h_day')
    machine_168h = Data.objects.get(machine_type='168h')
    machine_79h = Data.objects.get(machine_type='79h')
    machine_180h_night = Data.objects.get(machine_type='180h_night')
    machine_180h_weekend = Data.objects.get(machine_type='180h_weekend')

    # Кол-во файлов, которое можем обработать в месяц
    # sum_max_files = sum(Data.objects.all()[0]['avg_day_files'] + Data.objects.all()[3]['avg_day_files'] + Data.objects.all()[4]['avg_day_files'])

    objects = Data.objects.values('avg_fact_files_per_month')
    print(objects[3]['avg_fact_files_per_month'])
    sum_max_files = objects[0]['avg_fact_files_per_month'] + objects[3]['avg_fact_files_per_month'] + objects[4]['avg_fact_files_per_month']
    print(sum_max_files)
    # Заполнение словаря всей нужной информацией
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
