def get_prime_factors(number):
  factors = []
  divisor = 2
  while divisor <= number:
    if number % divisor == 0:
      if divisor not in factors:
        factors.append(divisor)
      number = number / divisor
    else:
      divisor += 1
  return factors

if __name__ == '__main__':
  print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
  print(get_prime_factors(13))  # [13]