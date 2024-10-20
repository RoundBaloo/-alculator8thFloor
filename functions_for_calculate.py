import math


class Machine:
    def __init__(self, name, hours_in_day, days_in_month, productivity):
        self.name = name
        self.hours_in_day = hours_in_day
        self.days_in_month = days_in_month
        self.productivity = productivity


    def calculate_max_files_number(self, result_dict, machines_number):
        files_in_a_day = round(self.hours_in_day * Calculator.minutes_in_hour / self.productivity * 0.85)
        if self.name not in result_dict:
            result_dict[self.name] = dict()
        result_dict[self.name]['month_files'] = files_in_a_day * self.days_in_month
        result_dict[self.name]['max_files'] = machines_number * result_dict[self.name]['month_files']


class Calculator:
    minutes_in_hour = 50

    day_machine_180hour = Machine('day_180hour', 11, 15, 8)
    day_machine_168hour = Machine('day_168hour', 8, 20, 8)
    day_machine_79hour = Machine('day_79hour', 4, 20, 8)
    weekends_machine = Machine('weekends', 11, 15, 6)
    night_machine = Machine('night', 11, 15, 6)


    def __init__(self, number_day_180hour_machines, number_day_168hour_machines, number_day_79hour_machines, number_night_machines):
        self.number_day_180hour_machines = number_day_180hour_machines
        self.number_day_168hour_machines = number_day_168hour_machines
        self.number_day_79hour_machines = number_day_79hour_machines
        self.number_weekends_machines = number_night_machines
        self.number_night_machines = number_night_machines


    def calculate_machines_scarcity(self, workload, files_number, result_dict, machine_name):
        machine_record = result_dict[machine_name]
        if workload < 0.86:
            return 0
        elif machine_name == 'day_168hour':
            machine_record['scarcity'] = round(files_number * (workload - 0.86) / 0.86 / machine_record['month_files'])
        else:
            machine_record['scarcity'] = math.ceil(files_number * (workload - 0.86) / 0.86 / machine_record['month_files'])


    def fact_calculate(self, avg_fact_files_number_day, avg_fact_files_number_weekends, avg_fact_files_number_night, result_dict):
        self.day_machine_180hour.calculate_max_files_number(result_dict, self.number_day_180hour_machines)
        self.day_machine_168hour.calculate_max_files_number(result_dict, self.number_day_168hour_machines)
        self.day_machine_79hour.calculate_max_files_number(result_dict, self.number_day_79hour_machines)

        key = 'max_files'
        day_files_number = result_dict['day_180hour'][key] + result_dict['day_168hour'][key] + result_dict['day_79hour'][key]
        result_dict['day_workload'] = avg_fact_files_number_day / day_files_number
        self.calculate_machines_scarcity(day_files_number, result_dict['day_workload'], result_dict, 'day_168hour')

        new_day_files_number = day_files_number + result_dict['day_168hour']['scarcity'] * result_dict['day_168hour']['month_files']
        new_day_workload = avg_fact_files_number_day / new_day_files_number
        result_dict['day_79hour']['scarcity'] = 0 if new_day_workload <= 0.86 else 1

        self.night_machine.calculate_max_files_number(result_dict, self.number_night_machines)
        self.weekends_machine.calculate_max_files_number(result_dict, self.number_weekends_machines)

        result_dict['night_workload'] = avg_fact_files_number_night / result_dict['night']['max_files']
        self.calculate_machines_scarcity(result_dict['night']['max_files'], result_dict['night_workload'], result_dict, 'night')
        
        result_dict['weekend_workload'] = avg_fact_files_number_weekends / result_dict['night']['max_files']
        self.calculate_machines_scarcity(result_dict['night']['max_files'], result_dict['weekend_workload'], result_dict, 'weekends')

        result_dict['night']['scarcity'] = max((result_dict['night']['scarcity'], result_dict['weekends']['scarcity']))
        result_dict['weekends']['scarcity'] = max((result_dict['night']['scarcity'], result_dict['weekends']['scarcity']))

        result_dict['avg_month_day_files_number'] = avg_fact_files_number_day
        result_dict['avg_month_weekends_files_number'] = avg_fact_files_number_weekends
        result_dict['avg_month_night_files_number'] = avg_fact_files_number_night

        return (result_dict)


    def plan_calculate(self, new_users_number, avg_fact_files_number_day, avg_fact_files_number_weekends, avg_fact_files_number_night):
        new_files_number_night = int(new_users_number * 1.3 * 0.27)
        new_files_number_weekends = int(new_users_number * 1.3 * 0.15)
        new_files_number_day = round(new_users_number * 1.3) - new_files_number_night - new_files_number_weekends

        avg_plan_files_number_night = new_files_number_night + avg_fact_files_number_night
        avg_plan_files_number_weekends = new_files_number_weekends + avg_fact_files_number_weekends
        avg_plan_files_number_day = new_files_number_day + avg_fact_files_number_day

        return self.fact_calculate(avg_plan_files_number_day, avg_plan_files_number_weekends, avg_plan_files_number_night, {})
#base_check
calc = Calculator(2, 3, 4, 1)
print(calc.fact_calculate(6539, 833, 1143, {}))
print(calc.plan_calculate(600, 6539, 833, 1143))
