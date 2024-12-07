import pytest
from functions_for_calculate import Calculator


@pytest.fixture
def setup_calculator():
    kwargs = {'180h': 2, '168h': 3, '79h': 1}  # Пример количества машин
    calculator = Calculator(kwargs)
    return calculator


def test_get_machines_month_files(setup_calculator):
    """
    Проверка функции get_machines_month_files

    Args:
        setup_calculator (func): инициализатор калькулятора с определенными аргументами
    """
    calculator = setup_calculator
    expected = {
        '180h_day': 870,
        '168h': 840,
        '79h': 420,
        '180h_night': 1170,
        '180h_weekend': 1170
    }
    result = calculator.get_machines_month_files()
    assert result == expected


def test_get_machines_max_files(setup_calculator):
    """
    Проверка функции get_machines_max_files

    Args:
        setup_calculator (func): инициализатор калькулятора с определенными аргументами
    """
    calculator = setup_calculator
    expected = {
        '180h_day': 1740,
        '168h': 2520,
        '79h': 420,
        '180h_night': 2340,
        '180h_weekend': 2340
    }
    result = calculator.get_machines_max_files()
    assert result == expected


def test_get_new_users_files(setup_calculator):
    """
    Проверка функции get_new_users_files

    Args:
        setup_calculator (func): инициализатор калькулятора с определенными аргументами
    """
    calculator = setup_calculator
    new_users_number = 6000
    expected = {
        '180h_day': 4524,
        '168h': 4524,
        '79h': 4524,
        '180h_night': 2106,
        '180h_weekend': 1170
    }
    result = calculator.get_new_users_files(new_users_number)
    assert result == expected


def test_get_new_avg_files(setup_calculator):
    """
    Проверка функции get_new_avg_files

    Args:
        setup_calculator (func): инициализатор калькулятора с определенными аргументами
    """
    calculator = setup_calculator
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    calculator.calc_new_avg_files(avg_day_files, avg_weekends_files, avg_night_files, new_users_number)

    expected = {
        '180h_day': 10524,
        '168h': 10524,
        '79h': 10524,
        '180h_night': 5106,
        '180h_weekend': 3170
    }

    result = calculator.get_new_avg_files(avg_day_files, avg_weekends_files, avg_night_files, new_users_number)
    assert result == expected


def test_get_fact_workloads(setup_calculator):
    """
    Проверка функции get_workloads для расчета ФАКТа

    Args:
        setup_calculator (func): инициализатор калькулятора с определенными аргументами
    """
    calculator = setup_calculator
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    type = 'fact'
    calculator.calculate_workloads(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)

    expected = {
        '180h_day': 128,
        '168h': 128,
        '79h': 128,
        '180h_night': 128,
        '180h_weekend': 85
    }

    result = calculator.get_workloads(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)
    assert result == expected


def test_get_plan_workloads(setup_calculator):
    """
    Проверка функции get_workloads для расчета ПЛАНа

    Args:
        setup_calculator (func): инициализатор калькулятора с определенными аргументами
    """
    calculator = setup_calculator
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    type = 'plan'
    calculator.calculate_workloads(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)

    expected = {
        '180h_day': 225,
        '168h': 225,
        '79h': 225,
        '180h_night': 218,
        '180h_weekend': 135
    }

    result = calculator.get_workloads(type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number)
    assert result == expected


def test_get_fact_machines_scarcity(setup_calculator):
    """
    Проверка функции get_machines_scarcity для расчета ФАКТа

    Args:
        setup_calculator (func): инициализатор калькулятора с определенными аргументами
    """
    calculator = setup_calculator
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    type = 'fact'
    need_workload = 0.86

    expected = {
        '180h_day': 1,
        '168h': 1,
        '79h': 1,
        '180h_night': 1,
        '180h_weekend': 1
    }

    result = calculator.get_machines_scarcity(
        type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number, need_workload
        )
    assert result == expected


def test_get_plan_machines_scarcity(setup_calculator):
    """
    Проверка функции get_machines_scarcity для расчета ПЛАНа

    Args:
        setup_calculator (func): инициализатор калькулятора с определенными аргументами
    """
    calculator = setup_calculator
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    type = 'plan'
    need_workload = 0.86

    expected = {
        '180h_day': 4,
        '168h': 0,
        '79h': 0,
        '180h_night': 4,
        '180h_weekend': 4
    }

    result = calculator.get_machines_scarcity(
        type, avg_day_files, avg_weekends_files, avg_night_files, new_users_number, need_workload
        )
    assert result == expected
