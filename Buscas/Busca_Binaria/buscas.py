from dataclasses import dataclass

@dataclass
class item:
    chave: int

def busca_sequencial(v: list[item], ch: int,  n:int) -> int:
    for i in range(n):
        if v[i].chave == ch:
            return i
    return -1

def busca_binaria(v: list[item], ch: int,  n:int) -> int:
    esquerda:int = 0
    direita:int = n-1
    while (esquerda <= direita):
        meio = (esquerda+direita) // 2
        if v[meio].chave == ch:
            return meio
        elif ch > v[meio].chave:
            esquerda = meio+1
        else:
            direita=meio-1
    return -1
