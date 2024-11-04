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
    
    
    def update_inputed_data(self):
        for obj in Data.objects.all():
            obj.cnt_machines = self.input_data['cnt_machines'][f'{obj.machine_type}'.split('_')[0]]
            obj.avg_fact_files_per_month = self.input_data['avg_fact_files_per_month'][f'{obj.machine_type}']
            obj.cnt_UZ = self.input_data['cnt_UZ']
            obj.save()
        self.update_calculated_data()
    
        
    def update_calculated_data(self):
        cnt_machines = Data.objects.values_list('cnt_machines', flat=True)
        self.calculator.set_new_machines_numbers({
            '180h': cnt_machines[0],
            '168h': cnt_machines[1],
            '79h': cnt_machines[2],
        })
        avg_fact_files_per_month = list(dict.fromkeys(Data.objects.values_list('avg_fact_files_per_month', flat=True)))
        for obj in Data.objects.all():
            # for all data
            obj.month_files = self.calculator.get_machines_month_files()[f'{obj.machine_type}']
            obj.max_files = self.calculator.get_machines_max_files()[f'{obj.machine_type}']
            obj.load_fact = self.calculator.get_workloads(
                'fact', 
                avg_fact_files_per_month[0], 
                avg_fact_files_per_month[1], 
                avg_fact_files_per_month[2], 
                self.input_data['cnt_UZ'])[f'{obj.machine_type}']
            obj.scarcity_fact = self.calculator.get_machines_scarcity(
                'fact', 
                avg_fact_files_per_month[0], 
                avg_fact_files_per_month[1], 
                avg_fact_files_per_month[2], 
                self.input_data['cnt_UZ'])[f'{obj.machine_type}']
            # for plan
            obj.load_plan = self.calculator.get_workloads(
                'plan', 
                avg_fact_files_per_month[0], 
                avg_fact_files_per_month[1], 
                avg_fact_files_per_month[2], 
                self.input_data['cnt_UZ'])[f'{obj.machine_type}']
            obj.scarcity_plan = self.calculator.get_machines_scarcity(
                'plan', 
                avg_fact_files_per_month[0], 
                avg_fact_files_per_month[1], 
                avg_fact_files_per_month[2], 
                self.input_data['cnt_UZ'])[f'{obj.machine_type}']
            obj.save()