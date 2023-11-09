from __future__ import annotations
from dataclasses import *

@dataclass
class item:
    chave: int | None
    valor: float | None

@dataclass
class no:
    dado: item
    prox: no = None

RetornoBusca = item | None

@dataclass
class lista:
    __primeiro: no = no(item(None,None))
    __ultimo: no = __primeiro


    def vazia(self) -> bool:
        return self.__primeiro.prox == None

    def __busca(self, chave: int) -> bool:
        ptr = self.__primeiro.prox
        while (ptr != None) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        return ptr

    def busca_item(self, chave: int) -> RetornoBusca:
        ptr = self.__busca(chave)
        if ptr != None:
            return ptr.dado
        else:
            return None
        
    def insere_ini(self, x: item) -> bool:
        if self.__busca(x.chave) == None:
            novo = no(x)
            novo.prox = self.__primeiro.prox
            if self.vazia():
                self.__ultimo = novo
            self.__primeiro.prox = novo
            return True
        else:
            return False

    def insere_fim(self, x: item) -> bool:
        if self.__busca(x.chave) == None:
            novo = no(x)
            self.__ultimo.prox = novo
            novo.prox=None
            self.__ultimo=novo
            return True
        else:
            return False

    def insere_pos(self, x: item, pos: int) -> bool:
        i=0
        ptr=self.__primeiro
        if self.__busca(x.chave) == None:
            while ptr!=None and i<pos:
                ptr=ptr.prox
                i+=1
            if ptr!=None:
                novo=no(x)
                novo.prox = ptr.prox
                if novo.prox == None:
                    self.__ultimo=novo
                ptr.prox=novo
                return True
        return False

    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.__primeiro.prox
            self.__primeiro.prox = rem.prox
            if self.vazia():
                self.__ultimo = self.__primeiro
            rem.prox = None
            return True
        return False

    def remove_chave(self, chave: int) -> bool:
        ptr=self.__primeiro
        while ptr.prox!=None and ptr.prox.dado.chave != chave:
            ptr=ptr.prox
        if ptr.prox!=None:
            paux=ptr.prox
            ptr.prox = paux.prox
            if ptr.prox == None:
                self.__ultimo = ptr
            paux.prox = None
            return True
        return False    

    def mostra_lista(self):
        v = self.__primeiro.prox
        print('[ ',end='')
        while v != None:
            print('(chave={0},valor={1}) '.format(v.dado.chave, v.dado.valor),end='')
            v = v.prox
        print(']')



