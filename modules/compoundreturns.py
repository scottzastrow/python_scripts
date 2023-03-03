#Title: Compounding Returns function
#Author: Scott Zastrow
from __future__ import division

def returns(rr, tp):
    '''
    Parameters:
        rr (float) : The rate of return for a period
        tp (float) : The time period for the return
        result (float) : The float result
        fs (string) : The formated string result
    '''
    result = (((1+rr)**tp)-1) *100
    
    fs =  "{0:.2f}%".format(result)

    print(f'Return Rate: {"{0:.2f}%".format(rr*100)}\nTime Period: {tp}\nCompounded Return: {fs}')
