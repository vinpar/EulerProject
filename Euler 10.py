# Euler 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True


v = 2000001
LOP = []

# check for factors
for i in range(2, v):
    if isPrime2(i):
        LOP.append(i)
        print(i)

print(sum(LOP))


