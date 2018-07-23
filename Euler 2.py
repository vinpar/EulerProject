# Euler 2
# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.
nless1 = 1
nless2 = 0
n = 1
sofevenn = 0
while n < 4000001:
    n = nless1 + nless2
    print(n)

    if n % 2 == 0:
        sofevenn += n

    nless2 = nless1
    nless1 = n

print("Sum of even n", sofevenn)

