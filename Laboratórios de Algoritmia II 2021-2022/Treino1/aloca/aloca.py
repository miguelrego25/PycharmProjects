"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto,
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

'''
def aloca(prefs):

    projetos = []
    for key, value in prefs.items():
        if value.issubset(projetos):
            continue
        else:
            projetos + list(value)

    for key,value in prefs.items():
        if (checkavailable(value, projetos)) != 0:
            continue
            #del key,value
        else:
            prefs.pop(key,value )
    for x in projetos:
        print(x)
    return [99999]


# devolve qual o projeto disponivel
def checkavailable(values, projetos):
    for x in projetos:
        for p in values:
            if (x == p):
                return p
        return 0

'''
def aloca(prefs):
    projetos = []

    for x in prefs:
        if (list[x.value])
            list[x.value] =



    return [99999]

def umelempertence(list1, list2):
    for x in list1:
        for y in list 2:
            if (x==y)
