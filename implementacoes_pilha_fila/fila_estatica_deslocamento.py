from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy, copy


@dataclass
class item:
    valor: int

class fila:
    def __init__(self, tam_max: int):
        self.tamanho = tam_max
        self.fim = 0
        self.elementos: list[item] = [item(None) for i in range(tam_max)]
    
    def vazia(self) -> bool:
        return self.fim == 0
    
    def cheia(self) -> bool:
        return self.fim == self.tamanho
    
    def enfileira(self, x: item):
        if self.cheia():
            raise ValueError('Fila cheia')
        else:
            self.elementos[self.fim] = deepcopy(x)
            self.fim += 1
    
    def desenfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            for i in range(1,self.fim):
                self.elementos[i-1] = self.elementos[i]
            self.fim -= 1
    
    def obtem_primeiro(self) -> item:
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.elementos[0])
    
    def string(self) -> str:
        s: str = '[ '
        for i in range(self.fim):
            s += '({0}) '.format(self.elementos[i].valor)
        s += ']'
        return s
    
    
    