numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(0, len(numbers)):
    is_prime = True
    for j in range(0, numbers[i]):
        if numbers[i] != 1 and numbers[j] !=1 and numbers[i] != numbers[j] and numbers[i] % numbers[j] == 0:
            is_prime = False
    if is_prime == True and numbers[i] != 1:
        primes.append(numbers[i])
    elif is_prime == False and numbers[i] != 1:
        not_primes.append(numbers[i])
print(numbers)
print(primes)
print(not_primes)
