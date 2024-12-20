from ..models import Data
from .functions_for_calculate import Calculator


class DataUpdater:
    def __init__(self, input_data):
        self.input_data = input_data
        self.cnt_machines = list(Data.objects.values_list('cnt_machines', flat=True))
        self.calculator = Calculator({
            '180h': input_data['cnt_machines']['180h'],
            '168h': input_data['cnt_machines']['168h'],
            '79h': input_data['cnt_machines']['79h'],
        })
        self.files = list(Data.objects.values_list('avg_fact_files_per_month', flat=True))

    def handle_inputed_data(self, table):
        """Обновляет записи в таблице на основе введенных

        Args:
            table (str): Какие таблицы следует обновить: fact - факт, plan - план, both - обе
        """
        for obj in Data.objects.all():
            obj.cnt_machines = self.input_data['cnt_machines'][f'{obj.machine_type}'.split('_')[0]]
            obj.avg_fact_files_per_month = self.input_data['avg_fact_files_per_month'][f'{obj.machine_type}']
            obj.cnt_UZ = self.input_data['cnt_UZ']
            if (table == 'plan' or table == 'both'):
                obj.permitted_load = self.input_data['permitted_load']
            obj.save()
        self.update_calculated_data(table)

    def update_calculated_data(self, table):
        """Передает введенные данные в класс для расчета, сохраняет новые расчитанные данные в БД

        Args:
            table (str): Какие таблицы следует обновить: fact - факт, plan - план, both - обе
        """
        cnt_machines = Data.objects.values_list('cnt_machines', flat=True)
        self.calculator.set_new_machines_numbers({
            '180h': cnt_machines[0],
            '168h': cnt_machines[1],
            '79h': cnt_machines[2],
        })
        avg_fact_files_per_month = list(Data.objects.values_list('avg_fact_files_per_month', flat=True))
        month_files = self.calculator.get_machines_month_files()
        max_files = self.calculator.get_machines_max_files()
        load_fact = self.calculator.get_workloads(
            'fact', 
            avg_fact_files_per_month[0], 
            avg_fact_files_per_month[3], 
            avg_fact_files_per_month[4], 
            self.input_data['cnt_UZ'])
        scarcity_fact = self.calculator.get_machines_scarcity(
            'fact', 
            avg_fact_files_per_month[0], 
            avg_fact_files_per_month[3], 
            avg_fact_files_per_month[4], 
            self.input_data['cnt_UZ'],
            self.input_data['permitted_load'] / 100)
        load_plan = self.calculator.get_workloads(
            'plan', 
            avg_fact_files_per_month[0], 
            avg_fact_files_per_month[3], 
            avg_fact_files_per_month[4], 
            self.input_data['cnt_UZ'])
        scarcity_plan = self.calculator.get_machines_scarcity(
            'plan', 
            avg_fact_files_per_month[0], 
            avg_fact_files_per_month[3], 
            avg_fact_files_per_month[4], 
            self.input_data['cnt_UZ'],
            self.input_data['permitted_load'] / 100)
        avg_fact_files_with_new = self.calculator.get_new_avg_files(
            avg_fact_files_per_month[0], 
            avg_fact_files_per_month[3], 
            avg_fact_files_per_month[4], 
            self.input_data['cnt_UZ'])
        new_users_files = self.calculator.get_new_users_files(self.input_data['cnt_UZ'])

        for obj in Data.objects.all():
            obj.month_files = month_files[f'{obj.machine_type}']
            obj.max_files = max_files[f'{obj.machine_type}']
            if (table == 'fact' or table == 'both'):
                obj.load_fact = load_fact[f'{obj.machine_type}']
                obj.scarcity_fact = scarcity_fact[f'{obj.machine_type}']
            if (table == 'plan' or table == 'both'):
                obj.avg_fact_files_with_new = avg_fact_files_with_new[f'{obj.machine_type}']
                obj.new_users_files = new_users_files[f'{obj.machine_type}']
                obj.load_plan = load_plan[f'{obj.machine_type}']
                obj.scarcity_plan = scarcity_plan[f'{obj.machine_type}']
            obj.save()
