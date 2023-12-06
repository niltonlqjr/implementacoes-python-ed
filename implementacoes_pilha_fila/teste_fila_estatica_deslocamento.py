from fila_estatica_deslocamento import *

f = fila(10)

vals = [1,8,4,9,3,7]


print("============enfileirar elementos==============")
for v in vals:
    f.enfileira(item(v))
    print(f.string())

print("======consultar primeiro e desenfileirar elementos======")
while not f.vazia():
    print('primeiro da fila:',f.obtem_primeiro())
    f.desenfileira()
    print(f.string())


print("============desenfileirar (fila vazia)==============")
f.desenfileira()

print("============consultar primeiro(fila vazia)==============")
f.obtem_primeiro()
