from pilha_estatica import *

p = pilha(20)

print(p.string())
valores=[9, 8, 3, 1, 7, 4]

print("=======Empilhando=======")
for v in valores:
    p.empilha(item(v))
    print(p.string())

print("=======Consultando topo e Desempilhando=======")    
while not p.vazia():
    print('topo =',p.elemento_topo())
    p.desempilha()
    print(p.string())
    
print("=======Desempilhando (pilha vazia)=======")    
for i in range(3):
    p.desempilha()
 
print("=======Consulta topo (pilha vazia)=======")    
p.elemento_topo()
