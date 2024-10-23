import math

class Machine:
    names = []
    minutes_in_hour = 50

    def __init__(self, name, hours_in_day, days_in_month, productivity, value_dict):
        self.name = name
        Machine.names.append(name)
        self.files_in_a_day = round(hours_in_day * Machine.minutes_in_hour / productivity * 0.85)

        value_dict[self.name] = dict()
        value_dict[self.name]['month_files'] = self.files_in_a_day * days_in_month


class Calculator:
    value_dict = dict()

    day_machine_180hour = Machine('day_180hour', 11, 15, 8, value_dict)
    day_machine_168hour = Machine('day_168hour', 8, 20, 8, value_dict)
    day_machine_79hour = Machine('day_79hour', 4, 20, 8, value_dict)
    weekends_machine = Machine('weekends', 11, 15, 6, value_dict)
    night_machine = Machine('night', 11, 15, 6, value_dict)

    def __init__(self, number_day_180hour_machines, number_day_168hour_machines, number_day_79hour_machines, number_night_machines):
        key = 'number'

        self.value_dict['day_180hour'][key] = number_day_180hour_machines
        self.value_dict['day_168hour'][key] = number_day_168hour_machines
        self.value_dict['day_79hour'][key] = number_day_79hour_machines
        self.value_dict['night'][key] = number_night_machines
        self.value_dict['weekends'][key] = number_night_machines


    def set_new_machines_numbers(self, number_day_180hour_machines, number_day_168hour_machines, number_day_79hour_machines, number_night_machines):
        self.value_dict = dict()
        key = 'number'

        day_machine_180hour = Machine('day_180hour', 11, 15, 8, self.value_dict)
        day_machine_168hour = Machine('day_168hour', 8, 20, 8, self.value_dict)
        day_machine_79hour = Machine('day_79hour', 4, 20, 8, self.value_dict)
        weekends_machine = Machine('weekends', 11, 15, 6, self.value_dict)
        night_machine = Machine('night', 11, 15, 6, self.value_dict)

        self.value_dict['day_180hour'][key] = number_day_180hour_machines
        self.value_dict['day_168hour'][key] = number_day_168hour_machines
        self.value_dict['day_79hour'][key] = number_day_79hour_machines
        self.value_dict['night'][key] = number_night_machines
        self.value_dict['weekends'][key] = number_night_machines
    

    def get_machines_month_files(self):
        month_files_dict = dict()
        key = 'month_files'

        for name in Machine.names:
            month_files_dict[name] = self.value_dict[name][key]

        return month_files_dict


    def calculate_machines_max_files(self):
        key = 'max_files'

        for name in Machine.names:
            self.value_dict[name][key] = self.value_dict[name]['month_files'] * self.value_dict[name]['number']


    def get_machines_max_files(self):
        max_files_dict = dict()
        key = 'max_files'

        if key not in self.value_dict[self.day_machine_180hour.name]:
            self.calculate_machines_max_files()

        for name in Machine.names:
            max_files_dict[name] = self.value_dict[name][key]

        return max_files_dict


    def calculate_workloads(self, type, avg_day_files, avg_night_files, avg_weekends_files, new_users_number): #type = plan or fact
        self.value_dict[type] = dict()

        if 'max_files' not in self.value_dict[self.day_machine_180hour.name]:
            self.calculate_machines_max_files()
        
        if type == 'plan':
            new_night_files = round(new_users_number * 1.3 * 0.27)
            avg_night_files += new_night_files
            new_weekends_files = round(new_users_number * 1.3 * 0.15)
            avg_weekends_files += new_weekends_files
            avg_day_files += round(new_users_number * 1.3) - new_night_files - new_weekends_files

        key = 'max_files'
        day_files = self.value_dict['day_180hour'][key] + self.value_dict['day_168hour'][key] + self.value_dict['day_79hour'][key]

        self.value_dict[type]['day'] = avg_day_files / day_files
        self.value_dict[type]['night'] = avg_night_files / self.value_dict['night'][key]
        self.value_dict[type]['weekends'] = avg_weekends_files / self.value_dict['weekends'][key]


    def get_workloads(self, type, avg_day_files, avg_night_files, avg_weekends_files, new_users_number): #type = plan or fact
        workloads_dict = dict()

        if type not in self.value_dict:
            self.calculate_workloads(type, avg_day_files, avg_night_files, avg_weekends_files, new_users_number)

        workloads_dict['day'] = self.value_dict[type]['day']
        workloads_dict['night'] = self.value_dict[type]['night']
        workloads_dict['weekends'] = self.value_dict[type]['weekends']

        return workloads_dict


    def calculate_machines_scarcity(self, type, avg_day_files, avg_night_files, avg_weekends_files, new_users_number): #type = plan or fact
        scarcity_key = type + '_scarcity'

        if type not in self.value_dict:
            self.calculate_workloads(type, avg_day_files, avg_night_files, avg_weekends_files, new_users_number)
        
        self.value_dict['day_180hour'][scarcity_key] = '-'
        machine_168hour = self.value_dict['day_168hour']
        machine_79hour = self.value_dict['day_79hour']
        if self.value_dict[type]['day'] <= 0.86:
            machine_168hour[scarcity_key] = 0
            machine_79hour[scarcity_key] = 0
        else:
            key = 'max_files'
            day_files = self.value_dict['day_180hour'][key] + self.value_dict['day_168hour'][key] + self.value_dict['day_79hour'][key]
            machine_168hour[scarcity_key] = round(day_files * (self.value_dict[type]['day'] - 0.86) / 0.86 / machine_168hour['month_files'])

            new_workload = avg_day_files / (day_files +  machine_168hour[scarcity_key] * machine_168hour['month_files'])
            if new_workload <= 0.86:
                machine_79hour[scarcity_key] = 0
            else:
                machine_79hour[scarcity_key] = 1
        
        night_machine = self.value_dict['night']
        if self.value_dict[type]['night'] <= 0.86:
            night_machine[scarcity_key] = 0
        else:
            night_machine[scarcity_key] = math.ceil(night_machine['max_files'] * (self.value_dict[type]['night'] - 0.86) / 0.86 / night_machine['month_files'])
        
        weekends_machine = self.value_dict['weekends']
        if self.value_dict[type]['weekends'] <= 0.86:
            weekends_machine[scarcity_key] = 0
        else:
            weekends_machine[scarcity_key] = math.ceil(weekends_machine['max_files'] * (self.value_dict[type]['weekends'] - 0.86) / 0.86 / weekends_machine['month_files'])
        
        need_night_machines = max(night_machine[scarcity_key], weekends_machine[scarcity_key])
        night_machine[scarcity_key] = need_night_machines
        weekends_machine[scarcity_key] = need_night_machines
        
    
    def get_machines_scarcity(self, type, avg_day_files, avg_night_files, avg_weekends_files, new_users_number): #type = plan or fact
        scarcities_dict = dict()
        scarcity_key = type + '_scarcity'

        if scarcity_key not in self.value_dict['day_168hour']:
            self.calculate_machines_scarcity(type, avg_day_files, avg_night_files, avg_weekends_files, new_users_number)
        
        for name in Machine.names:
            scarcities_dict[name] = self.value_dict[name][scarcity_key]
        
        return scarcities_dict



# check
calc = Calculator(2, 3, 3, 2)
print(calc.get_machines_scarcity('fact', 6539, 1143, 833, 600))
calc.set_new_machines_numbers(2, 4, 3, 2)
print(calc.get_machines_scarcity('fact', 6539, 1143, 833, 600))
print()