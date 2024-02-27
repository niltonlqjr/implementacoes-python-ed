from avl_remocao_simples import *

 
a1=arvore_avl()
a2=arvore_avl()
dados_insere=[1,12,10, 29, 36, 5, 33, 27, 40, 4, 7, 20, 23, 35, 37,42,21,22,23]
dados_busca=[12,10, 22, 36, 5, 33, 27, 40, 4, 7, 20, 23, 35, 37,42,24]
dados_remove=[12,10, 22, 36, 5, 33, 27, 40, 4, 7, 20, 23, 35, 37,42,24,1,29]
#dados = [5,3,9,2,4,7,10,1,2.5,3.5,4.5,6,8,9.5,11]
#dados=[19,2,3,4,5,6,7,8,9,10,11,12,13,20]
val=''

dados = dados_insere

for ch in dados:
    x=item(ch,val)
    a1.insere(x)
    x=item(ch,val)
    a2.insere(x)
    print('===inseriu {0}==='.format(ch))
    print(a1.string())
    print('=================')

dados = dados_busca

for ch in dados:
    x=a1.busca(ch)
    print(x)

dados = dados_remove

for ch in dados:
    a2.remove(ch)
    print('====removeu {0}===='.format(ch))
    print(a2.string())
    print('===================')


       
        




