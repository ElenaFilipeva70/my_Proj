from _pytest.capture import CaptureFixture

from src.decorators import log


@log("logs/mylog.txt")
def my_function(x: int | float, y: int | float) -> int | float:
    return x + y


def test_decorators_my_function() -> None:
    """Тестируем выполнение декорированной функции"""
    result = my_function(1, 2)
    assert result == 3


def test_decorators_log_file() -> None:
    """Тестируем запись в файл после успешного выполнения"""
    my_function(7, 5)
    with open("logs/mylog.txt", "r", encoding="utf-8") as file:
        result = file.readline()
    assert result == "Функция: my_function, результат: 12, ок\n"


def test_decorators_log_consol(capsys: CaptureFixture[str]) -> None:
    """Тестируем вывод в консоль после успешного выполнения"""

    @log()
    def my_function(x: int | float, y: int | float) -> int | float:
        return x + y

    my_function(71.02, 29.036)
    captured = capsys.readouterr()
    assert captured.out == "Функция: my_function, результат: 100.056, ок\n"


def test_decorators_log_invalid_file() -> None:
    """Тестируем вывод в файл при ошибке"""

    my_function("71.02", 29.036)
    with open("logs/mylog.txt", "r", encoding="UTF-8") as file:
        result = file.readline()
    assert result == "my_function, ERROR: TypeError. Inputs: ('71.02', 29.036), {}\n"


def test_decorators_log_invalid_consol(capsys: CaptureFixture[str]) -> None:
    """Тестируем вывод в консоль при ошибке"""

    @log()
    def my_function(x: int | float, y: int | float) -> int | float:
        return (x + y) * 8

    my_function("71.02", 29.036)
    captured = capsys.readouterr()
    assert captured.out == "Функция: my_function, ERROR: TypeError. Inputs: ('71.02', 29.036), {}\n"
