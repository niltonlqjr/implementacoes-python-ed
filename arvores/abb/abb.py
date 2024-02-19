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

    def insere(self, x:item):
        self.raiz = self.insere_no(self.raiz, x)
    
    def busca(self, ch:int) -> item | None:
        no = self.busca_no(self.raiz, ch)
        if no != None:
            return no.dado
        else:
            return None
    
    def remove(self, chave: int):
        self.raiz = self.remove_no(self.raiz, chave)

    def busca_no(self, n: no, chave:int) -> no | None:
        if n == None:
            return None
        elif chave > n.dado.chave:
            return self.busca_no(n.dir, chave)
        elif chave < n.dado.chave:
            return self.busca_no(n.esq, chave)
        else:
            return n
        
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
                elif n.esq == None:
                    n = n.dir
                else:
                    n = n.esq
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
