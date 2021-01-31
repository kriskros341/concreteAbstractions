""" page 93 """
def mod_expt(base, exponent, modulus):
    def mmod(x, y):
        return (x*y) % modulus
    if exponent == 0:
        return 1
    else:
        if exponent % 2 == 0:
            x = mod_expt(base, exponent/2, modulus)
            return mmod(x, x)
        else:
            return mmod(mod_expt(base, exponent-1, modulus), base)


def mod_expt(base, exponent, modulus, count=1):
    def mmod(x, y):
        print(count)
        return (x*y) % modulus
    if exponent == 0:
        return 1
    else:
        if exponent % 2 == 0:
            x = mod_expt(base, exponent/2, modulus, count+1)
            return mmod(x, x)
        else:
            return mmod(mod_expt(base, exponent-1, modulus, count+1), base)

def mod_expt(base, exponent, modulus, count=1):
    def mmod(x, y):
        return (x*y) % modulus
    if exponent == 0:
        return 1
    else:
        if exponent % 2 == 0:
            x = mod_expt(base**2, exponent/2, modulus, count+1)
            return (x*x) % modulus
        else:
            return mod_expt(base, exponent-1, modulus, count+1)**2 % base

def low_and_high(low, high, iterat=0):
    if low+iterat == high:
        return high
    return low+iterat+low_and_high(low,high,iterat+1)


def is_sum_div_by_17(n):
    def sumof(n):
        if n==1:
            return 1
        return n+sumof(n-1)
    return sumof(n) % 17 == 0


def make_verifier(f, m):
    def check(m, n):
        if m == n:
            return True
        else:
            return False
    return check(f, m)

def make_function_proxy(n, b, p):
    return p(n+1, b)

def f(x):
    return x**2 - 2*x

def find_smallest_in_range_for_function(mrange, mfunction):
    best = max(mrange)
    for x in mrange:
        val = mfunction(x)
        if val < best:
            best = val
    return best


def is_function_growing_in_range(l, h, mfunction):
    #min_value = min([f(x) for x in mrange])
    for x in range(l, h):
        if f(x) < f(l):
            return False
    return True
#l, h = 0, 100
#print(is_function_growing_in_range(l, h, f))
"""factory"""
def double(x):
    return x*2

def square(x):
    return x*x

def make_average(f, x):
    return (f+x)/2

def new_procedure(proc, f, x):
    return proc(f, x)

print(new_procedure(make_average, double(4), square(4)))

#def make_exponentiater (make-generator "excerpt")








