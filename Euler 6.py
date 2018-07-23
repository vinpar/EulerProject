v = 10
PrCount = 0
end = False
# Euler 7 What is the 10 001st prime number?
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

            PrCount = PrCount + 1
            print(PrCount, num)
            if PrCount == 10001:
                print(PrCount, num, "is a prime ")
                end = True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        # print(num,"is not a prime number")
        pass
    if end == True:
        break

