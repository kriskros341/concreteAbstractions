import math
import random

def zad1_4():
    temperature = 244
    elevation = 5280
    candy_temperature = lambda x,y: x+(y//500)
    return candy_temperature(temperature, elevation)

def zad1_5():
    income = 30000
    tax_bracket = 10000
    tax_value = 2/7
    if income > tax_bracket:
        taxable_income = income - tax_bracket
    else:
        return income
    return income - round(taxable_income*tax_value, 2)

def zad1_6(turkey_mass):
    if turkey_mass < 12:
        multiplier = 3/4
    else:
        multiplier = 1/2
    return round(turkey_mass * multiplier)

def to_first_higher_of_two(a,b,c):
    if b>c:
        value_to_increment_by = b
    else:
        value_to_increment_by = c
    return a+value_to_increment_by

def d(x):
    if x < 0:
        print("-"+x)
    else:
        print("+"+x)

def f(x, y):
    if x%2 == 0:
        return 7
    else:
        return x*y
def test_f():
    r = range(100)
    for p in r:
        for o in r:
            if f(p, o)==16:
                print(p, o)
                print(f(p, o))
def avg_of_2(x,y):
    return (x+y)/2

def right_triangle_height(x,y):
    return (x**2-y**2)**(1/2)

def sqrt(x):
    return x**(1/2)
def sqrt3(x):
    return x**(1/3)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


def double_slash_divide(n, d):
    if n < d:
        return 0
    else:
        return 1+double_slash_divide(n-d, d)
def multiply(x, y):
    if y == 0:
        return 0
    return x+multiply(x, y-1)

def add_squares_up_to(x):
    if x == 1:
        return 1
    return x**2 + add_squares_up_to(x-1)

def number_of_odd_in(x):
    n = 0
    for y in str(x):
        if int(y) % 2 != 0:
            n+=1
    return n

def foo(i, k=0):
    if i % 2 != 0:
        return i, k
    else:
        return foo(i/2, k+1)

def presents_on_christmas_day(n):
    if n == 1:
        return 1
    else:
        return n + presents_on_christmas_day(n-1)

def is_perfect(n):
    result = 0
    for x in range(1, n+1):
        if n % x == 0:
            result += x
    if result == 2*n:
        return True
    return False

def closest_power_recursive(b,n):
    if n < b:
        return 0
    else:
        return 1+closest_power(b, n/b)
def closest_power_iterative(b, n, res=0):
    if b > n:
        return res
    else:
        return closest_power_iterative(b, n//b, res+1)

def falling(n,k,r=0):
    if r == k:
        return 1
    return n*falling(n-1, k, r+1)

def pos_neg_pow(b, n):
    if n == 0:
        return 1
    elif n > 0:
        return pos_neg_pow(b, n-1)*b
    elif n < 0:
        return pos_neg_pow(b, n+1)/b
# iterative improvement
def first_perfect_after(n):
    nextone = n+1
    if is_perfect(nextone):
        return nextone
    else:
        return first_perfect_after(nextone)

def distance(x0,y0,x1,y1):
    diffx = x0-x1
    diffy = y0-y1
    return (diffx**2+diffy**2)**(1/2)

def find_approximation_from(starting_point, iterations = 10):
    if iterations > 0:
        return find_approximation_from(1+(1/starting_point), iterations-1)#formula, iteration-1
    else:
        return starting_point



print(find_approximation_from(5))
