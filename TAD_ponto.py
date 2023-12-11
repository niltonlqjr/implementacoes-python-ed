from __future__ import annotations

class ponto:
    def __init__(self, coordx: float, coordy: float):
        self.x: float = coordx
        self.y: float = coordy

    def imprime(self):
            print('(',self.x,',',self.y,')',sep='')

    def valor_x(self) -> float:
            return self.x
    
    def altera_x(self, novo_x: float):
            self.x = novo_x
    
    def imprime(self):
        print('(',self.x,',',self.y,')',sep='')
        
    def distancia(self, q: ponto) -> float:
        return ((self.x - q.x)**2 + (self.y - q.y)**2) ** (1/2)


p1=ponto(1,1)
p2=ponto(4,5)
print(p1.distancia(p2))
p1.imprime()
p2.imprime()