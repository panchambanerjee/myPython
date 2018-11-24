import math


def fibonacci_1(n):  # O(n^2) -- Iterative
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci_2(n):  # O(2^n) -- Recursive
    if n < 2:
        return n
    return fibonacci_2(n-1) + fibonacci_2(n-2)


def fibonacci_3(n):  # O(1) -- Closed form solution
    sq5 = math.sqrt(5)
    phi = (1 + sq5)/2
    return int(math.floor(phi**n/sq5))


def test_fib():
    n = 10
    assert(fibonacci_1(n) == 55)
    assert(fibonacci_2(n) == 55)
    assert(fibonacci_3(n) == 55)
    print("Tests passed")


if __name__ == "__main__":
    test_fib()
