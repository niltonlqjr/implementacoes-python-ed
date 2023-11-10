from lista_circular import *

l=lista()


print('======INSERCAO=======')
chaves=[1,3,5]
for ch in chaves:
    l.insere_ini(item(ch,0.0))
    l.mostra()

chaves=[9,4,8,2]
for ch in chaves:
    l.insere_fim(item(ch,1.0))
l.mostra()

print('======REMOCAO======')


while not l.vazia():
    l.remove_ini()
    l.mostra()

chaves=[12,3,8]
for ch in chaves:
    l.insere_fim(item(ch,7.0))
l.mostra()

it1 = l.busca_item(45)
print(it1)

it2 = l.busca_item(8)
print(it2)

it2.chave=99999999999
l.mostra()



