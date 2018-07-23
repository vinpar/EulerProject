import matplotlib.pyplot as plt
import math as m

#n=5983
n=1
bigDiv=0


while True:
    n=n+1
    tn=int((n*(n+1))/2)#triangular number
    d=0

    divCount=0
    #all the divisors up to sqrt(tn) will have a corresponding
    #one bigger than this so stop at this number and multiply by 2
    for d in range (1,int(m.sqrt(tn))):

        if tn%d==0:
            divCount=divCount+1
            if bigDiv<divCount:
                bigDiv=divCount
                print(n,tn, bigDiv)



    if divCount>250:
        break

