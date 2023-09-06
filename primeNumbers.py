def is_prime(n):
    prime = True
    if n <= 1:
            prime = False
    for i in range(2, int(n/2)):
        if n % i == 0:
            prime = False
    return prime
    
def print_is_prime():
    count = 0
    for i in range(1, 1001):
        if is_prime(i):
            count += 1
            print(i)
    print('Sum:', count)

print_is_prime()