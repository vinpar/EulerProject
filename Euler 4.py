# Euler 4
# Find the largest palindrome made from the product of two 3-digit numbers.
for i in range(1, 999 * 999):
    test = str(i)
    rtest = test[::-1]
    if (test[0:3] == rtest[0:3]):
        # print (i)
        # it is palindromic
        # now check to see if it has two 3 digit factors
        for j in range(1, i):
            if (i % j) == 0:
                if j > 99 and j < 1000 and i / j > 99 and i / j < 1000:
                    print(j, "times", i / j, "equals", i)


