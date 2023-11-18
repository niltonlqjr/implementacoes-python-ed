import random
from heapsort import heapsort
from quicksort import quick_sort
from mergesort import merge_sort
from shell import shellsort
from shell import shell

def issorted(v):
    i=1
    while i<len(v) and v[i-1] <= v[i]:
        i+=1
    return i==len(v)

def test(sort_alg, num_tests=100, vec_size=200, vini=-1000, vfim=1000):
    for i in range(num_tests):
        v = [random.randint(vini,vfim) for i in range(vec_size)]
        sort_alg(v)
        assert issorted(v)
        print('test:',i,'OK')
    print('All tests OK!')


algs = [heapsort, quick_sort, merge_sort, shellsort, shell]

for algoritmo in algs:
    print('Testando:', algoritmo.__name__)
    test(algoritmo, num_tests=10, vec_size=200, vini=-1000, vfim=1000)
