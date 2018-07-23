#function for working out proper divisors
def ProperDivisorsSum(n):
    divisorsOFN = []
    for pD in range (1 , n) :
        if n%pD == 0:
            divisorsOFN.append(pD)
    return (sum(divisorsOFN))

SOAN=0
for i in range(100,10000):

    x = ProperDivisorsSum(i)
    y = ProperDivisorsSum(x)
    if (y==i and i!=x):
        print("Amicable number of",i," = ",x)
        SOAN+=i


print(SOAN)