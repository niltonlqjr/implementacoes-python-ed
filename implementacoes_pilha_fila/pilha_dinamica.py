from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int

class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None

class pilha:
    def __init__(self):
        self.topo: no | None = None
  
    def vazia(self) -> bool:
        return self.topo == None

    def empilha(self, x: item):
        novo = no(x)
        novo.prox = self.topo
        self.topo = novo


    def desempilha(self):
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            rem = self.topo
            self.topo = self.topo.prox
            rem.prox = None

    def elemento_topo(self) -> item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            dado = self.topo.dado
            ret = deepcopy(dado.valor)
            return ret

    def string(self) -> str:
        v = self.topo
        s: str = '[ '
        while v != None:
            s+='({0}) '.format(v.dado.valor)
            v = v.prox
        s+=']'
        return s

