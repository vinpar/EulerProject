#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m


def CalculateTime(a1, a2, a3, a4, a5, a6):

    # First Triangle.
    m1 = m.sqrt(5000)
    adj1 = 50 - (m1 / 2)
    fa1 = m.radians(180-(a1+135))

    h1 = adj1 / m.sin(fa1) * m.sin(m.radians(135))
    c = (h1 / m.sin(m.radians(135))) * m.sin(m.radians(a1))
    y1 = m.sin(m.radians(45)) * c
    x1 = adj1 + y1

    # Second Triangle.
    adj2 = 10
    h2 = adj2 / m.cos(m.radians(a2))
    s2 = m.radians(45- a2)
    #print (s2)
    x2 = m.cos(s2) * h2
    y2 = m.sin(s2) * h2

    # Third Triangle.
    adj3 = 10
    h3 = adj3 / m.cos(m.radians(a3))
    s3 = m.radians(45 - a3)

    x3 = m.cos(s3) * h3
    y3 = 0-m.sin(s3) * h3

    # Fourth Triangle.
    adj4 = 10
    h4 = adj4 / m.cos(m.radians(a4))
    s4 = m.radians(45 - a4)

    x4 = m.cos(s4) * h4
    y4 = 0-m.sin(s4) * h4

    # Fifth Triangle.
    adj5 = 10
    h5 = adj5 / m.cos(m.radians(a5))
    s5 = m.radians(45 - a5)

    x5 = m.cos(s5) * h5
    y5 = 0-m.sin(s5) * h5

    # Sixth Triangle.
    adj6 = 10
    h6 = adj6 / m.cos(m.radians(a6))
    s6 = m.radians(45 - a6)

    x6 = m.cos(s6) * h6
    y6 =0- m.sin(s6) * h6

    # Seventh Triangle
    sumofx = x1 + x2 + x3 + x4 + x5 + x6
    sumofy = y1 + y2 + y3 + y4 + y5 + y6

    x7 = 100 - sumofx
    y7 = 0-sumofy

    h7 = m.sqrt((x7 * x7) + (sumofy * sumofy))



    time = h1 / 10 + h2 / 9 + h3 / 8 + h4 / 7 + h5 / 6 + h6 / 5 + h7 / 10
    # print(time)

    #points = np.matrix([[x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]])
    #print(points)
    sx1=x1
    sx2=sx1+x2
    sx3=sx2+x3
    sx4=sx3+x4
    sx5=sx4+x5
    sx6=sx5+x6

    sy1 = y1
    sy2 = sy1 + y2
    sy3 = sy2 + y3
    sy4 = sy3 + y4
    sy5 = sy4 + y5
    sy6 = sy5 + y6

    finalx=sumofx+x7
    finaly=sumofy+y7

    x = [0,sx1,sx2,sx3,sx4,sx5,sx6,finalx]
    y = [0,sy1,sy2,sy3,sy4,sy5,sy6,finaly]
    RetVal=[x,y,time]

    return RetVal






ShortTime = 20

#########################################
#STORAGE
sa1 = 145
sa2 = 145
sa3 = 145
sa4 = 145
sa5 = 145
sa6 = 145
##########################





# an1 = 11.00
# an2 = sta2 = 48.00
# an3 = sta3 = 42.00
# an4 = sta4 = 35.00
# an5 = sta5 = 28.00
# an6 = sta6 = 24.00


an1 = sta1 = 45
an2 = sta2 = 45
an3 = sta3 = 45
an4 = sta4 = 45
an5 = sta5 = 45
an6 = sta6 = 0

ea1 = an1 + 5
ea2 = an2 + 5
ea3 = an3 + 5
ea4 = an4 + 5
ea5 = an5 + 5
ea6 = an6 + 10
increment = 1

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
fig.show()
fig.canvas.draw()



while (an1 < ea1):
    an1 = an1 + increment
    while (an2 < ea2):
        an2 = an2 + increment
        print("an5: ", an5)

        while (an3 < ea3):
            an3 = an3 + increment

            while (an4 < ea4):
                an4 = an4 + increment

                while (an5 < ea5):
                    an5 = an5 + increment

                    while (an6 < ea6):
                        an6 = an6 + increment

                        t = CalculateTime(an6,
                                        (an5),
                                        (an4),
                                        (an3),
                                        (an2),
                                        (an1))


                        fig.canvas.draw()

                        if t[2] < ShortTime:
                            ShortTime = t[2]
                            sa1 = an1
                            sa2 = an2
                            sa3 = an3
                            sa4 = an4
                            sa5 = an5
                            sa6 = an6

                            ax.clear()
                            ax.plot(t[0], t[1], 'ro')
                            ax.plot(0, 10, 'ro')
                            ax.plot(10, -1)






                            # print(an1," ",an2," ",an3," ",an4," ",an5," ",an6)
                            # print("Shortest time=", ShortTime)

                            # print(t)
                            # print("")

                    an6 = sta6
                an5 = sta5
            an4 = sta4
        an3 = sta3
    an2 = sta2

print(ShortTime)
print(sa1, sa2, sa3, sa4, sa5, sa6)





