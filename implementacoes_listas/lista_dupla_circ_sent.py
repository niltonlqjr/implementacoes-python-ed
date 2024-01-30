from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    chave: int | None
    valor: float | None


class no:
    def __init__(self,x: item):
        self.dado: item = x
        self.prox: no | None = None
        self.ant: no | None = None


class lista:
    def __init__(self):
        self.primeiro = no(item(None, None))
        self.primeiro.prox = self.primeiro
        self.primeiro.ant = self.primeiro
    
    def vazia(self) -> bool:
        return self.primeiro.prox == self.primeiro

    def busca(self, chave) -> no | None:
        ptr = self.primeiro.prox
        while (ptr != self.primeiro) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        if ptr != self.primeiro:
            return ptr
        else:
            return None


    def busca_item(self, chave: int) -> item | None:
        ptr = self.busca(chave)
        if ptr != None:
            return deepcopy(ptr.dado)
        else:
            return None

    def insere_ini(self, x: item) -> bool:
        if self.busca(x.chave) == None:
            novo = no(deepcopy(x))
            novo.prox = self.primeiro.prox
            novo.ant = self.primeiro
            self.primeiro.prox.ant = novo
            self.primeiro.prox = novo
            return True
        else:
            return False

    def insere_fim(self, x: item) -> bool:
        if self.busca(x.chave) == None:
            ult = self.primeiro.ant
            novo = no(deepcopy(x))
            novo.prox = ult.prox
            ult.prox.ant = novo
            novo.ant = ult
            ult.prox = novo
            return True
        else:
            return False

    def insere_pos(self, x: item, pos: int) -> bool:
        if self.busca(x.chave) == None:
            aux = self.primeiro
            cont=0
            while (cont < pos) and (aux != self.primeiro.ant):
                cont += 1
                aux = aux.prox
            if cont == pos:
                novo = no(deepcopy(x))
                novo.prox = aux.prox
                novo.ant = aux
                aux.prox.ant = novo
                aux.prox = novo
                return True
        return False
            
    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.primeiro.prox
            self.primeiro.prox = rem.prox
            rem.prox.ant = self.primeiro
            rem.prox = None
            rem.ant = None
            return True
        else:
            return False

    def remove_chave(self, chave: int) -> bool:
        rem = self.busca(chave)
        if rem != None:
            rem.prox.ant = rem.ant
            rem.ant.prox = rem.prox
            rem.prox = None
            rem.ant = None
            return True
        else:
            return False

    def string(self) -> str:
        v: no = self.primeiro.prox
        l_str: str = '[ '
        while v != self.primeiro:
            l_str += '({0}, {1}) '.format(v.dado.chave, v.dado.valor)
            v = v.prox
        l_str += ']'
        return l_str