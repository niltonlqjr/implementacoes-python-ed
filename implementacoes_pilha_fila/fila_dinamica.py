from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int | None

class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None

class fila:
    def __init__(self):
        self.primeiro = no(item(None))
        self.ultimo = self.primeiro
  
    def vazia(self):
        return self.primeiro.prox == None

    def enfileira(self, x:item):
        novo = no(x)
        self.ultimo.prox = novo
        novo.prox=None
        self.ultimo=novo
        
    def desenfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            rem = self.primeiro.prox
            self.primeiro.prox = rem.prox
            if self.vazia():
                self.ultimo = self.primeiro
            rem.prox = None

    def obtem_primeiro(self) -> item:
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            dado = self.primeiro.prox.dado
            ret = deepcopy(dado)
            return ret

    def string(self):
        v: no = self.primeiro.prox
        s: str = '[ '
        while v != None:
            s += '({0}) '.format(v.dado.valor)
            v = v.prox
        s += ']'
        return s



