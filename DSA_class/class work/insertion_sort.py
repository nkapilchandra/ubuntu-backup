def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        for j in range(i,0,-1):
            if (a[j] < a[j-1]):
                a[j],a[j-1] = a[j-1],a[j]
            else:
                break
    return a
print(insertion_sort([14,4531,220,4]))
