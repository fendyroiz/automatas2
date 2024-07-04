
def load_sustantivos_sentimientos():
    fid = open('Recursos/adjetivos.txt')
    sustantivo = dict()
    lista = list()
    sustantivo["sentimientos"]= {}
    
    for line in fid:
        for l in line.split(','):
            lista.append(l)
    sustantivo['sentimientos'] = lista
    
    print(sustantivo)
    
    fid.close()

load_sustantivos_sentimientos()

def load_sustantivos_fisicos():
    fid = open('Recursos/obejetos_fisicos.txt')
    sustantivo = dict()
    lista = list()
    sustantivo["sentimientos"]= {}
    
    for line in fid:
        for l in line.split(','):
            lista.append(l)
    sustantivo['sentimientos'] = lista
    
    print(sustantivo)
    
    fid.close()

load_sustantivos_fisicos()