import math


class Machine:
    def __init__(self, hours_in_day, days_in_month, productivity):
        self.hours_in_day = hours_in_day
        self.days_in_month = days_in_month
        self.productivity = productivity


    def calculate_max_month_files_number(self):
        files_in_a_day = round(self.hours_in_day * Calculator.minutes_in_hour / self.productivity * 0.85)
        return files_in_a_day * self.days_in_month


class Calculator:
    minutes_in_hour = 50

    machine_180hour = Machine(11, 15, 8)
    machine_168hour = Machine(8, 20, 8)
    machine_79hour = Machine(4, 20, 8)
    weekends_machine = Machine(11, 15, 6)
    night_machine = Machine(11, 15, 6)


    def __init__(self, number_180hour_machines, number_168hour_machines, number_79hour_machines, number_night_machines):
        self.number_180hour_machines = number_180hour_machines
        self.number_168hour_machines = number_168hour_machines
        self.number_79hour_machines = number_79hour_machines
        self.number_weekends_machines = number_night_machines
        self.number_night_machines = number_night_machines


    def calculate_machines_scarcity(self, workload, files_number, max_month_files):
        if workload < 0.86:
            return 0
        else:
            return files_number * (workload - 0.86) / 0.86 / max_month_files


    def fact_calculate(self, avg_fact_files_number_day, avg_fact_files_number_weekends, avg_fact_files_number_night):
        max_month_files_180hour_machine = self.machine_180hour.calculate_max_month_files_number()
        max_files_180hour_machine = max_month_files_180hour_machine * self.number_180hour_machines

        max_month_files_168hour_machine = self.machine_168hour.calculate_max_month_files_number()
        max_files_168hour_machine = max_month_files_168hour_machine * self.number_168hour_machines

        max_month_files_79hour_machine = self.machine_79hour.calculate_max_month_files_number()
        max_files_79hour_machine = max_month_files_79hour_machine * self.number_79hour_machines
        
        day_files_number = max_files_180hour_machine + max_files_168hour_machine + max_files_79hour_machine
        day_work_diff = day_files_number - avg_fact_files_number_day
        day_workload = avg_fact_files_number_day / day_files_number

        scarcity_168hour_machine = round(self.calculate_machines_scarcity(day_workload, day_files_number, max_month_files_168hour_machine))
        new_day_workload = avg_fact_files_number_day / (day_files_number + scarcity_168hour_machine * max_month_files_168hour_machine)
        scarcity_79hour_machine = 0 if new_day_workload <= 0.86 else 1

        max_month_files_night_machine = self.night_machine.calculate_max_month_files_number()
        max_files_night_machine = max_month_files_night_machine * self.number_night_machines

        night_work_diff = max_files_night_machine - avg_fact_files_number_night
        night_workload = avg_fact_files_number_night / max_files_night_machine
        scarcity_night_machines = math.ceil(self.calculate_machines_scarcity(night_workload, max_files_night_machine, max_month_files_night_machine))

        weekend_work_diff = max_files_night_machine - avg_fact_files_number_weekends
        weekend_workload = avg_fact_files_number_weekends / max_files_night_machine
        scarcity_weekends_machines = math.ceil(self.calculate_machines_scarcity(weekend_workload, max_files_night_machine, max_month_files_night_machine))

        result_night_machines_scarcity = max(scarcity_night_machines, scarcity_weekends_machines)
        return (scarcity_168hour_machine, scarcity_79hour_machine, result_night_machines_scarcity)


    def plan_calculate(self, new_users_number, avg_fact_files_number_day, avg_fact_files_number_weekends, avg_fact_files_number_night):
        new_files_number_night = int(new_users_number * 1.3 * 0.27)
        new_files_number_weekends = int(new_users_number * 1.3 * 0.15)
        new_files_number_day = round(new_users_number * 1.3) - new_files_number_night - new_files_number_weekends

        avg_plan_files_number_night = new_files_number_night + avg_fact_files_number_night
        avg_plan_files_number_weekends = new_files_number_weekends + avg_fact_files_number_weekends
        avg_plan_files_number_day = new_files_number_day + avg_fact_files_number_day

        return self.fact_calculate(avg_plan_files_number_day, avg_plan_files_number_weekends, avg_plan_files_number_night)
#base_check
calc = Calculator(2, 3, 4, 1)
print(calc.fact_calculate(6539, 833, 1143))
print(calc.plan_calculate(600, 6539, 833, 1143))
