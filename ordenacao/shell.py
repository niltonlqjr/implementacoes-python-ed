def shellsort(v: list[int]):
    i: int; j: int
    n: int = len(v)
    gap: int = 1
    while gap < n:
        gap=gap*3+1
    while gap > 1:
        gap = (gap-1)//3
        for i in range(gap,n):
            j=i
            aux = v[i]
            while j>=gap and v[j-gap] > aux:
                v[j] = v[j-gap]
                j-=gap
            v[j] = aux

def insertion(v: list[int], n: int):
    i: int; j:int; aux:int
    for i in range(1,n):
            aux=v[i]
            j=i
            while j>0 and v[j-1] > aux:
                    v[j]=v[j-1]
                    j-=1
            v[j]=aux

def shell(v: list[int]):
    i: int; j: int; k: int
    n: int = len(v)
    gap: int = 1
    aux: list[int] = [0]*n
    while gap < n:
        gap=gap*3+1
    while gap>1:
        gap = (gap-1)//3
        for i in range(gap):
            k=0
            for j in range(i,n,gap):
                aux[k]=v[j]
                k+=1
            insertion(aux,k)
            k=0
            for j in range(i,n,gap):
                v[j]=aux[k]
                k+=1
    

