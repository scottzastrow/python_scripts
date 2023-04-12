#Title: Compounding Returns function
#Author: Scott Zastrow

from __future__ import division
import msvcrt

count = 0

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

    print("\n---------------")
    print("Output Results:")
    print("---------------")
    print(f'Return Rate: {"{0:.2f}%".format(rr*100)}\nTime Period: {tp}\nCompounded Return: {fs}\n')
    global count
    if count < 1:
        count = 1
        enterReturns()

def enterReturns():
    print("\n---------------")
    print("Note: .01 is 1%")
    print("---------------")

    while True:
        data = input("Enter Return rate: ")
        try:
            rate = float(data)
            break
        except:
            continue
            
    while True:
        data = input("Enter Time period: ")
        try:
            time = float(data)
            break
        except:
            continue       
    returns(rate,time)
        

