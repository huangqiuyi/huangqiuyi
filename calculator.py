#!usr/bin/env python3
 
import sys
a=sys.argv[1]
try:
    x=int(a)
    b=x-3500
    if (b<=1500):
        c=b*0.03
    elif (1500<b<=4500):
        c=b*0.1-105
    elif (4500<b<=9000):
        c=b*0.2-555
    elif (9000<b<=35000):
        c=b*0.25-1005
    elif (35000<b<=55000):
        c=b*0.3-2755
    elif (55000<b<=80000):
        c=b*0.35-5505
    else: 
        c=b*0.45-13505

    c=format(c,".2f")
    print(c)
except ValueError:
    print('input error')
    print ('exit')
