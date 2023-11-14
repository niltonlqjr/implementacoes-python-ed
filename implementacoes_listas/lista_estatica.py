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
        self.__elementos = [int()] * tam_max
    
    def busca(self, ch: int) -> int:
        for i in range(self.__tam):
            if self.__elementos[i].chave == ch:
                return i
        return -1

    def insere_fim(self, x: item) -> bool:
        if (self.__tam < self.__tam_max) and (self.busca(x.chave) == -1):
            self.__elementos[self.__tam] = deepcopy(x)
            self.__tam += 1
            return True
        return False

    def insere_pos(self, x: item, pos: int) -> bool:
        if (self.__tam < self.__tam_max) and (pos <= self.__tam) and (self.busca(x.chave) == -1):
            for i in range(self.__tam, pos, -1):
                self.__elementos[i-1] = self.__elementos[i]
            self.__elementos[pos] = deepcopy(x)
            self.__tam += 1
            return True
        return False

    def __desloca(self, pos: int):
        for i in range(pos+1, self.__tam):
            self.__elementos[i-1] = self.__elementos[i]
        

    def remove_fim(self) -> bool:
        if (self.__tam > 0):
            self.__tam -= 1
            return True
        return False

    def remove_pos(self, pos: int) -> bool:
        if (self.__tam > 0):
            self.__desloca(pos)
            return True
        return False
    
    def remove_chave(self, chave: int) -> bool:
        idx_chave = self.busca(chave)
        if idx_chave != -1:
            self.__desloca(idx_chave)
            return True
        return False
    
    def string(self):
        l_str: str = '[ '
        for i in range(self.__tam):
            l_str += '({ch}, {val}) '.format(
                ch=self.__elementos[i].chave,
                val=self.__elementos[i].valor)
        l_str += ']'
        return l_str




    