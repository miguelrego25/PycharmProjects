"""

Implemente uma função que dada uma sequência de inteiros, determinar o
comprimento da maior sub-sequência (não necessariamente contígua) que se
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.



def crescente(lista):
    dic = {}
    if lista == 0:
        return 0
    results = []
    for i in range(len(lista)):
        results.append(biggrz(lista[i:], dic))
    return max(results)


def biggrz(rtlista,dic):
    x = []
    for i in range(len(rtlista)):
        if rtlista[0] < rtlista [i]:
            x.append(biggrz(rtlista[i:]))
    return 1+max([0] + x)



def crescente(lista):
    dict = {}
    valores = []
    if lista == []:
        return 0
    for i in reversed(list(range(len(lista)))):
        m = lista[i]
        aux = lista[i]
        if i == len(lista)-1:
            valores.append(1)
            dict[lista[i]] = 1
        else:
            for elem in lista[i:]:
                if lista[i] < elem:
                    m = elem
                    break
            if m in dict:
                valores.append(1 + dict[m])
                dict[lista[i]] = 1 + dict[m]
            else:
                valores.append(1)
                dict[lista[i]] = 1
    return max(valores)
"""


# def memo(incompleta) -> 60%
def crescenteMemo(lista, o, acc):
    if o >= len(lista) - 1:
        return 1
    elif o in acc:
        return acc[o]
    else:
        i = o + 1
        while i < len(lista):
            if lista[o] <= lista[i]:
                return crescenteMemo(lista, i, acc) + 1
            i += 1


def crescente2(lista):
    acc = {}
    for i in range(0, len(lista)):
        acc[i] = crescenteMemo(lista, i, acc)
    return max(acc.values())

def main():
    print("<h3>crescente</h3>")
    lista = [5, 2, 7, 4, 3, 8]
    print("in:", lista)
    print("out:", crescente2(lista))


if __name__ == '__main__':
    main()
'''

            lista = [5,2,7,4,3,8]
            self.assertEqual(crescente(lista),3)

            lista = [15,27,14,38,26,55,46,65,85]
            self.assertEqual(crescente(lista),6)'''