from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy



@dataclass
class item:
    chave: int
    valor: float

class no:
    def __init__(self, dado: item):
        self.esq: no | None = None
        self.dir: no | None = None
        self.dado: item = dado

class arvore:
    def __init__(self):
        self.raiz: no | None = None

    def vazia(self):
        return self.raiz == None

    def insere(self, x:item) -> bool:
        self.raiz = self.insere_no(self.raiz, x)
        
    def remove(self, chave: int) -> bool:
        self.raiz = self.remove_no(self.raiz, chave)

    def insere_no(self, n: no , x: item) -> no | None:
        if n == None:
            n = no(deepcopy(x))
        elif x.chave > n.dado.chave:
            n.dir = self.insere_no(n.dir,x)
        elif x.chave < n.dado.chave:
            n.esq = self.insere_no(n.esq,x)
        return n

    def troca_e_remove(self, no_atual: no, remover: no) -> no:
        if no_atual.esq != None:
            no_atual.esq = self.troca_e_remove(no_atual.esq, remover)
        else:
            remover.dado = no_atual.dado
            remover = no_atual
            no_atual = no_atual.dir
        return no_atual
    
    def remove_no(self, n: no, chave: int) -> no | None:
        if n != None:
            if n.dado.chave < chave:
                n.dir = self.remove_no(n.dir, chave)
            elif n.dado.chave > chave:
                n.esq = self.remove_no(n.esq, chave)
            else:
                if n.esq != None and n.dir != None:
                    n.dir = self.troca_e_remove(n.dir, n)
                if n.esq == None:
                    n = n.dir
                else:
                    n = n.dir
        return n
    
    def string_ramo(self, n:no, nivel:int):
        s = ''
        s += '  '*nivel
        s += '|____'
        if n != None:
            s += str(n.dado.chave) + '\n'
        else:
            s += '\n'
        if n != None:
            str_esq = self.string_ramo(n.esq,nivel+1)
            str_dir = self.string_ramo(n.dir,nivel+1)
            s += str_esq + str_dir
        return s

    def string(self):
        return self.string_ramo(self.raiz, 0)

def menor(a):
    if a == None:
        m = None
    elif a.esq == None:
        m = a
    else:
        m=menor(a.esq)
    return m



def remove(a,chave):
    if a != None:
        if a.dado.chave < chave:
            a.dir = remove(a.dir,chave)
        elif a.dado.chave > chave:
            a.esq = remove(a.esq,chave)
        else:
            if a.esq != None and a.dir != None:
                q = menor(a.dir)
                a.dado = q.dado
                a.dir = remove(a.dir,q.dado.chave)
            else:
                if a.esq == None:
                    a = a.dir
                else:
                    a = a.esq
    return a
        
a1=arvore()
a2=arvore()
dados=[1,12,10, 29, 36, 5, 33, 27, 40, 4, 7, 20, 23, 35, 37,42,21,22,23]
dados=[12,10, 22, 36, 5, 33, 27, 40, 4, 7, 20, 23, 35, 37,42,24]
#dados = [5,3,9,2,4,7,10,1,2.5,3.5,4.5,6,8,9.5,11]
#dados=[19,2,3,4,5,6,7,8,9,10,11,12,13,20]
val=''

for ch in dados:
    x=item(ch,val)
    a1.insere(x)
    x=item(ch,val)
    a2.insere(x)
    print('===inseriu {0}==='.format(ch))
    print(a1.string())
    print('=================')

       
        




