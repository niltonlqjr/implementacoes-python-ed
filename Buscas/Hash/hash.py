from dataclasses import dataclass
from lista_ligada import lista
from lista_ligada import item

class hash:
    def __init__(self, m: int = 1001):
        self.tamanho: int = m
        self.dados: list[lista] = [lista() for i in range(self.tamanho)]
    
    def funcao_hash(self, chave: int):
        return chave % self.tamanho
    
    def busca(self, chave: int) -> item | None:
        idx = self.funcao_hash(chave)
        item = self.dado[idx].busca_item(chave)
        return item

    def insere(self, x: item) -> bool:
        idx = self.funcao_hash(x.chave)
        return self.dados[idx].insere_fim(x)
    
    def remove(self, chave: int) -> bool:
        idx = self.funcao_hash(chave)
        return self.dados[idx].remove_chave(chave)
    
    def string(self) -> str:
        str = ''
        for i in range(self.tamanho):
            str += '[{0}] -> '.format(i)
            str += self.dados[i].string()
            str += '\n'
        return str