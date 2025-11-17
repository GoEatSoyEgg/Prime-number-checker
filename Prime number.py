def prime_232730E(number_232730E):
    if number_232730E <= 1:
        return False
    for i in range(2, int(number_232730E ** 0.5) + 1):
        if number_232730E % i == 0:
            return False
    return True


def primes_in_range_232730E(lower, upper):
    for number_232730E in range(lower, upper + 1):
        if prime_232730E(number_232730E):
            print(number_232730E)


lower_232730E = int(input("Enter Lower value: "))
upper_232730E = int(input("Enter Upper value: "))

primes_in_range_232730E(lower_232730E, upper_232730E)