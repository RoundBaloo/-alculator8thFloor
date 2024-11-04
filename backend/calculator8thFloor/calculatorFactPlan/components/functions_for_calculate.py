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
    day_machine_180hour = Machine('180h_day', 11, 15, 8)
    day_machine_168hour = Machine('168h', 8, 20, 8)
    day_machine_79hour = Machine('79h', 4, 20, 8)
    weekends_machine = Machine('180h_weekend', 11, 15, 6)
    night_machine = Machine('180h_night', 11, 15, 6)

    # kwargs - словарь, где по названию машины содержится их кол-во
    def __init__(self, kwargs):
        self.value_dict = dict()
        self.set_new_machines_numbers(kwargs)

    def set_new_machines_numbers(self, kwargs):
        self.value_dict.clear()
        key = 'number'

        self.calculate_machines_month_files()

        self.value_dict['180h_day'][key] = kwargs['180h']
        self.value_dict['168h'][key] = kwargs['168h']
        self.value_dict['79h'][key] = kwargs['79h']
        self.value_dict['180h_night'][key] = kwargs['180h']
        self.value_dict['180h_weekend'][key] = kwargs['180h']

    def calc_scarcity(self, machine_name, workload, files_number):
        machine = self.value_dict[machine_name]

        if workload <= 0.86:
            return 0
        else:
            need_add_files = files_number * (workload - 0.86) / 0.86
            scarcity = need_add_files / machine['month_files']
            return scarcity

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
        day_files = self.value_dict['180h_day'][key] + self.value_dict['168h'][key] + self.value_dict['79h'][key]

        workload['day'] = avg_day_files / day_files
        workload['180h_night'] = avg_night_files / self.value_dict['180h_night'][key]
        workload['180h_weekend'] = avg_weekends_files / self.value_dict['180h_weekend'][key]


    def get_workloads(self, type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number):  # type = plan or fact
        workloads_dict = dict()
        if type not in self.value_dict:
            self.calculate_workloads(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)

        workloads_dict['180h_day'] = self.value_dict[type]['day']
        workloads_dict['168h'] = self.value_dict[type]['day']
        workloads_dict['79h'] = self.value_dict[type]['day']
        workloads_dict['180h_night'] = self.value_dict[type]['180h_night']
        workloads_dict['180h_weekend'] = self.value_dict[type]['180h_weekend']

        return workloads_dict

    def calculate_machines_scarcity(self, type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number):  # type = plan or fact
        if type not in self.value_dict:
            self.calculate_workloads(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)
        workload = self.value_dict[type]
        scarcity_key = type + '_scarcity'

        night_machine = self.value_dict['180h_night']
        weekends_machine = self.value_dict['180h_weekend']
        machine_180hour = self.value_dict['180h_day']
        machine_168hour = self.value_dict['168h']
        machine_79hour = self.value_dict['79h']

        night_scarcity = math.ceil(self.calc_scarcity('180h_night', workload['180h_night'], night_machine['max_files']))
        weekends_scarcity = math.ceil(self.calc_scarcity('180h_weekend', workload['180h_weekend'], weekends_machine['max_files']))
        need_180hour_machines = max(night_scarcity, weekends_scarcity)

        weekends_machine[scarcity_key] = need_180hour_machines
        night_machine[scarcity_key] = need_180hour_machines
        machine_180hour[scarcity_key] = need_180hour_machines

        key = 'max_files'
        day_files = machine_180hour[key] + machine_168hour[key] + machine_79hour[key]

        new_add_files1 = machine_180hour[scarcity_key] * machine_180hour['month_files']
        new_day_workload1 = avg_day_files / (day_files + new_add_files1)
        machine_168hour[scarcity_key] = round(self.calc_scarcity('168h', new_day_workload1, day_files))

        new_add_files2 = machine_168hour[scarcity_key] * machine_168hour['month_files']
        new_day_workload2 = avg_day_files / (day_files + new_add_files1 + new_add_files2)
        if new_day_workload2 <= 0.86:
            machine_79hour[scarcity_key] = 0
        else:
            machine_79hour[scarcity_key] = 1

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
    '180h': 1,
    '168h': 4,
    '79h': 4
}

calc = Calculator(machines_numbers_dict1)
print(calc.get_machines_scarcity('fact', 6539, 1143, 833, 600))
machines_numbers_dict2 = {
    '180h': 2,
    '168h': 3,
    '79h': 6
}
calc.set_new_machines_numbers(machines_numbers_dict2)
print(calc.get_machines_scarcity('fact', 6539, 1143, 833, 600))
print(calc.get_workloads('fact', 6539, 1143, 833, 600))
print('a')
