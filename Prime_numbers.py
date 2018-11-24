import math


def prime_1(num):  # Brute force

    is_prime = True
    for x in range(2, num):
        if num % x == 0:
            is_prime = False
            break

    return is_prime


def prime_2(num):  # Reject candidates up to square root of number

    is_prime = True
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            is_prime = False
            break

    return is_prime


def generate_primes(n):

    prime_list = []
    for i in range(1, n+1):
        if prime_1(i):
            prime_list.append(i)

    return prime_list


def test_prime():
    n1 = 10
    n2 = 17

    assert(prime_1(n1) is False)
    assert(prime_1(n2) is True)
    assert(prime_2(n1) is False)
    assert(prime_2(n2) is True)
    print("Tests passed!!")


if __name__ == "__main__":
    test_prime()

    print(generate_primes(20))

