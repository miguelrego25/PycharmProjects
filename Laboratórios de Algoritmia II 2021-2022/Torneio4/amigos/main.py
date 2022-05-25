'''

Implemente uma função que descubra o maior conjunto de pessoas que se conhece
mutuamente. A função recebe receber uma sequências de pares de pessoas que se
conhecem e deverá devolver o tamanho do maior conjunto de pessoas em que todos
conhecem todos os outros.


//        30%
def amigos(conhecidos):
    dic = {}
    for primeiro, segundo in conhecidos:
        if primeiro not in dic:
            dic[primeiro] = 0
        if segundo not in dic:
            dic[segundo] = 0
        if primeiro == segundo:
            dic[primeiro] -=2
        if primeiro in dic:
            dic[primeiro] += 1
        if segundo in dic:
            dic[segundo] += 1
    list = dic.values()
    list = sorted(list, reverse=True)
    print(list)
    return list[0]

def first(h):


def next(h, c):

def valid(h, c):


def main(conhecidos):

    c = first(conhecidos)
    while (c != None):
        if valid(conhecidos,c):
            return c
        c = next(conhecidos,c)




def checknames(nome, conhecidos,verif):
    count = 0
    for primeiro, segundo in conhecidos:
        if primeiro == segundo:
            count += 0
        elif primeiro == nome or segundo == nome and primeiro not in verif or segundo not in verif:
            if primeiro == nome:
                verif.append(primeiro)
                count += 1
            elif segundo == nome:
                verif.append(segundo)
                count += 1
    return count


def amigos(conhecido):
    conhecidos = list(conhecido)
    dic = {}
    nameschecked = []
    maxi = 0

    for primeiro,segundo in conhecidos:

        if primeiro == segundo:
            maxi += 0
        elif primeiro not in nameschecked:
            s = checknames(primeiro,conhecidos[1:],[])
            s += 1
            if maxi < s:
                maxi = s
            nameschecked.append(primeiro)
        if segundo not in nameschecked:
            s=checknames(segundo,conhecidos[1:],[])
            s += 1
            if maxi < s:
                maxi = s
            nameschecked.append(segundo)
    return maxi
'''

def searchconhecidos(primeiro,conhecidos):
    listamigos = []
    for fstnome,scdnome in conhecidos:
        if fstnome != scdnome:
            if primeiro == scdnome and fstnome not in listamigos:
                listamigos.append(fstnome)
            if primeiro == fstnome and scdnome not in listamigos:
                listamigos.append(scdnome)
    return listamigos

def amigos(s):
    conhecidos = list(s)
    dic = {}
    max = 0

    for fstnome,scdnome in conhecidos:
        if fstnome != scdnome:
            if fstnome not in dic.keys():
                dic[fstnome] = searchconhecidos(fstnome, conhecidos)
            if scdnome not in dic.keys():
                dic[scdnome] = searchconhecidos(scdnome, conhecidos)

    print(dic )
    newlist = sorted(dic.items(), key=lambda x: len(x[1]), reverse=True)
    return len(newlist[0][1])



def main():
    print("<h3>amigos</h3>")
    conhecidos = conhecidos = {('pedro', 'maria'), ('pedro', 'jose'), ('pedro', 'manuel'), ('maria', 'jose'), ('maria', 'francisca'), ('jose', 'francisca'), ('francisca', 'manuel')}
    print("in:", conhecidos)
    print("out:", amigos(conhecidos))


if __name__ == '__main__':
    main()
