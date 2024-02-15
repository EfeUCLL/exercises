# Write your code here

#2 is the only even prime number
#range is exclusive of the last number
def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
            #if n % i == 0, it means that n is divisible by a different number than itself or 1, so it is not prime
    return True