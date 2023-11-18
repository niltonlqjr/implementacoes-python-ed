from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    chave: int 
    valor: float 


class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None 

class lista:
    def __init__(self):
        self.ultimo: no | None = None
  
    def vazia(self) -> bool:
        return self.ultimo is None

    def busca(self, chave: int) ->  no | None:
        if self.vazia():
            return None
        ptr = self.ultimo.prox
        while (ptr != self.ultimo) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        if ptr.dado.chave == chave:
            return ptr
        else:
            return None
        
    def busca_item(self, chave: int) -> item | None:
        ptr: no | None = self.busca(chave)
        if ptr is not None:
            return deepcopy(ptr.dado)
        else:
            return None

    def insere_ini(self, x: item) -> bool:
        if self.busca(x.chave) is None:
            novo = no(x)
            if self.vazia():
                self.ultimo = novo
            else:
                novo.prox = self.ultimo.prox
            self.ultimo.prox = novo
            return True
        else:
            return False

    def insere_fim(self, x: item) -> bool:
        inseriu = self.insere_ini(x)
        if inseriu:
            self.ultimo=self.ultimo.prox
        return inseriu


    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.ultimo.prox
            self.ultimo.prox = rem.prox
            if rem == self.ultimo:
                self.ultimo = None
            rem.prox = None
            return True
        return False

    def string(self) -> str:
        l_str: str = '[ '
        if not self.vazia():
            v: no = self.ultimo.prox
            while v != self.ultimo:
                l_str += '({0}, {1}) '.format(v.dado.chave, v.dado.valor)
                v = v.prox
            l_str += '({0}, {1}) ]'.format(v.dado.chave, v.dado.valor)
        else:
            l_str += ']'
        return l_str        
        


