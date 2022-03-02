t= int(input())
while (t >0):
    n=int(input())
    rem=0
    while(n>0):
           rem = n % 10
           n = n // 10
    print(rem)
    t=t-1

