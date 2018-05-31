'''
Coursera divide and conquer programming assignment 1
'''
from math import floor,ceil
def karatsuba(x,y):
    if x<10 and y < 10:
        return x*y
    x_len=len(str(x))
    y_len=len(str(y))
    n=max(x_len,y_len)
    m=int(n/2)

    a=int(x/(10**m))
    b=int(x%(10**m))
    c=int(y/(10**m))
    d=int(y%(10**m))

    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    sum_sum=karatsuba(a+b,c+d)
    adbc=sum_sum-ac-bd
    return int((10**(2*m))*ac+(10**m)*adbc+bd)



if __name__=="__main__":
    result=karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                     2718281828459045235360287471352662497757247093699959574966967627)

    print(result)