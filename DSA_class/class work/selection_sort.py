def selection_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
    return a
print(selection_sort([4,5,623,212]))
