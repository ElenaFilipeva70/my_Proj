import os
from collections.abc import Callable
from functools import wraps
from time import time
from typing import Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции, а также
    ее результаты или возникшие ошибки."""

    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()

                if filename is not None:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"Функция: {func.__name__}, результат: {result}, ок\n")
                        print(f"Время работы функции: {end_time - start_time:.6f}")
                else:
                    print(f"Функция: {func.__name__}, результат: {result}, ок")
                return result
            except TypeError as error:
                if filename is not None:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__}, ERROR: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"Функция: {func.__name__}, ERROR: {error.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_file = os.path.join(base_dir, "logs", "mylog.txt")


# @log(filename=path_file)
# def my_function(x: int | float, y: int | float) -> int | float:
#     return x + y

# my_function(71.02, 29.036)
