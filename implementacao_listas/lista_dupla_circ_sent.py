class item:
    def __init__(self, ch, val):
        self.chave=ch
        self.valor=val

class no:
    def __init__(self):
        self.dado=None
        self.prox=None
        self.ant=None

class lista:
    def __init__(self):
        self.primeiro = no()
        self.primeiro.prox = self.primeiro
        self.primeiro.ant = self.primeiro
  
def vazia(l):
    return l.primeiro.prox == l.primeiro

def busca(l, chave):
    ptr = l.primeiro.prox
    while (ptr != l.primeiro) and (ptr.dado.chave != chave):
        ptr = ptr.prox
    if ptr != l.primeiro:
        return ptr
    else:
        return None

 

def insere_ini(l,x):
    if busca(l,x.chave) == None:
        novo = no()
        novo.dado = x
        novo.prox = l.primeiro.prox
        novo.ant = l.primeiro
        l.primeiro.prox.ant = novo
        l.primeiro.prox = novo
        return True
    else:
        return False

def insere_fim(l,x):
    if busca(l,x.chave) == None:
        ult = l.primeiro.ant
        novo = no()
        novo.dado = x
        novo.prox = ult.prox
        ult.prox.ant = novo
        novo.ant = ult
        ult.prox = novo
        return True
    else:
        return False

def insere_pos(l,pos,x):
    if busca(l,x.chave) == None:
        aux = l.primeiro
        cont=0
        while (cont < pos) and (aux != l.primeiro.ant):
            cont += 1
            aux = aux.prox
        if cont == pos:
            #insere_frente(l,atu,x)
            novo = no()
            novo.dado = x
            novo.prox = aux.prox
            novo.ant = aux
            aux.prox.ant = novo
            aux.prox = novo
            return True
    return False
        
def remove_ini(l):
    if not vazia(l):
        rem = l.primeiro.prox
        l.primeiro.prox = rem.prox
        rem.prox.ant = l.primeiro
        rem.prox = None
        rem.ant = None
        return True
    else:
        return False

def remove_chave(l,chave):
    rem = busca(l,chave)
    if rem != None:
        rem.prox.ant = rem.ant
        rem.ant.prox = rem.prox
        rem.prox = None
        rem.ant = None
        return True
    else:
        return False
    

def mostra_lista(l):
    v = l.primeiro.prox
    print('[ ',end='')
    while v != l.primeiro:
        print('({0},{1}) '.format(v.dado.chave, v.dado.valor),end='')
        v = v.prox
    print(']')




