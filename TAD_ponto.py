from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ponto:
    __x: float # o VSCode esta indicando erro em atributos ocultos, porem esta funcionando
    __y: float

    def imprime(self):
        print('(',self.__x,',',self.__y,')',sep='')
        
    def valor_x(self) -> float:
        return self.__x

    def valor_y(self) -> float:
        return self.__y
    
    def altera_x(self, novo_x: float):
        self.__x = novo_x
        
    def altera_y(self, novo_y: float):
        self.__y = novo_y
    
    def distancia(self, q: ponto) -> float:
        return ((self.__x - q.valor_x())**2 + (self.__y - q.valor_y())**2) ** (1/2)
    
p1=ponto(1,1)
p2=ponto(4,5)
print(p1.distancia(p2))
p1.imprime()
p2.imprime()

p1.altera_x(9)
p1.altera_y(11)

p1.imprime()
p2.imprime()