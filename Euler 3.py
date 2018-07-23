# Euler 3
# What is the largest prime factor of the number 600851475143 ?
# Python program to check if the input number is prime or not
v = 600851475143
for num in range(0, v):

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # print(num,"is not a prime number")
                # print(i,"times",num//i,"is",num)
                pass
                break
        else:

            if v % num == 0:
                print(num, "is a prime factor")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        # print(num,"is not a prime number")
        pass

