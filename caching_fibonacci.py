from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    This function creates a closure that implements a memoized version of the
    Fibonacci sequence. Memoization stores previously calculated results in a
    cache to avoid redundant calculations.

    Returns:
        Callable[[int], int]: A function that calculates the nth Fibonacci number
        using memoization.
    """

    print("start 'caching_fibonacci'")
    cache = {}
    print(f"cache after start: {cache}")

    def fibonacci(n: int) -> int:
        """
        Calculates the nth Fibonacci number using memoization.
        Args:
            n (int): The index of the Fibonacci number to calculate.
                    Must be non-negative.
        Returns:
            int: The nth Fibonacci number.
        """
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
