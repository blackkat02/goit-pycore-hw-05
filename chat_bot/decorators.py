from functools import wraps


def try_except_wrapper(func):
    """
    Декоратор, який обгортає функцію блоком try-except.
    Args:
        func (Callable): Функція, яку потрібно обгорнути.
    Returns:
        Callable: Декорована функція.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка при виконанні функції {func.__name__}: {e}")

    return wrapper
