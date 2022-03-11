'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''

def tabela(jogos):
    dic = {}
    dif = {}
    finaldic = {}

    #adicionar todas as equipas a um dicionario
    for a,b,c,d in jogos:
        dic[a] = 0
        dic[c] = 0
        dif[a] = 0
        dif[c] = 0
        finaldic[a] = 0
        finaldic[c] = 0


    #adicionar pontos e diferença de golos as equipas

    for a,b,c,d in jogos:

        if b>d:
            dic[a] += 3
        if b<d:
            dic[c] += 3
        if b == d :
            dic[a] += 1
            dic[c] += 1

        dif[a] += b-d
        dif[c] += d-b


    x = sorted(dic.items(), key = lambda x: x[0])

    for a,b in x:
        finaldic[a] = (dic[a],dif[a])
    print(finaldic.items())
    x = finaldic.items()
    x=sorted(x)
    x=sorted(x, key=lambda y: y[1][1], reverse=True)
    x=sorted(x, key=lambda y: y[1][0], reverse=True)

    emptylist = []
    for a,b in x:
        emptylist.append((a, b[0]))
    return emptylist





##
# Main function of the Python program.
#
##


def main():
    print("<h3>tabela</h3>")
    jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
    print("in:",jogos)
    print("out:",tabela(jogos))

if __name__ == '__main__':
    main()
