import math


class Machine:
    names: list = []
    files_in_a_month: dict = dict()
    minutes_in_hour = 50

    def __init__(self, name, hours_in_day, days_in_month, productivity):
        Machine.names.append(name)
        minutes_in_day = hours_in_day * Machine.minutes_in_hour
        files_in_a_day = round(minutes_in_day / productivity * 0.85)
        Machine.files_in_a_month[name] = days_in_month * files_in_a_day


class Calculator:
    value_dict: dict = dict()

    day_machine_180hour = Machine('day_180hour', 11, 15, 8)
    day_machine_168hour = Machine('day_168hour', 8, 20, 8)
    day_machine_79hour = Machine('day_79hour', 4, 20, 8)
    weekends_machine = Machine('weekends', 11, 15, 6)
    night_machine = Machine('night', 11, 15, 6)

    # kwargs - словарь, где по названию машины содержится их кол-во
    def __init__(self, kwargs):
        self.set_new_machines_numbers(kwargs)

    def set_new_machines_numbers(self, kwargs):
        self.value_dict.clear()
        key = 'number'

        self.calculate_machines_month_files()

        self.value_dict['day_180hour'][key] = kwargs['day_180hour']
        self.value_dict['day_168hour'][key] = kwargs['day_168hour']
        self.value_dict['day_79hour'][key] = kwargs['day_79hour']
        self.value_dict['night'][key] = kwargs['night']
        self.value_dict['weekends'][key] = kwargs['night']

    def calculate_machines_month_files(self):
        key = 'month_files'
        for name in Machine.names:
            self.value_dict[name] = dict()
            self.value_dict[name][key] = Machine.files_in_a_month[name]

    def get_machines_month_files(self):
        month_files_dict = dict()
        key = 'month_files'

        for name in Machine.names:
            month_files_dict[name] = self.value_dict[name][key]

        return month_files_dict

    def calculate_machines_max_files(self):
        key = 'max_files'

        for name in Machine.names:
            machine = self.value_dict[name]
            machine[key] = machine['month_files'] * machine['number']

    def get_machines_max_files(self):
        max_files_dict = dict()
        key = 'max_files'

        if key not in self.value_dict[Machine.names[0]]:
            self.calculate_machines_max_files()

        for name in Machine.names:
            max_files_dict[name] = self.value_dict[name][key]

        return max_files_dict

    def calculate_workloads(self, type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number):  # type = plan or fact
        self.value_dict[type] = dict()
        workload = self.value_dict[type]

        if 'max_files' not in self.value_dict[Machine.names[0]]:
            self.calculate_machines_max_files()

        if type == 'plan':
            new_night_files = round(new_users_number * 1.3 * 0.27)
            avg_night_files += new_night_files

            new_weekends_files = round(new_users_number * 1.3 * 0.15)
            avg_weekends_files += new_weekends_files

            new_day_files = round(new_users_number * 1.3) - new_night_files - new_weekends_files
            avg_day_files += new_day_files

        key = 'max_files'
        day_files = self.value_dict['day_180hour'][key] + self.value_dict['day_168hour'][key] + self.value_dict['day_79hour'][key]

        workload['day'] = avg_day_files / day_files
        workload['night'] = avg_night_files / self.value_dict['night'][key]
        workload['weekends'] = avg_weekends_files / self.value_dict['weekends'][key]

    def get_workloads(self, type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number):  # type = plan or fact
        workloads_dict = dict()

        if type not in self.value_dict:
            self.calculate_workloads(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)

        workloads_dict['day_180hour'] = self.value_dict[type]['day']
        workloads_dict['day_168hour'] = self.value_dict[type]['day']
        workloads_dict['day_79hour'] = self.value_dict[type]['day']
        workloads_dict['night'] = self.value_dict[type]['night']
        workloads_dict['weekends'] = self.value_dict[type]['weekends']

        return workloads_dict

    def calculate_machines_scarcity(self, type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number):  # type = plan or fact
        scarcity_key = type + '_scarcity'

        if type not in self.value_dict:
            self.calculate_workloads(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)

        self.value_dict['day_180hour'][scarcity_key] = 0
        machine_168hour = self.value_dict['day_168hour']
        machine_79hour = self.value_dict['day_79hour']
        workload = self.value_dict[type]

        if workload['day'] <= 0.86:
            machine_168hour[scarcity_key] = 0
            machine_79hour[scarcity_key] = 0
        else:
            key = 'max_files'
            day_files = self.value_dict['day_180hour'][key] + machine_168hour[key] + machine_79hour[key]
            need_files = day_files * (workload['day'] - 0.86) / 0.86
            machine_168hour[scarcity_key] = round(need_files / machine_168hour['month_files'])

            new_add_files = machine_168hour[scarcity_key] * machine_168hour['month_files']
            new_workload = avg_day_files / (day_files + new_add_files)
            if new_workload <= 0.86:
                machine_79hour[scarcity_key] = 0
            else:
                machine_79hour[scarcity_key] = 1

        night_machine = self.value_dict['night']
        if workload['night'] <= 0.86:
            night_machine[scarcity_key] = 0
        else:
            need_add_files = night_machine['max_files'] * (workload['night'] - 0.86) / 0.86
            night_machine[scarcity_key] = math.ceil(need_add_files / night_machine['month_files'])

        weekends_machine = self.value_dict['weekends']
        if workload['weekends'] <= 0.86:
            weekends_machine[scarcity_key] = 0
        else:
            need_add_files = weekends_machine['max_files'] * (workload['weekends'] - 0.86) / 0.86
            weekends_machine[scarcity_key] = math.ceil(need_add_files / weekends_machine['month_files'])

        need_night_machines = max(night_machine[scarcity_key], weekends_machine[scarcity_key])
        night_machine[scarcity_key] = need_night_machines
        weekends_machine[scarcity_key] = need_night_machines

    def get_machines_scarcity(self, type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number):  # type = plan or fact.
        scarcities_dict = dict()
        scarcity_key = type + '_scarcity'

        if scarcity_key not in self.value_dict[Machine.names[1]]:
            self.calculate_machines_scarcity(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)

        for name in Machine.names:
            scarcities_dict[name] = self.value_dict[name][scarcity_key]

        return scarcities_dict


# check
machines_numbers_dict1 = {
    'day_180hour': 2,
    'day_168hour': 5,
    'day_79hour': 4,
    'night': 2
}

calc = Calculator(machines_numbers_dict1)
# print(calc.get_workloads('fact', 6539, 1143, 833, 600))
machines_numbers_dict2 = {
    'day_180hour': 2,
    'day_168hour': 5,
    'day_79hour': 6,
    'night': 3
}
calc.set_new_machines_numbers(machines_numbers_dict2)
# print(calc.get_workloads('fact', 6539, 1143, 833, 600))
# print('a')
print('180h night'.split())
print('180hnight'.split())