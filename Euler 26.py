import decimal as dec

bitHit=0
bigHitn=0

searchLen=10  #length of number  to use as search string

dec.getcontext().prec=1000
for n in range (10,1001):
    d=str(dec.Decimal(1)/dec.Decimal(n))
    d=d[10:d.__len__()] #chop off front bit

    #can I find multiple hits??
    findStr=d[0:searchLen]  #find string offet in by 1
    Hit=d.find(findStr,1)
    if Hit>bigHitn:
        bigHitn=Hit
        bigHitn=n
        print(n,Hit)
        print(d[0:100])
        print(d[Hit:Hit+100])
