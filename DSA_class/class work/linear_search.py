from time import perf_counter
""" Linear Search
    List size: 1000000
    BEST CASE: 2.0568999843817437e-05
    WORST CASE: 0.07774594400007118"""
def lin_search(List,num):
    ind = 0
    for i in List:
        if (i==num):
            return ind
        else:
            ind += 1
    return "Number not present"

""" Binary Search
    List size: 1000000
    BEST CASE: 8.108899965009186e-05
    WORST CASE:
"""
def binary_search(List,num):
    i = 0
    j = len(List)-1
    while(True):
        mid = (i+j)//2
        print(i,mid,j)
        if(List[mid]==num):
            return mid
        if (num < List[mid]):
            j = mid-1
        else:
            i = mid+1



a = range(1000000)
a = list(a)
t1 = perf_counter()
print (binary_search(a,1))
t2 = perf_counter()
print(t2-t1)
