from ..models import TableColumnName

def fill_fact_table_names():
    names = {
        'month_files': 'Максимальное кол-во файлов в месяц',
        'avg_fact_files_per_month': 'Факт среднего кол-ва файлов в месяц',
        'avg_fact_files_with_new': 'Факт среднего кол-ва файлов в месяц',
        'new_users_files': 'Факт среднего кол-ва файлов в месяц',
        'cnt_machines': 'Факт кол-ва машин',
        'max_files': 'Факт максимального кол-ва файлов',
        'load_fact': 'Факт нагрузки, %',
        'scarcity_fact': 'Факт нехватки машин',
        'cnt_UZ': 'Факт нехватки машин',
        'load_plan': 'Факт нехватки машин',
        'scarcity_plan': 'Факт нехватки машин1',
    }
    
    print('success')
    
    if (len(TableColumnName.objects.all()) > 0):
        TableColumnName.objects.all().delete()
    
    fact_table_column_name_instance = TableColumnName(**names)
    fact_table_column_name_instance.save()
        