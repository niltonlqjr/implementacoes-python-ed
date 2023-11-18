def merge_sort(v):
    def merge(v: list[int], ini: int, meio: int, fim: int):
        i: int; j: int
        tam_v1: int = meio-ini+1
        tam_v2: int = fim-meio
        v1: list[int] = [0] * tam_v1
        v2: list[int] = [0] * tam_v2
        k: int = ini
        for i in range(tam_v1):
            v1[i] = v[k]
            k+=1
        for j in range(tam_v2):
            v2[j] = v[k]
            k+=1
        i,j,k = 0,0,ini
        while i < tam_v1 and j < tam_v2:
            if v1[i] <= v2[j]:
                v[k] = v1[i]
                i+=1
            else:
                v[k] = v2[j]
                j+=1
            k+=1
        while j < tam_v2:
            v[k] = v2[j]
            k,j = k+1,j+1
        while i < tam_v1:
            v[k] = v1[i]
            k,i = k+1,i+1

    def mergesort(v: list[int], ini: int, fim: int):
        meio: int = (ini+fim)//2
        if ini<fim:
            mergesort(v, ini, meio)
            mergesort(v, meio+1, fim)
            merge(v, ini, meio, fim)

    mergesort(v,0,len(v)-1)
