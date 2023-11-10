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


l.insere_fim(item(99,99))
l.mostra()
l.insere_ini(item(-1, -1))
l.mostra()

l.mostra()
print('======REMOCAO======')

l.remove_ini()
l.insere_fim(item(200,5.0))
l.mostra()


while not l.vazia():
    l.remove_ini()
    l.mostra()

chaves=[12,3,8]
for ch in chaves:
    l.insere_fim(item(ch,7.0))
l.mostra()
