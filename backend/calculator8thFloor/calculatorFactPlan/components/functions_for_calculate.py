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

    def calc_scarcity(self, machine_name, workload, files_number, need_workload):
        machine = self.value_dict[machine_name]

        if workload <= need_workload:
            return 0
        else:
            need_add_files = files_number * (workload - need_workload) / need_workload
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

    def calc_new_users_files(self, new_users_number):
        self.value_dict['new_users_files'] = dict()
        new_users_files = self.value_dict['new_users_files']

        new_users_files['night'] = round(new_users_number * 1.3 * 0.27)
        new_users_files['weekend'] = round(new_users_number * 1.3 * 0.15)
        new_users_files['day'] = round(new_users_number * 1.3) - new_users_files['night'] - new_users_files['weekend']

    def get_new_users_files(self, new_users_number):
        new_users_files_dict = dict()

        if 'new_users_files' not in self.value_dict:
            self.calc_new_users_files(new_users_number)

        new_users_files = self.value_dict['new_users_files']

        new_users_files_dict['180h_day'] = new_users_files['day']
        new_users_files_dict['168h'] = new_users_files['day']
        new_users_files_dict['79h'] = new_users_files['day']
        new_users_files_dict['180h_night'] = new_users_files['night']
        new_users_files_dict['180h_weekend'] = new_users_files['weekend']

        return new_users_files_dict

    def calc_new_avg_files(
        self,
        avg_day_files, avg_weekends_files, avg_night_files,
        new_users_number
    ):
        self.value_dict['new_avg_files'] = dict()
        new_avg_files = self.value_dict['new_avg_files']

        if 'new_users_files' not in self.value_dict:
            self.calc_new_users_files(new_users_number)

        new_users_files = self.value_dict['new_users_files']

        new_avg_files['day'] = avg_day_files + new_users_files['day']
        new_avg_files['weekend'] = avg_weekends_files + new_users_files['weekend']
        new_avg_files['night'] = avg_night_files + new_users_files['night']

    def get_new_avg_files(
        self,
        avg_day_files, avg_weekends_files, avg_night_files,
        new_users_number
    ):
        new_avg_files_dict = dict()

        if 'new_avg_files' not in self.value_dict:
            self.calc_new_avg_files(
                avg_day_files, avg_weekends_files, avg_night_files,
                new_users_number
            )

        new_avg_files = self.value_dict['new_avg_files']

        new_avg_files_dict['180h_day'] = new_avg_files['day']
        new_avg_files_dict['168h'] = new_avg_files['day']
        new_avg_files_dict['79h'] = new_avg_files['day']
        new_avg_files_dict['180h_night'] = new_avg_files['night']
        new_avg_files_dict['180h_weekend'] = new_avg_files['weekend']

        return new_avg_files_dict

    def calculate_workloads(
        self, type,
        avg_day_files, avg_weekends_files, avg_night_files,
        new_users_number
    ):  # type = plan or fact
        self.value_dict[type] = dict()
        workload = self.value_dict[type]

        if 'max_files' not in self.value_dict[Machine.names[0]]:
            self.calculate_machines_max_files()

        if type == 'plan':
            if 'new_avg_files' not in self.value_dict:
                self.calc_new_avg_files(
                    avg_day_files, avg_weekends_files, avg_night_files,
                    new_users_number
                )

            new_avg_files = self.value_dict['new_avg_files']

            avg_night_files = new_avg_files['night']
            avg_weekends_files = new_avg_files['weekend']
            avg_day_files = new_avg_files['day']

        key = 'max_files'
        day_files = self.value_dict['180h_day'][key] + self.value_dict['168h'][key] + self.value_dict['79h'][key]

        workload['day'] = avg_day_files / day_files
        workload['180h_night'] = avg_night_files / self.value_dict['180h_night'][key]
        workload['180h_weekend'] = avg_weekends_files / self.value_dict['180h_weekend'][key]

    def get_workloads(
        self, type,
        avg_day_files, avg_weekends_files, avg_night_files,
        new_users_number
    ):  # type = plan or fact
        workloads_dict = dict()
        if type not in self.value_dict:
            self.calculate_workloads(
                type,
                avg_day_files, avg_weekends_files, avg_night_files,
                new_users_number
            )

        workloads_dict['180h_day'] = self.value_dict[type]['day'] * 100
        workloads_dict['168h'] = self.value_dict[type]['day'] * 100
        workloads_dict['79h'] = self.value_dict[type]['day'] * 100
        workloads_dict['180h_night'] = self.value_dict[type]['180h_night'] * 100
        workloads_dict['180h_weekend'] = self.value_dict[type]['180h_weekend'] * 100

        return workloads_dict

    def calculate_machines_scarcity(
        self, type,
        avg_day_files, avg_weekends_files, avg_night_files,
        new_users_number, need_workload
    ):  # type = plan or fact
        if type not in self.value_dict:
            self.calculate_workloads(
                type,
                avg_day_files, avg_weekends_files, avg_night_files,
                new_users_number
            )
        workload = self.value_dict[type]
        scarcity_key = type + '_scarcity'

        night_machine = self.value_dict['180h_night']
        weekends_machine = self.value_dict['180h_weekend']
        machine_180hour = self.value_dict['180h_day']
        machine_168hour = self.value_dict['168h']
        machine_79hour = self.value_dict['79h']

        night_scarcity = math.ceil(self.calc_scarcity(
            '180h_night', workload['180h_night'],
            night_machine['max_files'], need_workload
        ))
        weekends_scarcity = math.ceil(self.calc_scarcity(
            '180h_weekend', workload['180h_weekend'],
            weekends_machine['max_files'], need_workload
        ))
        need_180hour_machines = max(night_scarcity, weekends_scarcity)

        weekends_machine[scarcity_key] = need_180hour_machines
        night_machine[scarcity_key] = need_180hour_machines
        machine_180hour[scarcity_key] = need_180hour_machines

        key = 'max_files'
        day_files = machine_180hour[key] + machine_168hour[key] + machine_79hour[key]

        new_add_files1 = machine_180hour[scarcity_key] * machine_180hour['month_files']
        new_day_workload1 = avg_day_files / (day_files + new_add_files1)
        machine_168hour[scarcity_key] = round(self.calc_scarcity(
            '168h', new_day_workload1, day_files, need_workload
        ))

        new_add_files2 = machine_168hour[scarcity_key] * machine_168hour['month_files']
        new_day_workload2 = avg_day_files / (day_files + new_add_files1 + new_add_files2)
        if new_day_workload2 <= need_workload:
            machine_79hour[scarcity_key] = 0
        else:
            machine_79hour[scarcity_key] = 1

    def get_machines_scarcity(
        self, type,
        avg_day_files, avg_weekends_files, avg_night_files,
        new_users_number, need_workload=0.86
    ):  # type = plan or fact.
        scarcities_dict = dict()
        scarcity_key = type + '_scarcity'

        if scarcity_key not in self.value_dict[Machine.names[1]]:
            self.calculate_machines_scarcity(
                type,
                avg_day_files, avg_weekends_files, avg_night_files,
                new_users_number, need_workload
            )

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
    '168h': 4,
    '79h': 4
}
calc.set_new_machines_numbers(machines_numbers_dict2)
print(calc.get_machines_scarcity('fact', 6539, 1143, 833, 600, 0.5))
print(calc.get_workloads('fact', 6539, 1143, 833, 600))
print('a')
