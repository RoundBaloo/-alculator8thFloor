from ..models import TableColumnName

def fill_fact_table_names():
    names = {
        'month_files': 'Максимальное кол-во файлов в месяц',
        'avg_fact_files_per_month': 'Факт среднего кол-ва файлов в месяц',
        'avg_fact_files_with_new': 'Кол-во файлов с учетом новых УЗ',
        'new_users_files': 'Кол-во файлов новых пользователей',
        'cnt_machines': 'Факт кол-ва машин',
        'max_files': 'Факт максимального кол-ва файлов',
        'load_fact': 'Факт нагрузки, %',
        'scarcity_fact': 'Факт нехватки машин',
        'cnt_UZ': 'Кол-во новых УЗ',
        'load_plan': 'Факт нагрузки, в %',
        'scarcity_plan': 'Планируемая нехватка машин',
    }
    
    print('success')
    
    if (len(TableColumnName.objects.all()) > 0):
        TableColumnName.objects.all().delete()
    
    fact_table_column_name_instance = TableColumnName(**names)
    fact_table_column_name_instance.save()
        