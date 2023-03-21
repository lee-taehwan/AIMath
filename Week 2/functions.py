import numpy as np
from matplotlib import pyplot as plt

def year2salary(year):
    basis = 0
    raise_per_year = 2
    salary = basis + year * raise_per_year
    return salary

def year2salary_unknown_basis(year, basis):
    raise_per_year = 2
    salary = basis + year * raise_per_year
    return salary

def compute_error(guess, gt):
    error = guess - gt
    squared_error = error**2
    return squared_error.sum()

def derivative(f, a, eps=1e-4):
    return (f(a + eps) - f(a - eps)) / (eps * 2)

def composite(a_hat):
    x = 1
    y = 3

    y_hat = x * a_hat
    error = y_hat - y
    L = error ** 2

    return L

# prepare inputs
years = np.arange(1, 10)

# prepare GTs
salaries = year2salary(years)
print(salaries)

# compute errors for basis guesses
errors = []
basis_guesses = np.arange(-3, 3)
for basis_guess in basis_guesses:
    salaries_guess = year2salary_unknown_basis(years, basis_guess)
    error = compute_error(salaries_guess, salaries)
    errors.append(error)
print(basis_guesses)
print(errors)
min_error = min(errors)
min_idx = errors.index(min_error)
print(basis_guesses[min_idx])

a_hat = 1
x = 1
y = 3
y_hat = x * a_hat
error = y_hat - y
L = error ** 2

dLde = 2 * error
dedyh = 1
dLdyh = dLde * dedyh
dyhdah = 1
dLdah = dLdyh * dyhdah

print('dLde', dLde)
print('dLdyh', dLdyh)
print('dLdah', dLdah)

print(derivative(composite, 1))