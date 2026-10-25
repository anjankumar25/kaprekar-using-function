def kap(a):
    b=a
    c=0
    d=a*a
    v=len(str(a))
    e=d%(10**v)
    m=d//(10**v)
    c=e+m
    if b == c:
        print("kaprekar")
    else:
        print("not a kaprekar")
kap(a=45)
