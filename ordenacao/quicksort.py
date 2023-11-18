def quick_sort(v: list[int]):
    def partition(v: list[int], ini: int, fim: int):
        i: int
        pivo: int =v[ini]
        j: int =ini+1
        for i in range(ini+1,fim+1):
            if v[i] < pivo:
                v[i],v[j] = v[j],v[i]
                j+=1
        v[ini],v[j-1] = v[j-1],v[ini]
        return j-1
    def quicksort(v: list[int], ini: int, fim: int):
        if ini < fim:
            pivo: int = partition(v,ini,fim)
            quicksort(v,ini,pivo-1)
            quicksort(v,pivo+1,fim)
    quicksort(v,0,len(v)-1)

