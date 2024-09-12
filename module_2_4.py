numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
a = 0
for i in numbers:
    for j in range(2, i):
        a = 0
        if  i % j == 0:
            a += 1
            break
    if i == 1:
        continue
    elif a <= 0:
        primes.append(i)
    else:
        not_primes.append(i)
print('Простые: ', primes)
print('Не простые: ', not_primes)