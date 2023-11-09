from dataclasses import dataclass

@dataclass
class item:
    chave: int 
    valor: float 

@dataclass
class no:
    dado: item
    prox = None

@dataclass
class lista:
   ultimo: no = None
  
def vazia(l: lista) -> bool:
    return l.ultimo == None

def busca(l: lista, chave: int) -> no:
    if vazia(l):
        return None
    ptr = l.ultimo.prox
    while (ptr != l.ultimo) and (ptr.dado.chave != chave):
        ptr = ptr.prox
    if ptr.dado.chave == chave:
        return ptr
    else:
        return None

def insere_ini(l: lista, x: item) -> bool:
    if busca(l,x.chave) == None:
        novo = no(x)
        if vazia(l):
            l.ultimo = novo
        else:
            novo.prox = l.ultimo.prox
        l.ultimo.prox = novo
        return True
    else:
        return False

def insere_fim(l: lista, x: item) -> bool:
    inseriu = insere_ini(l,x)
    if inseriu:
        l.ultimo=l.ultimo.prox
    return inseriu


def remove_ini(l: lista) -> bool:
    if not vazia(l):
        rem = l.ultimo.prox
        l.ultimo.prox = rem.prox
        if rem == l.ultimo:
            l.ultimo = None
        rem.prox = None
        return True
    return False

def mostra_lista(l: lista) -> bool:
    if not vazia(l):
        v = l.ultimo.prox
        print('[ ',end='')
        while v != l.ultimo:
            print('(chave={0}, valor={1}) '.format(v.dado.chave, v.dado.valor),end='')
            v = v.prox
        print('((chave={0}, valor={1})) '.format(v.dado.chave, v.dado.valor),end='')
        print(']')
    else:
        print('[ ]')

    


