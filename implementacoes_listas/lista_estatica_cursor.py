import os 
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
queue_dir = os.path.join(dir_path,'../implementacoes_pilha_fila')
sys.path.insert(1,queue_dir)

from dataclasses import dataclass
from fila_estatica_circular import fila
from copy import deepcopy

@dataclass
class item:
    valor: int
    
class no:
    def __init__(self, dado: item):
        self.dado = dado
        self.prox = 0
    
class lista:
    def __init__(self, tamanho:int):
        self.elementos: list[no | None] = [None] * tamanho
        self.tamanho: int = tamanho
        self.primeiro: int = -1
        self.num_itens = 0
        self.disponiveis: fila = fila(tamanho+1)
        for i in range(tamanho):
            self.disponiveis.enfileira(item(i))
        
    def vazia(self) -> bool:
        return self.num_itens == 0
    
    def cheia(self) -> bool:
        return self.num_itens == self.tamanho
    
    def busca_item(self, ch: int) -> item | None:
        pass
    
    def insere_ini(self, x:item) -> bool:
        if not self.cheia():
            np = self.disponiveis.obtem_primeiro().valor
            self.elementos[np] = no(deepcopy(x))
            self.elementos[np].prox = self.primeiro
            self.primeiro = np
            self.num_itens += 1
            self.disponiveis.desenfileira()
            return True
        return False

    def insere_pos(self, x: item, pos: int) -> bool:
        pass
    
    def remove_ini(self) -> bool:
        if not self.vazia():
            p = self.primeiro
            self.primeiro = self.elementos[p].prox
            self.num_itens -= 1
            self.disponiveis.enfileira(item(p))
            return True
        return False
        
    def remove_chave(self, chave: int) -> bool:
        pass
    
    def string(self) -> str:
        x:int = self.primeiro
        str='['
        while x != -1:
            str += '({0})'.format(self.elementos[x].dado.valor)
            x = self.elementos[x].prox
        str+=']'
        return str
            
l=lista(5)
for i in range(8):
    l.insere_ini(item(i))
    print(l.string())

while not l.vazia():
    l.remove_ini()
    print(l.string())

