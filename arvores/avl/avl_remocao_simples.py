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
        self.altura: int = 1
        self.dado: item = dado

class arvore_avl:
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
    
    def remove(self, chave: int) -> bool:
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
        if n != None:
            n.altura = self.altura_no(n)
        return self.balanceia(n)

    def maior(self, n: no) -> no:
        if n.dir == None:
            return n
        else:
            return self.maior(n.dir)
    
    def remove_no(self, n: no, chave: int) -> no | None:
        if n != None:
            if n.dado.chave < chave:
                n.dir = self.remove_no(n.dir, chave)
            elif n.dado.chave > chave:
                n.esq = self.remove_no(n.esq, chave)
            else:
                if n.esq != None and n.dir != None:
                    antecessor = self.maior(n.esq)
                    n.dado = antecessor.dado
                    n.esq = self.remove_no(n.esq, antecessor.dado.chave)
                elif n.esq == None:
                    n = n.dir
                else:
                    n = n.esq
        return self.balanceia(n)
    
    def altura_no(self, n:no) -> int:
        altura_sad = 0
        altura_sae = 0
        altura_no = 0
        if n != None:
            if n.dir != None:
                altura_sad = n.dir.altura
            if n.esq != None:
                altura_sae = n.esq.altura
            altura_no = max(altura_sae,altura_sad) + 1
        return altura_no
    
    def rotacao_esq(self, p: no) -> no:
        q = p.dir
        p.dir = q.esq
        q.esq = p
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        return q
    
    def rotacao_dir(self, p: no) -> no:
        q = p.esq
        p.esq = q.dir
        q.dir = p
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        return q
    
    def balanceia(self, n: no) -> no:
        if n!= None:
            asd = self.altura_no(n.dir)
            ase = self.altura_no(n.esq)
            if asd > ase + 1 :
                if self.altura_no(n.dir.esq) > self.altura_no(n.dir.dir):
                    n.dir = self.rotacao_dir(n.dir)
                return self.rotacao_esq(n)
            elif ase > asd + 1:
                if self.altura_no(n.esq.dir) > self.altura_no(n.esq.esq):
                    n.esq = self.rotacao_esq(n.esq)
                return self.rotacao_dir(n)
            n.altura = self.altura_no(n)
        return n
    
    def string_ramo(self, n:no, nivel:int):
        s = ''
        s += '  '*nivel
        s += '|____'
        if n != None:
            s += 'chave:' + str(n.dado.chave) +' - altura:'+ str(n.altura) +'\n'
        else:
            s += '\n'
        if n != None:
            str_esq = self.string_ramo(n.esq,nivel+1)
            str_dir = self.string_ramo(n.dir,nivel+1)
            s += str_esq + str_dir
        return s

    def string(self):
        return self.string_ramo(self.raiz, 0)
