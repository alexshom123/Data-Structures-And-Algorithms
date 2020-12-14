#Recursion Practice Problems----------------------------------------------------

#1 - sum of digits in a number
def sumOfDigits(n):
    assert n>=0 and int(n)==n
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))
print(f"\nsum of digits in 13 is {sumOfDigits(13)}\n")

#2 - power (calculate base^power)
def Power(base,power):
    assert power>=0 and int(power) == power
    if power == 0:
        return 1
    if power == 1:
        return base
    return base*(Power(base,power-1))
print(f"five to the power of two is {Power(5,2)}\n")

#3 - greatest common divisor between a and b (euclidean algorithm used)
def gcd(a,b):
    assert int(a) == a and int(b) == b
    if a<0:
        a = -1*a
    if b<0:
        b  = -1*b
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(f"The greatest common divisor of 100 and 55 is {gcd(100,55)}\n")

#4 - decimal to binary (I noticed working backwards f(n) = nmod2 + 10f(fn/2))
def DtoB(n):
    assert int(n) == n
    if n == 0:
        return 0
    else:
        return n%2 + 10*DtoB(int(n/2))
print(f"13 in binary is {DtoB(13)}\n")
