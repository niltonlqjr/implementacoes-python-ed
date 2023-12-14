from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int | None

class pilha:
    def __init__(self, tam_max: int):
        self.elementos: list[item] = [item(None)] * tam_max
        self.tam_max = tam_max
        self.topo = 0

    def vazia(self) -> bool:
        return self.topo == 0
    
    def cheia(self) -> bool:
        return self.topo == self.tam_max

    def empilha(self, x: item):
        if self.cheia():
            raise ValueError('Pilha Cheia')
        else:
            self.elementos[self.topo] = deepcopy(x)
            self.topo += 1

    def desempilha(self):
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            self.topo -= 1
    
    def elemento_topo(self) -> item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            return deepcopy(self.elementos[self.topo-1])
            
    def string(self) -> str:
        s: str = '[ '
        for i in range(self.topo):
            s += '({0})'.format(self.elementos[i].valor)
        s += ']'
        return s
        