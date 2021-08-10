import concurrent.futures
import math

NUMBERS = [
   2,
   1099726899285419,
   1570341764013157,
   1637027521802551,
   1880450821379411,
   1893530391196711,
   2447109360961063,
   3,
   2772290760589219,
   3033700317376073,
   4350190374376723,
   4350190491008389,
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,
]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            return False
    return True

def executer():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(NUMBERS, executor.map(is_prime, NUMBERS)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    executer()