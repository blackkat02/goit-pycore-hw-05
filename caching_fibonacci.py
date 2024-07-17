from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    print("start 'caching_fibonacci'")
    cache = {}
    print(f"cache after start: {cache}")

    def fibonacci(n: int) -> int:
        if n < 0:
            return 0
        elif n <= 1:
            return n
        elif n in cache:
            return cache[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        print(f"change cache: {cache}") # Змінжється, тільки якщо n не знаходиться в словнику cache
        return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci


fib = caching_fibonacci()

print(fib(10))
print(fib(15))

for i in range(0, 18):
    print(fib(i))
