from __future__ import annotations
from dataclasses import dataclass

@dataclass
class item:
    chave: int | None
    valor: float | None

@dataclass
class no:
    dado: item
    prox: no = None
    ant: no = None

@dataclass
class lista:
    __primeiro: no = None

    def __post_init__(self):
        self.__primeiro = no(item(None, None))
        self.__primeiro.prox = self.__primeiro
        self.__primeiro.ant = self.__primeiro
    
    def vazia(self) -> bool:
        return self.__primeiro.prox == self.__primeiro

    def __busca(self, chave) -> no:
        ptr = self.__primeiro.prox
        while (ptr != self.__primeiro) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        if ptr != self.__primeiro:
            return ptr
        else:
            return None

    def busca_item(self, chave: int):
        ptr = self.__busca(chave)
        if ptr != None:
            return item(ptr.dado.chave, ptr.dado.valor)
        else:
            return None

    def insere_ini(self, x: item) -> bool:
        if self.__busca(x.chave) == None:
            novo = no(x)
            novo.prox = self.__primeiro.prox
            novo.ant = self.__primeiro
            self.__primeiro.prox.ant = novo
            self.__primeiro.prox = novo
            return True
        else:
            return False

    def insere_fim(self, x: item) -> bool:
        if self.__busca(x.chave) == None:
            ult = self.__primeiro.ant
            novo = no(x)
            novo.prox = ult.prox
            ult.prox.ant = novo
            novo.ant = ult
            ult.prox = novo
            return True
        else:
            return False

    def insere_pos(self, x: item, pos: int) -> bool:
        if self.__busca(x.chave) == None:
            aux = self.__primeiro
            cont=0
            while (cont < pos) and (aux != self.__primeiro.ant):
                cont += 1
                aux = aux.prox
            if cont == pos:
                novo = no(x)
                novo.prox = aux.prox
                novo.ant = aux
                aux.prox.ant = novo
                aux.prox = novo
                return True
        return False
            
    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.__primeiro.prox
            self.__primeiro.prox = rem.prox
            rem.prox.ant = self.__primeiro
            rem.prox = None
            rem.ant = None
            return True
        else:
            return False

    def remove_chave(self, chave: int) -> bool:
        rem = self.__busca(chave)
        if rem != None:
            rem.prox.ant = rem.ant
            rem.ant.prox = rem.prox
            rem.prox = None
            rem.ant = None
            return True
        else:
            return False

    def mostra(self):
        v = self.__primeiro.prox
        print('[ ',end='')
        while v != self.__primeiro:
            print('(chave={0}, valor={1}) '.format(v.dado.chave, v.dado.valor),end='')
            v = v.prox
        print(']')




