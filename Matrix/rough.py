n = int(input())
even =[]
odd = []
arr=list(map(int,input().split()))
for i in range(n):
    arr[i] % 2 == 0
for i in range(n):
    print(arr[i], end=' ')
print()
for i in range(n):
    arr[i] % 2 != 0
for i in range(n):
    print(arr[i], end=' ')
