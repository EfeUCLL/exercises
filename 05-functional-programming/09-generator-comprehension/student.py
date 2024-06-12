from itertools import count


# def is_prime(n):
#     if n == 0 or n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         return True


def is_prime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, n))


# count telt vanaf 2 verder.... 2, 3, 4, 5, 6 ...
def primes():
    return (n for n in count(2) if is_prime(n))
