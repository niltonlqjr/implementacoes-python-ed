from lista_estatica import *

l=lista(20)


print('======INSERCAO=======')
chaves=[1,3,5]
for ch in chaves:
    l.insere_pos(item(ch,0.0), 0)
    print(l.string())

chaves=[9,4,8,2]
for ch in chaves:
    l.insere_fim(item(ch,1.0))
print(l.string())

chavesp=[(7,0), (6,8)]
for ch,p in chavesp:
    l.insere_pos(item(ch,3.0),p)
print(l.string())

l.insere_fim(item(99,99))
print(l.string())
l.insere_pos(item(-1, -1), 0)
print(l.string())

print(l.string())
print('======REMOCAO======')

l.insere_fim(item(200,5.0))
print(l.string())


while not l.vazia():
    l.remove_fim()
    print(l.string())

chaves=[12,3,8]
for ch in chaves:
    l.insere_fim(item(ch,7.0))
print(l.string())

print("=======BUSCA=======")

it1 = l.busca_item(45)
print(it1)

it2 = l.busca_item(8)
print(it2)

it2.chave=99999999999
print(l.string())