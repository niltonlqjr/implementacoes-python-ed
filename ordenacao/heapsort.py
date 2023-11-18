def heapsort(v: list[int]):
    def maxheapfy(v: list[int], i: int, n: int):
        maior:int = i
        fe: int = 2*i+1
        fd: int = 2*i+2
        if fd < n and v[fd]>v[maior]:
            maior = fd
        if fe < n and v[fe]>v[maior]:
            maior = fe
        if maior != i:
            v[i],v[maior] = v[maior],v[i]
            maxheapfy(v,maior,n)

    def buildmaxheap(v):
        n: int = len(v)
        i: int  = n//2
        while i >=0:
            maxheapfy(v,i,n)
            i-=1
            
    n: int = len(v)
    buildmaxheap(v)
    for i in range(n-1,0,-1):
        v[i],v[0] = v[0], v[i]
        maxheapfy(v,0,i)




