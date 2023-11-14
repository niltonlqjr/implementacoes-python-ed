from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    chave: int
    valor: float

@dataclass
class lista:
    __tam_max: int
    __elementos: list[item]
    __tam: int

    def __init__(self, tam_max: int):
        self.__tam = 0
        self.__tam_max = tam_max
        self.__elementos = [None] * tam_max
    
    def vazia(self) -> bool:
        return self.__tam == 0
    
    def cheia(self) -> bool:
        return self.__tam == self.__tam_max

    def busca(self, ch: int) -> int:
        for i in range(self.__tam):
            if self.__elementos[i].chave == ch:
                return i
        return -1

    def busca_item(self, ch: int) -> item | None:
        idx = self.busca(ch)
        if idx != -1:
            return deepcopy(self.__elementos[idx])
        else:
            return None

    def insere_fim(self, x: item) -> bool:
        if (not self.cheia()) and (self.busca(x.chave) == -1):
            self.__elementos[self.__tam] = deepcopy(x)
            self.__tam += 1
            return True
        return False

    def insere_pos(self, x: item, pos: int) -> bool:
        if (not self.cheia()) and (pos <= self.__tam) and (self.busca(x.chave) == -1):
            for i in range(self.__tam, pos, -1):
                self.__elementos[i] = self.__elementos[i-1]
            self.__elementos[pos] = deepcopy(x)
            self.__tam += 1
            return True
        return False

    def __desloca(self, pos: int):
        for i in range(pos+1, self.__tam):
            self.__elementos[i-1] = self.__elementos[i]
        

    def remove_fim(self) -> bool:
        if not self.vazia():
            self.__tam -= 1
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
        for i in range(self.__tam):
            l_str += '({ch}, {val}) '.format(
                ch=self.__elementos[i].chave,
                val=self.__elementos[i].valor)
        l_str += ']'
        return l_str




    