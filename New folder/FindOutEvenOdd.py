n = int(input())
even = []
odd = []
list1 = list(map(int, input().split()))
for i in list1:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

for i in even:
    print(i, end=' ')
print()

for i in odd:
    print(i, end=' ')

