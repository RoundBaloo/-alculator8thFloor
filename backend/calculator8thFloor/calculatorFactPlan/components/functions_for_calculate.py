import math


class Machines_info:
    """
    Класс, который содержит имена машин и количество файлов, которые
    каждая машина может обработать за месяц.
    """
    # Список имен машин
    names: list = []
    # Словарь, где ключи - имена машин, а значения - количество файлов за месяц
    files_in_a_month: dict = dict()
    # Константа для преобразования часов в минуты
    minutes_in_hour = 50

    def add_machine_info(self, name, hours_in_day, days_in_month, productivity):
        """
        Добавляет имя машины в names и рассчитывает и добавляет
        количество файлов за месяц в files_in_a_month

        Args:
            name (str): имя машины
            hours_in_day (int): часы работы в день
            days_in_month (int): дни работы в месяц
            productivity (int): время, необходимое для создания одного файла
        """
        Machines_info.names.append(name)
        minutes_in_day = hours_in_day * Machines_info.minutes_in_hour
        files_in_a_day = round(minutes_in_day / productivity * 0.85)
        Machines_info.files_in_a_month[name] = days_in_month * files_in_a_day


class Calculator:
    """
    Класс, который выполняет все расчеты, связанные с машинами.
    """
    # Инициализируем машины с их параметрами
    machines_info = Machines_info()

    def __init__(self, kwargs):
        """
        Инициализирует калькулятор с данными о количестве каждой машины.

        Args:
            kwargs (dict): словарь, где ключи - имена машин, а значения - количества машин
        """
        Calculator.machines_info.add_machine_info('180h_day', 11, 15, 8)
        Calculator.machines_info.add_machine_info('168h', 8, 20, 8)
        Calculator.machines_info.add_machine_info('79h', 4, 20, 8)
        Calculator.machines_info.add_machine_info('180h_weekend', 11, 15, 6)
        Calculator.machines_info.add_machine_info('180h_night', 11, 15, 6)

        # Словарь, в котором хранится информация о машинах и их файлах в месяц
        self.value_dict = dict()
        self.set_new_machines_numbers(kwargs)  # Устанавливаем количество машин

    def set_new_machines_numbers(self, kwargs):
        """
        Обновляет количество машин и количество файлов в месяц в value_dict.

        Args:
            kwargs (dict): словарь, где ключи - имена машин, а значения - количества машин
        """
        self.value_dict.clear()

        self.calculate_machines_month_files()

        # Сохраняем количество каждой машины в словаре
        key = 'number'

        self.value_dict['180h_day'][key] = kwargs['180h']
        self.value_dict['168h'][key] = kwargs['168h']
        self.value_dict['79h'][key] = kwargs['79h']
        self.value_dict['180h_night'][key] = kwargs['180h']
        self.value_dict['180h_weekend'][key] = kwargs['180h']

    def calculate_machines_month_files(self):
        """
        Заполняет value_dict количеством файлов, которые
        каждая машина обрабатывает за месяц.
        """
        key = 'month_files'
        for name in Machines_info.names:
            # Инициализируем пустой словарь для каждой машины
            self.value_dict[name] = dict()
            self.value_dict[name][key] = Machines_info.files_in_a_month[name]

    def get_machines_month_files(self):
        """
        Получает количество файлов за месяц для каждой машины из value_dict.

        Returns:
            dict: словарь с ключами-именами машин и значениями - количеством файлов за месяц
        """
        month_files_dict = dict()
        key = 'month_files'

        for name in Machines_info.names:
            month_files_dict[name] = self.value_dict[name][key]

        return month_files_dict

    def calculate_machines_max_files(self):
        """
        Рассчитывает и заполняет value_dict количеством файлов, которые каждая
        машина обрабатывает за месяц.
        """
        key = 'max_files'

        for name in Machines_info.names:
            machine = self.value_dict[name]
            machine[key] = machine['month_files'] * machine['number']

    def get_machines_max_files(self):
        """
        Получает максимальное кол-во файлов, которые могут быть
        обработаны за месяц для каждой машины.

        Returns:
            dict: словарь с ключами-именами машин и значениями - максимальным количеством файлов
        """
        max_files_dict = dict()
        key = 'max_files'

        # Проверяем, нужно ли произвести расчет max_files
        if key not in self.value_dict[Machines_info.names[0]]:
            self.calculate_machines_max_files()

        for name in Machines_info.names:
            max_files_dict[name] = self.value_dict[name][key]

        return max_files_dict

    def calc_new_users_files(self, new_users_number):
        """
        Рассчитывает и заполняет value_dict количеством новых файлов, которые
        появятся для каждой машины в связи с новыми пользователями.

        Args:
            new_users_number (int): количество новых пользователей
        """
        self.value_dict['new_users_files'] = dict()
        new_users_files = self.value_dict['new_users_files']

        # Рассчитываем кол-во файлов для разных машин и добавляем их в словарь
        all_files = round(new_users_number * 1.3)
        new_users_files['night'] = round(new_users_number * 1.3 * 0.27)
        new_users_files['weekend'] = round(new_users_number * 1.3 * 0.15)
        # Остальные файлы для дня
        new_users_files['day'] = all_files - new_users_files['night'] - new_users_files['weekend']

    def get_new_users_files(self, new_users_number):
        """
        Получает количество файлов новых пользователей для каждой машины.

        Args:
            new_users_number (int): количество новых пользователей

        Returns:
            dict: словарь с ключами-именами машин и значениями - кол-вом
            файлов новых пользователей для каждой машины
        """
        new_users_files_dict = dict()

        # Проверяем, нужно ли произвести расчет new_users_files
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
        self, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number
    ):
        """
        Рассчитывает и заполняет value_dict новым средним кол-вом файлов
        после добавления новых пользователей.

        Args:
            avg_day_files (int): среднее количество дневных файлов
            avg_weekends_files (int): среднее количество файлов выходного дня
            avg_night_files (int): среднее количество ночных файлов
            new_users_number (int): количество новых пользователей
        """
        self.value_dict['new_avg_files'] = dict()
        new_avg_files = self.value_dict['new_avg_files']

        # Проверяем, нужно ли произвести расчет new_users_files
        if 'new_users_files' not in self.value_dict:
            self.calc_new_users_files(new_users_number)

        new_users_files = self.value_dict['new_users_files']

        # Рассчитываем новое среднее количество файлов для каждого типа машин
        new_avg_files['day'] = avg_day_files + new_users_files['day']
        new_avg_files['weekend'] = avg_weekends_files + new_users_files['weekend']
        new_avg_files['night'] = avg_night_files + new_users_files['night']

    def get_new_avg_files(
        self, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number
    ):
        """
        Получает новое среднее количество файлов для каждой машины.

        Args:
            avg_day_files (int): среднее количество дневных файлов
            avg_weekends_files (int): среднее количество файлов выходного дня
            avg_night_files (int): среднее количество ночных файлов
            new_users_number (int): количество новых пользователей

        Returns:
            dict: словарь с новыми средними кол-вами файлов для каждой машины
        """
        new_avg_files_dict = dict()

        # Проверяем, нужно ли произвести расчет new_avg_files
        if 'new_avg_files' not in self.value_dict:
            self.calc_new_avg_files(
                avg_day_files, avg_weekends_files,
                avg_night_files, new_users_number
                )

        new_avg_files = self.value_dict['new_avg_files']

        new_avg_files_dict['180h_day'] = new_avg_files['day']
        new_avg_files_dict['168h'] = new_avg_files['day']
        new_avg_files_dict['79h'] = new_avg_files['day']
        new_avg_files_dict['180h_night'] = new_avg_files['night']
        new_avg_files_dict['180h_weekend'] = new_avg_files['weekend']

        return new_avg_files_dict

    def calculate_workloads(
        self, type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number
    ):
        """
        Рассчитывает нагрузку для каждой машины.

        Args:
            type (str): тип ('plan' или 'fact')
            avg_day_files (int): среднее количество дневных файлов
            avg_weekends_files (int): среднее количество файлов выходного дня
            avg_night_files (int): среднее количество ночных файлов
            new_users_number (int): количество новых пользователей
        """
        self.value_dict[type] = dict()
        workload = self.value_dict[type]

        # Проверяем, нужно ли произвести расчет max_files
        if 'max_files' not in self.value_dict[Machines_info.names[0]]:
            self.calculate_machines_max_files()

        if type == 'plan':
            # Проверяем, нужно ли произвести расчет new_avg_files
            if 'new_avg_files' not in self.value_dict:
                self.calc_new_avg_files(avg_day_files, avg_weekends_files,
                                        avg_night_files, new_users_number)

            new_avg_files = self.value_dict['new_avg_files']

            # Используем новые средние значения
            avg_night_files = new_avg_files['night']
            avg_weekends_files = new_avg_files['weekend']
            avg_day_files = new_avg_files['day']

        key = 'max_files'

        # Общее кол-во файлов, производимых дневными машинами
        day_files = self.value_dict['180h_day'][key] + self.value_dict['168h'][key] + self.value_dict['79h'][key]

        # Рассчитываем нагрузку для каждого типа машин
        workload['day'] = avg_day_files / day_files
        workload['180h_night'] = avg_night_files / self.value_dict['180h_night'][key]
        workload['180h_weekend'] = avg_weekends_files / self.value_dict['180h_weekend'][key]

    def get_workloads(
        self, type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number
    ):
        """
        Получает нагрузку для каждой машины.

        Args:
            type (str): тип ('plan' или 'fact')
            avg_day_files (int): среднее количество дневных файлов
            avg_weekends_files (int): среднее количество файлов выходного дня
            avg_night_files (int): среднее количество ночных файлов
            new_users_number (int): количество новых пользователей

        Returns:
            dict: словарь с ключами-именами машин и значениями - нагрузкой в процентах
        """
        workloads_dict = dict()
        # Проверяем, нужно ли произвести расчет нагрузки
        if type not in self.value_dict:
            self.calculate_workloads(type, avg_day_files, avg_weekends_files,
                                     avg_night_files, new_users_number)

        workload = self.value_dict[type]

        workloads_dict['180h_day'] = round(workload['day'] * 100)
        workloads_dict['168h'] = round(workload['day'] * 100)
        workloads_dict['79h'] = round(workload['day'] * 100)
        workloads_dict['180h_night'] = round(workload['180h_night'] * 100)
        workloads_dict['180h_weekend'] = round(workload['180h_weekend'] * 100)

        return workloads_dict

    def calc_scarcity(
        self, machine_name, workload, files_number, need_workload
    ):
        """
        Рассчитывает нехватку для одного типа машины.

        Args:
            machine_name (str): имя машины
            workload (int): Нагрузка, которая должна быть у этого типа машины
            files_number (int): общее количество файлов, которое машина должна обработать
            need_workload (int): необходимая Нагрузка

        Returns:
            float: неокругленная нехватка для этого типа машин
        """
        machine = self.value_dict[machine_name]

        # Если Нагрузка не превышает необходимую, нехватка равна 0
        if workload <= need_workload:
            return 0
        else:
            # Рассчитываем, сколько дополнительных файлов необходимо, чтобы
            # нагрузка приблизилась к необходимой
            need_add_files = files_number * (workload - need_workload) / need_workload
            # Округляется при получении в методе
            scarcity = need_add_files / machine['month_files']
            return scarcity

    def calculate_machines_scarcity(
        self, type, avg_day_files, avg_weekends_files, avg_night_files,
        new_users_number, need_workload
    ):
        """
        Рассчитывает нехватку машин на основе заданных параметров.

        Args:
            type (str): тип ('plan' или 'fact')
            avg_day_files (int): среднее количество дневных файлов
            avg_weekends_files (int): среднее количество файлов выходного дня
            avg_night_files (int): среднее количество ночных файлов
            new_users_number (int): количество новых пользователей
            need_workload (float): необходимая Нагрузка
        """
        # Проверяем, нужно ли произвести расчет нагрузки
        if type not in self.value_dict:
            self.calculate_workloads(type, avg_day_files, avg_weekends_files,
                                     avg_night_files, new_users_number)

        workload = self.value_dict[type]
        # Ключ для нехватки машин
        scarcity_key = type + '_scarcity'

        # Получаем информацию о машинах из словаря
        night_machine = self.value_dict['180h_night']
        weekends_machine = self.value_dict['180h_weekend']
        machine_180hour = self.value_dict['180h_day']
        machine_168hour = self.value_dict['168h']
        machine_79hour = self.value_dict['79h']

        # Вычисляем нехватку для машин ночного и выходного типа
        night_scarcity = math.ceil(self.calc_scarcity(
            '180h_night', workload['180h_night'],
            night_machine['max_files'], need_workload
        ))
        weekends_scarcity = math.ceil(self.calc_scarcity(
            '180h_weekend', workload['180h_weekend'],
            weekends_machine['max_files'], need_workload
        ))
        # Определяем, сколько машин 180 часов необходимо
        need_180hour_machines = max(night_scarcity, weekends_scarcity)

        # Сохраняем нехватку для соответствующих машин
        weekends_machine[scarcity_key] = need_180hour_machines
        night_machine[scarcity_key] = need_180hour_machines
        machine_180hour[scarcity_key] = need_180hour_machines

        key = 'max_files'
        # Общее кол-во файлов, производимых дневными машинами
        day_files = machine_180hour[key] + machine_168hour[key] + machine_79hour[key]

        # Рассчитываем нехватку для машин 168 часов
        # Сколько файлов добавится, если добавить нехватащие машины 180ч/день
        new_add_files1 = machine_180hour[scarcity_key] * machine_180hour['month_files']
        # Новая нагрузка на дневные машины при добавлении нехватащих машин 180ч/день
        new_day_workload1 = avg_day_files / (day_files + new_add_files1)
        # Вычисляем и записываем нехватку машин 168ч/день
        machine_168hour[scarcity_key] = round(self.calc_scarcity(
            '168h', new_day_workload1, day_files, need_workload
        ))

        # Рассчитываем нехватку для машин 79 часов
        # Сколько файлов добавится, если добавить нехватащие машины 168ч/день
        new_add_files2 = machine_168hour[scarcity_key] * machine_168hour['month_files']
        # Новая нагрузка на дневные машины при добавлении нехватащих машин 168ч/день
        new_day_workload2 = avg_day_files / (day_files + new_add_files1 + new_add_files2)

        # Так как мы по максимуму заполняли нагрузку с помощью машин 168ч/день,
        # то теперь нам либо хватает машин 79ч/день, либо не хватает одной
        if new_day_workload2 <= need_workload:
            machine_79hour[scarcity_key] = 0
        else:
            machine_79hour[scarcity_key] = 1

    def get_machines_scarcity(
        self, type, avg_day_files, avg_weekends_files, avg_night_files,
        new_users_number, need_workload=0.86
    ):
        """
        Получает нехватку для машин.

        Args:
            type (str): тип ('plan' или 'fact')
            avg_day_files (int): среднее количество дневных файлов
            avg_weekends_files (int): среднее количество файлов выходного дня
            avg_night_files (int): среднее количество ночных файлов
            new_users_number (int): количество новых пользователей
            need_workload (float): необходимая Нагрузка

        Returns:
            dict: словарь с нехваткой для каждой машины
        """
        scarcities_dict = dict()
        # Ключ для нехватки машин
        scarcity_key = type + '_scarcity'

        # Проверяем, нужно ли произвести расчет нехватки
        if scarcity_key not in self.value_dict[Machines_info.names[1]]:
            self.calculate_machines_scarcity(
                type, avg_day_files, avg_weekends_files, avg_night_files,
                new_users_number, need_workload
            )

        for name in Machines_info.names:
            scarcities_dict[name] = self.value_dict[name][scarcity_key]

        return scarcities_dict
