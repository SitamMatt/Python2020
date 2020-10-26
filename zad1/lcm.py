from utils import get_list


def factorize_to_primes(num):
    i = 2
    result = []
    while i * i < num:
        while num % i == 0:
            num /= i
            result.append(i)
        i += 1
    result.append(int(num))
    return result


def count_multiples(numbers):
    multiples = {}
    for number in numbers:
        if number in multiples:
            multiples[number] += 1
        else:
            multiples[number] = 1
    return multiples


def lcm(a, b):
    a_prime_factors = factorize_to_primes(a)
    a_prime_factors_multiplicities = count_multiples(a_prime_factors)

    b_prime_factors = factorize_to_primes(b)
    b_prime_factors_multiplicities = count_multiples(b_prime_factors)

    distinct_factors = set(get_list(a_prime_factors_multiplicities) + get_list(b_prime_factors_multiplicities))

    result = 1
    for factor in distinct_factors:
        factor_exponent = max(a_prime_factors_multiplicities.get(factor, 0),
                              b_prime_factors_multiplicities.get(factor, 0))
        result *= factor ** factor_exponent

    return result
