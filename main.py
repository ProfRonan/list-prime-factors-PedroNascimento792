"""Módulo com funções."""
from typing import List

def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0,5)+ 1):
        if number % i == 0:
            return False
    return True    


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    factors = []
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors

number = 84
result = list_prime_factors(number)
print(result)
