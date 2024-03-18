def counting_sort(v: list[int]):
    n = len(v)
    k = max(v)+1
    contador = [0 for i in range(k)]
    resposta = [0 for i in range(n)]
    for i in range(n):
        contador[v[i]] += 1
    for i in range(1,k):
        contador[i] += contador[i-1]
    for i in range(n-1,-1,-1):
        elemento = v[i]
        resposta[contador[elemento]-1] = elemento
        contador[elemento] -= 1
    for i in range(n):
        v[i] = resposta[i]
                        

