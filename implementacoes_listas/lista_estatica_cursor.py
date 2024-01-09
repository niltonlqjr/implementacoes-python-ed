import os 
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
queue_dir = os.path.join(dir_path,'../implementacoes_pilha_fila')
sys.path.insert(1,queue_dir)

'''acima estao os imports e declaracoes para colocar o caminho
   da implementacao da fila na variavel de ambiente path'''
   
from dataclasses import dataclass
from fila_estatica_circular import fila
from copy import deepcopy

@dataclass
class item:
    chave: int
    valor: float

    
class no:
    def __init__(self, dado: item):
        self.dado = dado
        self.prox = -1
    
class lista:
    def __init__(self, tamanho:int):
        self.elementos: list[no | None] = [None] * tamanho
        self.tamanho_maximo: int = tamanho
        self.primeiro: int = -1
        self.num_itens = 0
        self.disponiveis: fila = fila(tamanho+1)
        for i in range(tamanho):
            self.disponiveis.enfileira(i)
        
    def vazia(self) -> bool:
        return self.num_itens == 0
    
    def cheia(self) -> bool:
        return self.disponiveis.vazia()
    
    def busca(self, ch: int) -> int:
        c: int = self.primeiro
        while c != -1 and self.elementos[c].dado.chave != ch:
            c = self.elementos[c].prox
        return c

    def busca_item(self, ch: int) -> item | None:
        idx = self.busca(ch)
        print(idx)
        if idx != -1:
            return deepcopy(self.elementos[idx].dado)
        else:
            return None
    
    def insere_ini(self, x:item) -> bool:
        if not self.cheia() and self.busca(x.chave) == -1:
            pos: int = self.disponiveis.obtem_primeiro()
            self.elementos[pos] = no(deepcopy(x))
            self.elementos[pos].prox = self.primeiro
            self.primeiro = pos
            self.num_itens += 1
            self.disponiveis.desenfileira()
            return True
        return False

    def insere_fim(self, x:item) -> bool:
        return self.insere_pos(x,self.num_itens)

    def insere_pos(self, x: item, pos: int) -> bool:
        if not self.cheia() and self.busca(x.chave) == -1:
            if pos == 0:
                return self.insere_ini(x)
            else:
                p: int = self.disponiveis.obtem_primeiro()
                cur: int = self.primeiro
                cont: int = 1
                while cur != -1 and cont < pos:
                    cur = self.elementos[cur].prox
                    cont += 1
                if cur != -1:
                    self.elementos[p] = no(deepcopy(x))
                    self.elementos[p].prox = self.elementos[cur].prox
                    self.elementos[cur].prox = p
                    self.num_itens += 1
                    self.disponiveis.desenfileira()
                    return True
        return False

        
    def remove_ini(self) -> bool:
        if not self.vazia():
            p = self.primeiro
            self.primeiro = self.elementos[p].prox
            self.num_itens -= 1
            self.disponiveis.enfileira(p)
            return True
        return False

    def remove_pos(self, pos: int) -> bool:
        if not self.vazia():    
            if pos == 0:
                return self.remove_ini()
            else:
                cont: int = 0
                cur: int = self.primeiro
                while cur != -1 and cont < pos-1:
                    cur = self.elementos[cur].prox
                    cont += 1
                if self.elementos[cur].prox != -1:
                    d = self.elementos[cur].prox
                    self.elementos[cur].prox = self.elementos[d].prox
                    self.num_itens -= 1
                    self.disponiveis.enfileira(d)
                    return True
        return False


    def remove_chave(self, ch: int) -> bool:
        if not self.vazia():
            pos:int = self.primeiro
            if self.elementos[pos].dado.chave == ch:
                self.remove_ini()
            else:
                while pos != -1 and self.elementos[pos].dado.chave != ch:
                    ant: int = pos
                    pos = self.elementos[pos].prox
                if pos != -1:
                    self.elementos[ant].prox = self.elementos[pos].prox
                    self.num_itens -= 1
                    self.disponiveis.enfileira(pos)
                    return True
        return False

    def remove_fim(self) -> bool:
        if not self.vazia():
            return self.remove_pos(self.num_itens-1)
        return False
    
    def string(self) -> str:
        c:int = self.primeiro
        str='['
        while c != -1:
            e: item = self.elementos[c].dado
            str += '({0}, {1})'.format(e.chave, e.valor)
            c = self.elementos[c].prox
        str+=']'
        return str
