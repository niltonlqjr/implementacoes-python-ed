from lista_circular import *

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


l.insere_fim(item(99,99))
print(l.string())
l.insere_ini(item(-1, -1))
print(l.string())

print(l.string())
print('======REMOCAO======')

l.remove_ini()
l.insere_fim(item(200,5.0))
print(l.string())


while not l.vazia():
    l.remove_ini()
    print(l.string())

print('======INSERCAO=======')
chaves=[12,3,8]
for ch in chaves:
    l.insere_fim(item(ch,7.0))
    print(l.string())

print('======BUSCA=======')
it1 = l.busca_item(45)
print(it1)

it2 = l.busca_item(8)
print(it2)

it2.chave=99999999999
print(l.string())
