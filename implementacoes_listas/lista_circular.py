from __future__ import annotations
from dataclasses import dataclass

@dataclass
class item:
    chave: int 
    valor: float 

@dataclass
class no:
    dado: item
    prox: no = None

@dataclass
class lista:
    __ultimo: no = None
  
    def vazia(self) -> bool:
        return self.__ultimo == None

    def __busca(self, chave: int) -> no:
        if self.vazia():
            return None
        ptr = self.__ultimo.prox
        while (ptr != self.__ultimo) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        if ptr.dado.chave == chave:
            return ptr
        else:
            return None

    def insere_ini(self, x: item) -> bool:
        if self.__busca(x.chave) == None:
            novo = no(x)
            if self.vazia():
                self.__ultimo = novo
            else:
                novo.prox = self.__ultimo.prox
            self.__ultimo.prox = novo
            return True
        else:
            return False

    def insere_fim(self, x: item) -> bool:
        inseriu = self.insere_ini(x)
        if inseriu:
            self.__ultimo=self.__ultimo.prox
        return inseriu


    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.__ultimo.prox
            self.__ultimo.prox = rem.prox
            if rem == self.__ultimo:
                self.__ultimo = None
            rem.prox = None
            return True
        return False

    def mostra(self):
        if not self.vazia():
            v = self.__ultimo.prox
            print('[ ',end='')
            while v != self.__ultimo:
                print('(chave={0}, valor={1}) '.format(v.dado.chave, v.dado.valor),end='')
                v = v.prox
            print('((chave={0}, valor={1})) '.format(v.dado.chave, v.dado.valor),end='')
            print(']')
        else:
            print('[ ]')

        


