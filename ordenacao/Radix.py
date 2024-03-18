def radix_sort(v: list[int]):
    def digitos(x:int) -> int:
        return len(str(x))
    
    def obtem_digito(x: int, d:int)->int:
        return (x % (10**(d))) // (10**(d-1))
        
    def counting_sort_dig(v: list[int], digito:int):
        n = len(v)
        k = 10
        contador = [0 for x in range(k)]
        resposta = [0 for x in range(n)]
        for i in range(n):
            dig = obtem_digito(v[i],digito)
            contador[dig] += 1
        for i in range(1,k):
            contador[i] += contador[i-1]
        for i in range(n-1,-1,-1):
            elemento = v[i]
            dig = obtem_digito(elemento,digito)
            resposta[contador[dig]-1] = elemento
            contador[dig] -= 1
        for i in range(n):
            v[i] = resposta[i]

    maior:int = max(v)
    n=digitos(maior)
    for i in range(1,n+1):
        counting_sort_dig(v,i)