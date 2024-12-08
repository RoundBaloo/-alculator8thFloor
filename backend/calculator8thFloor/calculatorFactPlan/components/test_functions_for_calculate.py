import pytest
from functions_for_calculate import Calculator


@pytest.fixture
def calculator1():
    """
    создает калькулятор с первым набором аргументов

    Returns:
        Calculator: калькулятор с первым набором аргументов
    """
    kwargs = {'180h': 2, '168h': 3, '79h': 1}
    calculator = Calculator(kwargs)
    return calculator


@pytest.fixture
def calculator2():
    """
    создает калькулятор со вторым набором аргументов

    Returns:
        Calculator: калькулятор со вторым набором аргументов
    """
    kwargs = {'180h': 5, '168h': 0, '79h': 2}
    calculator = Calculator(kwargs)
    return calculator


def test_get_machines_month_files(calculator1, calculator2):
    """
    Проверка функции get_machines_month_files

    Args:
        calculator1 (func): калькулятор с первым набором аргументов
        calculator2 (func): калькулятор со вторым набором аргументов
    """
    expected = {
        '180h_day': 870,
        '168h': 840,
        '79h': 420,
        '180h_night': 1170,
        '180h_weekend': 1170
    }
    result1 = calculator1.get_machines_month_files()
    assert result1 == expected

    result2 = calculator2.get_machines_month_files()
    assert result2 == expected


def test_get_machines_max_files(calculator1, calculator2):
    """
    Проверка функции get_machines_max_files

    Args:
        calculator1 (func): калькулятор с первым набором аргументов
        calculator2 (func): калькулятор со вторым набором аргументов
    """
    expected1 = {
        '180h_day': 1740,
        '168h': 2520,
        '79h': 420,
        '180h_night': 2340,
        '180h_weekend': 2340
    }
    result1 = calculator1.get_machines_max_files()
    assert result1 == expected1

    expected2 = {
        '180h_day': 4350,
        '168h': 0,
        '79h': 840,
        '180h_weekend': 5850,
        '180h_night': 5850
    }
    result2 = calculator2.get_machines_max_files()
    assert result2 == expected2


def test_get_new_users_files(calculator1, calculator2):
    """
    Проверка функции get_new_users_files

    Args:
        calculator1 (func): калькулятор с первым набором аргументов
        calculator2 (func): калькулятор со вторым набором аргументов
    """
    new_users_number = 6000

    expected = {
        '180h_day': 4524,
        '168h': 4524,
        '79h': 4524,
        '180h_night': 2106,
        '180h_weekend': 1170
    }
    result1 = calculator1.get_new_users_files(new_users_number)
    assert result1 == expected

    result2 = calculator2.get_new_users_files(new_users_number)
    assert result2 == expected


def test_get_new_avg_files(calculator1, calculator2):
    """
    Проверка функции get_new_avg_files

    Args:
        calculator1 (func): калькулятор с первым набором аргументов
        calculator2 (func): калькулятор со вторым набором аргументов
    """
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000

    expected = {
        '180h_day': 10524,
        '168h': 10524,
        '79h': 10524,
        '180h_night': 5106,
        '180h_weekend': 3170
    }
    result1 = calculator1.get_new_avg_files(avg_day_files, avg_weekends_files, avg_night_files, new_users_number)
    assert result1 == expected

    result2 = calculator2.get_new_avg_files(avg_day_files, avg_weekends_files, avg_night_files, new_users_number)
    assert result2 == expected


def test_get_fact_workloads(calculator1, calculator2):
    """
    Проверка функции get_workloads для расчета ФАКТа

    Args:
        calculator1 (func): калькулятор с первым набором аргументов
        calculator2 (func): калькулятор со вторым набором аргументов
    """
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    type = 'fact'

    expected1 = {
        '180h_day': 128,
        '168h': 128,
        '79h': 128,
        '180h_night': 128,
        '180h_weekend': 85
    }
    result1 = calculator1.get_workloads(
        type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number
    )
    assert result1 == expected1

    expected2 = {
        '180h_day': 116,
        '168h': 116,
        '79h': 116,
        '180h_night': 51,
        '180h_weekend': 34
    }
    result2 = calculator2.get_workloads(
        type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number
    )
    assert result2 == expected2


def test_get_plan_workloads(calculator1, calculator2):
    """
    Проверка функции get_workloads для расчета ПЛАНа

    Args:
        calculator1 (func): калькулятор с первым набором аргументов
        calculator2 (func): калькулятор со вторым набором аргументов
    """
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    type = 'plan'

    expected1 = {
        '180h_day': 225,
        '168h': 225,
        '79h': 225,
        '180h_night': 218,
        '180h_weekend': 135
    }
    result1 = calculator1.get_workloads(
        type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number
    )
    assert result1 == expected1

    expected2 = {
        '180h_day': 203,
        '168h': 203,
        '79h': 203,
        '180h_night': 87,
        '180h_weekend': 54
    }
    result2 = calculator2.get_workloads(
        type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number
    )
    assert result2 == expected2


def test_get_fact_machines_scarcity(calculator1, calculator2):
    """
    Проверка функции get_machines_scarcity для расчета ФАКТа

    Args:
        calculator1 (func): калькулятор с первым набором аргументов
        calculator2 (func): калькулятор со вторым набором аргументов
    """
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    type = 'fact'
    need_workload = 0.86

    expected1 = {
        '180h_day': 1,
        '168h': 1,
        '79h': 1,
        '180h_night': 1,
        '180h_weekend': 1
    }
    result1 = calculator1.get_machines_scarcity(
        type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number, need_workload
    )
    assert result1 == expected1

    expected2 = {
        '180h_day': 0,
        '168h': 2,
        '79h': 1,
        '180h_weekend': 0,
        '180h_night': 0
    }
    result2 = calculator2.get_machines_scarcity(
        type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number, need_workload
    )
    assert result2 == expected2


def test_get_plan_machines_scarcity(calculator1, calculator2):
    """
    Проверка функции get_machines_scarcity для расчета ПЛАНа

    Args:
        calculator1 (func): калькулятор с первым набором аргументов
        calculator2 (func): калькулятор со вторым набором аргументов
    """
    avg_day_files = 6000
    avg_weekends_files = 2000
    avg_night_files = 3000
    new_users_number = 6000
    type = 'plan'
    need_workload = 0.86

    expected1 = {
        '180h_day': 4,
        '168h': 0,
        '79h': 0,
        '180h_night': 4,
        '180h_weekend': 4
    }
    result1 = calculator1.get_machines_scarcity(
        type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number, need_workload
    )
    assert result1 == expected1

    expected2 = {
        '180h_day': 1,
        '168h': 1,
        '79h': 1,
        '180h_weekend': 1,
        '180h_night': 1
    }
    result2 = calculator2.get_machines_scarcity(
        type, avg_day_files, avg_weekends_files,
        avg_night_files, new_users_number, need_workload
    )
    assert result2 == expected2
