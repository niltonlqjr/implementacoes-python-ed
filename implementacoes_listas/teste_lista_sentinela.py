from lista_sentinela import *

l=lista()


print('======INSERCAO=======')
chaves=[1,3,5]
for ch in chaves:
    l.insere_ini(item(ch,0.0))

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
l.insere_ini(item(-1, -1))
print(l.string())

print(l.string())
print('======REMOCAO======')

l.remove_chave(99)
print(l.string())

l.insere_fim(item(200,5.0))
print(l.string())


while not l.vazia():
    l.remove_ini()
    print(l.string())

print('======INSERCAO======')
chaves=[12,3,8]
for ch in chaves:
    l.insere_fim(item(ch,7.0))
    print(l.string())

print('======BUSCA======')
item1 = l.busca_item(45)
print(item1)
item2 = l.busca_item(3)
print(item2)

item2.chave = 99999

print(l.string())