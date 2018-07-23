# Euler 5

for n in range(2, 21):
    m = 1
    while True:
        m = m + 1

        Remainder = False

        for num in range(1, n + 1):

            if (m % num != 0):
                Remainder = True
                # print (0)

        if Remainder == False:
            print(n, "         ", m)
            break

