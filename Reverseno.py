x=int(input())
def getReverse(num):
    res=0
    remainder=0
    while(num>0):
        remainder=num % 10
        num=num // 10
        res=res * 10 +remainder
    return res
print(getReverse(x))