from euclidean import gcd
from lcm import lcm
from primes import sieve_of_eratosthenes
from wallis import wallis_product

print("Programowanie w języku Python - zadanie 1:")
print("zad 1: \n")

for i in range(1, 11):
    print(f"n = {i}, wallis = {wallis_product(i)}")

print()

print(f"nwd dla (84,18) = {gcd(84, 18)}")

print()
print("zad 3: \n")

print(f"Liczby pierwsze < 100 = {sieve_of_eratosthenes(2, 100)}")

print()
print("zad 4: \n")

print(f"nww dla (192,348) = {lcm(192, 348)}")
