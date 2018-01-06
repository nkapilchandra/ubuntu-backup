def merge_sort(a):
    n = len(a)
    if (n == 1):
        return a
    else:
        left = a[:n//2]
        right = a[n//2:]
        # print(left,right)
        return merge(merge_sort(left),merge_sort(right))

def merge(left,right):
    new = []
    i = 0
    j = 0
    while(i<len(left) and j<len(right)):
        if(left[i] <= right[j]):
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    while (i < len(left)):
        new.append(left[i])
        i += 1
    while (j < len(right)):
        new.append(right[j])
        j += 1
    return new

print(merge_sort([9,123123,9,0,0,0]))
