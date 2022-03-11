
"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def hacker(log):
    dic = {}
    dicnum = {}
    #inicializar o dicionario com zeros

    for a,b in log:
        dic[b] = 0

    for a,b in log:
        dicnum[b] = 0

    for cartao,email in log:
        if dic[email] != 0:
            dic[email] = junta(dic[email], cartao)
        else:
            dic[email] = cartao


    x=sorted (dic.items(),key = lambda x:len(x[1]), reverse=True)

    #conta caracteres * nos numeros de cartao
    for email,cartao in x:
        for numeros in cartao:
            if numeros == "*":
                dicnum[email] += 1
            else:
                continue

    listafinal = []

    for email,cartao in x:
        listafinal.append((cartao, email , dicnum[email]))

    x = sorted(listafinal, key=lambda x: x[1])
    x = sorted (x, key = lambda x: x[2])

    listafinal1=[]

    for a,b,c in x:
        listafinal1.append((a,b))

    return listafinal1


#função que compara o duas strings e devolve o resultado de combinar as duas


def junta (cartao2 ,cartao1 ):
    listavazia = []
    indice= -1

    for a in cartao1:
        indice = indice + 1
        if a == cartao2[indice]:
            listavazia.append(a)
            continue
        if a == "*":
            listavazia.append(cartao2[indice])
            continue
        if cartao2[indice] == "*":
            listavazia.append(a)
            continue
        else:
            listavazia.append(a)


    return ''.join(listavazia)





def main():
    print(" hacker ")
    log = [("****1234********","miguel.com"),
           ("0000************","ze@gmail.com"),
           ("****1111****3333","ze@gmail.com"),
           ("****1234********","maria@mail.pt"),
           ("00001234****3333","m"),]
    print("in:",log)
    print("out:",hacker(log))

if __name__ == '__main__':
    main()
