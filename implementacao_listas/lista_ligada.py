from __future__ import annotations
from dataclasses import dataclass

@dataclass
class item:
    chave: int
    valor: float

@dataclass
class no:
    dado: item
    prox: no = None #erro no mypy que não sei como resolver
                    #tentei criar uma union "no | None"
                    #porém o erro passa a ser algo no sentido dos campos
                    #não existirem no tipo none

@dataclass
class lista:
    __primeiro: no = None
    __ultimo: no = None
    
    def vazia(self):
        return self.__primeiro == None
    
    def __busca(self, chave:int) -> no:
        ptr = self.__primeiro
        while (ptr != None) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        return ptr
    
    def busca_item(self, chave:int) -> item | None:
        ptr = self.__busca(chave)
        if ptr != None:
            return item(ptr.dado.chave, ptr.dado.valor)
        else:
            return None
    
    def insere_ini(self, x:item) -> bool:
        if self.__busca(x.chave) == None:
            novo = no(x)
            if self.vazia():
                self.__ultimo = novo
            novo.prox = self.__primeiro
            self.__primeiro=novo
            return True
        else:
            return False

    def insere_fim(self, x:item) -> bool:
        if self.__busca(x.chave) == None:
            novo = no(x)
            if self.vazia():
                self.__primeiro=novo
            else:
                self.__ultimo.prox=novo
            novo.prox=None
            self.__ultimo=novo
            return True
        else:
            return False

    def insere_pos(self, x:item, pos:int) -> bool:
        i=0
        ptr=self.__primeiro
        if pos == 0:
            return self.insere_ini(x)
        elif self.__busca(x.chave) == None:
            while ptr!=None and i<pos-1:
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

    def remove_ini(self):
        if not self.vazia():
            rem = self.__primeiro
            self.__primeiro = self.__primeiro.prox
            if self.vazia():
                self.__ultimo = None
            rem.prox = None
            return True
        return False


    def remove_chave(self, chave: int) -> bool:
        ptr=self.__primeiro
        if not self.vazia():
            if ptr.dado.chave == chave:
                return self.remove_ini()
            while ptr.prox != None and ptr.prox.dado.chave != chave:
                ptr=ptr.prox
            if ptr.prox != None:
                exc = ptr.prox
                ptr.prox = exc.prox
                if ptr.prox == None:
                    self.__ultimo=exc
                exc.prox=None
                return True
        return False

    def mostra(self):
        v = self.__primeiro
        print('[ ',end='')
        while v != None:
            print('(chave={0},valor={1}) '.format(v.dado.chave, v.dado.valor),end='')
            v = v.prox
        print(']')
        

    


