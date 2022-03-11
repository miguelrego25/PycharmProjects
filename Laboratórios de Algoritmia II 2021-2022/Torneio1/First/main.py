"""

Implemente uma função que, dada uma lista com registos de instantes de tempo e nome de piloto, 
descrevendo os tempos de passagem pela meta dos varios pilotos numa corrida de F1, 
devolva a lista com os nomes dos pilotos com a volta mais rápida ordenada por ordem alfabética. 
Assuma que todos os pilotos iniciaram a prova no instante 0.

"""

def formula1(log):
    dic={}
    list=[]
    dicc ={} #tempo real

    #inicializar os pilotos no dicionario

    if len(log)==0:
        return []

    for tempo,piloto in log:
        dic[piloto] = 500
        dicc[piloto] = 0

    for tempo,piloto in log:
        #atualizar o tempo corrente da volta do piloto
        temporeal = tempo - dicc[piloto]


        if temporeal < dic[piloto]:
            dic[piloto] = temporeal

        dicc[piloto] = tempo

    list =sorted(dic.items(),key = lambda x:x[1])

    fastest = list[0][1]
    finalist =[]
    for x in list:
        if x[1] == fastest:
            finalist.append(x[0])

    finalist.sort()



    return finalist

def main():
    print("<h4>formula1</h4>")
    log = [(20,"Alonso"),(20,"Rosberg"),(30,"Rosberg"),(35,"Rosberg"),(50,"Alonso"),(55,"Hamilton"),(70,"Hamilton"),(80,"Rosberg"),(70,"Alonso"),(100,"Alonso"),(120,"Hamilton")]
    print(formula1(log))


if __name__ == '__main__':
    main()
