from __future__ import annotations
from dataclasses import *
from copy import deepcopy

@dataclass
class item:
    chave: int | None # optei por colocar None pois a sentinela irá armazenar um item(None, None)
    valor: float | None

class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None

class lista:
    def __init__(self):
        self.primeiro = no(item(None,None))
        self.ultimo = self.primeiro

    def vazia(self) -> bool:
        return self.primeiro.prox == None

    def busca(self, chave: int) -> no:
        ptr = self.primeiro.prox
        while (ptr != None) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        return ptr

    def busca_item(self, chave: int) -> item | None:
        ptr = self.busca(chave)
        if ptr != None:
            return deepcopy(ptr.dado)
        else:
            return None
        
    def insere_ini(self, x: item) -> bool:
        if self.busca(x.chave) == None:
            novo = no(x)
            novo.prox = self.primeiro.prox
            if self.vazia():
                self.ultimo = novo
            self.primeiro.prox = novo
            return True
        else:
            return False

    def insere_fim(self, x: item) -> bool:
        if self.busca(x.chave) == None:
            novo = no(x)
            self.ultimo.prox = novo
            novo.prox=None
            self.ultimo=novo
            return True
        else:
            return False

    def insere_pos(self, x: item, pos: int) -> bool:
        i=0
        ptr=self.primeiro
        if self.busca(x.chave) == None:
            while ptr!=None and i<pos:
                ptr=ptr.prox
                i+=1
            if ptr!=None:
                novo=no(x)
                novo.prox = ptr.prox
                if novo.prox == None:
                    self.ultimo=novo
                ptr.prox=novo
                return True
        return False

    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.primeiro.prox
            self.primeiro.prox = rem.prox
            if self.vazia():
                self.ultimo = self.primeiro
            rem.prox = None
            return True
        return False

    def remove_chave(self, chave: int) -> bool:
        ptr=self.primeiro
        while ptr.prox!=None and ptr.prox.dado.chave != chave:
            ptr=ptr.prox
        if ptr.prox!=None:
            paux=ptr.prox
            ptr.prox = paux.prox
            if ptr.prox == None:
                self.ultimo = ptr
            paux.prox = None
            return True
        return False    

    def string(self) -> str:
        v: no = self.primeiro.prox
        l_str = '[ '
        while v != None:
            l_str += '(chave={0},valor={1}) '.format(v.dado.chave, v.dado.valor)
            v = v.prox
        l_str += ']'
        return l_str 



