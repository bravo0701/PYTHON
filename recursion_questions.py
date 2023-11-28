# Sum of digits of a number

def sum_of_digits(n):

    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n/10))


print(sum_of_digits(1124738))


# Power of a number

def power(base, exp):

    assert exp >= 0 and int(exp) == exp, 'The exponent must be positive integer only!'
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power(base, exp-1)


print(power(2, 1))


# Greatest Common Divisor of two numbers

def gcd(a, b):

    assert int(a) == a and int(b) == b, 'The numbers must be positive integer only!'
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(18, 48))


# Convert a number from Decimal to Binary

def dec_bin(n):

    assert int(n) == n, "The number must be a integer only"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * dec_bin(int(n/2))


print(dec_bin(13))
