# Fibonacci sequence using generator


def fib_gen():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == "__main__":
    fibonacci = fib_gen()
    for _ in range(10):
        print(next(fibonacci))
