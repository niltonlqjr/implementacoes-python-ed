from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    chave: int
    valor: float

class lista:
    def __init__(self, tamanho: int):
        self.tam: int = 0
        self.tam_max: int = tamanho
        self.elementos: list[item | None] = [None] * tamanho
    
    def vazia(self) -> bool:
        return self.tam == 0
    
    def cheia(self) -> bool:
        return self.tam == self.tam_max

    def busca(self, ch: int) -> int:
        for i in range(self.tam):
            if self.elementos[i].chave == ch:
                return i
        return -1

    def busca_item(self, ch: int) -> item | None:
        idx = self.busca(ch)
        if idx != -1:
            return deepcopy(self.elementos[idx])
        else:
            return None

    def insere_fim(self, x: item) -> bool:
        if (not self.cheia()) and (self.busca(x.chave) == -1):
            self.elementos[self.tam] = deepcopy(x)
            self.tam += 1
            return True
        return False

    def insere_pos(self, x: item, pos: int) -> bool:
        if (not self.cheia()) and (pos <= self.tam) and (self.busca(x.chave) == -1):
            for i in range(self.tam, pos, -1):
                self.elementos[i] = self.elementos[i-1]
            self.elementos[pos] = deepcopy(x)
            self.tam += 1
            return True
        return False

    def __desloca(self, pos: int):
        for i in range(pos+1, self.tam):
            self.elementos[i-1] = self.elementos[i]
        

    def remove_fim(self) -> bool:
        if not self.vazia():
            self.tam -= 1
            return True
        return False

    def remove_pos(self, pos: int) -> bool:
        if not self.vazia():
            self.__desloca(pos)
            return True
        return False
    
    def remove_chave(self, chave: int) -> bool:
        idx_chave = self.busca(chave)
        if idx_chave != -1:
            self.__desloca(idx_chave)
            return True
        return False
    
    def string(self) -> str:
        l_str: str = '[ '
        for i in range(self.tam):
            l_str += '({ch}, {val}) '.format(
                ch=self.elementos[i].chave,
                val=self.elementos[i].valor)
        l_str += ']'
        return l_str




    