from functools import lru_cache

# UTILS ------------------------------------------------------------------------------
def get_least_significant_decimal_digits(number: int, decimal_count: int = 6) -> int:
    return number % (10 ** decimal_count)


# USING LRU CACHE DECORATOR -----------------------------------------------------------
@lru_cache(maxsize=None)
def recursive_lru_cache_fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return recursive_lru_cache_fibonacci(n - 1) + recursive_lru_cache_fibonacci(
            n - 2
        )


# USING A GLOBAL DICT AS CACHE --------------------------------------------------------
fibonacci_cache = {1: 1, 2: 1}


def recursive_cache_global_dict_fibonacci(n: int) -> int:
    global fibonacci_cache
    if not n in fibonacci_cache.keys():
        fibonacci_cache[n] = recursive_cache_global_dict_fibonacci(
            n - 1
        ) + recursive_cache_global_dict_fibonacci(n - 2)
    return fibonacci_cache[n]


# USING A SIMPLE RECURSIVE METHOD (slow, exponential complexity, stack overflow) ------
def recursive_slow_fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return recursive_slow_fibonacci(n - 1) + recursive_slow_fibonacci(n - 2)


# USING AN ITERATIVE METHOD -----------------------------------------------------------
def iterative_fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# USING DIVIDE AND CONQUER WITH MATRIX MULTIPLICATION ---------------------------------
def dac_fibonacci(n):

    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):

    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):

    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if n % 2 != 0:
        multiply(F, M)


# MAIN --------------------------------------------------------------------------------
def get_fibonacci(n: int) -> dict:

    if n == 1 or n == 2:
        return 1

    elif n == 0:
        return 0

    else:
        return get_least_significant_decimal_digits(dac_fibonacci(n))


def execute():
    while True:
        try:
            n = int(
                input(
                    "Type an integer number to get the 6 least significant decimals digits of the fibonacci sequence: "
                )
            )
            if n < 0:
                n = abs(n)
                print(
                    f"Negative numbers are not allowed, using absolute value: {str(n)}"
                )
            break
        except:
            print("That's not an integer number!")

    return get_fibonacci(n)
