'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade:
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos).
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade,
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):

    dic = {}
    criticrua = {}

    '''for rua in ruas:
        for letras in rua:
            if letras in dic:
                dic[letras] += 1
            else:
                dic[letras] = 1
     
     '''

#ve numero de ocurrencias de letras em toda a lista
    for rua in ruas:
        criticrua[rua] = 0

    for rua in ruas:
        for letras in rua:
            criticrua[rua] += dic[letras]
 



    #cria um segundo dicionario com o nome das ruas e a sua criticidade

    x=sorted(dic.items())
    x= filter(lambda x: x[1] != 1,x)
    p=sorted(x, key=lambda x: x[1], reverse=False)

    return p




    #ir a cada palavra e retirar o primeiro e ultimo carater e colocar em list




def main():
    print("<h3>cruzamentos</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa","q"]
    print("in:",ruas)
    print("out:",cruzamentos(ruas))

if __name__ == '__main__':
    main()

'''def cruzamentos(ruas):

    list = []
    temp = []

    dic = {}

    for x in ruas:
        temp = x.split()
        list.append(temp[0]).append(temp[-1])
    #ir a cada palavra e retirar o primeiro e ultimo carater e colocar em list

    list.sort
    for y in list:
        if y in dic:
            dic[y] += 1
        else:
            dic[y] = 1
    #colocar os elementos do list num dicionarios com key o caracter e value a quantidade de ocurrencias desse caracter


    return [('z',99)]

'''
'''

    list = []
    temp = []

    dic = {}

    for x in ruas:
        temp = x.split()
        list.append(temp[0]).append(temp[-1])
    #ir a cada palavra e retirar o primeiro e ultimo carater e colocar em list

    list.sort
    for y in list:
        if y in dic:
            dic[y] += 1
        else:
            dic[y] = 1
    #colocar os elementos do list num dicionarios com key o caracter e value a quantidade de ocurrencias desse caracter

'''