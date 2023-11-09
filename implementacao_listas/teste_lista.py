from lista_ligada import *

l=lista()


print('======INSERCAO=======')
chaves=[1,3,5]
for ch in chaves:
    insere_ini(l,item(ch,0.0))

mostra_lista(l)

chaves=[9,4,8,2]
for ch in chaves:
    insere_fim(l,item(ch,1.0))
mostra_lista(l)

chavesp=[(7,0), (6,8)]
for ch,p in chavesp:
    insere_pos(l,item(ch,3.0),p)
mostra_lista(l)

insere_fim(l,item(99,99))
mostra_lista(l)
insere_ini(l,item(-1, -1))
mostra_lista(l)

mostra_lista(l)
print('======REMOCAO======')

remove_chave(l,99)
mostra_lista(l)

insere_fim(l,item(200,5.0))
mostra_lista(l)


while not vazia(l):
    remove_ini(l)
    mostra_lista(l)

chaves=[12,3,8]
for ch in chaves:
    insere_fim(l,item(ch,7.0))
mostra_lista(l)
