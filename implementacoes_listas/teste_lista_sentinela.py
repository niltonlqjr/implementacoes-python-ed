from lista_sentinela import *

l=lista()


print('======INSERCAO=======')
chaves=[1,3,5]
for ch in chaves:
    l.insere_ini(item(ch,0.0))

l.mostra_lista()

chaves=[9,4,8,2]
for ch in chaves:
    l.insere_fim(item(ch,1.0))
l.mostra_lista()

chavesp=[(7,0), (6,8)]
for ch,p in chavesp:
    l.insere_pos(item(ch,3.0),p)
l.mostra_lista()

l.insere_fim(item(99,99))
l.mostra_lista()
l.insere_ini(item(-1, -1))
l.mostra_lista()

l.mostra_lista()
print('======REMOCAO======')

l.remove_chave(99)
l.mostra_lista()

l.insere_fim(item(200,5.0))
l.mostra_lista()


while not l.vazia():
    l.remove_ini()
    l.mostra_lista()

chaves=[12,3,8]
for ch in chaves:
    l.insere_fim(item(ch,7.0))
l.mostra_lista()


item1 = l.busca_item(45)
print(item1)
item2 = l.busca_item(3)
print(item2)