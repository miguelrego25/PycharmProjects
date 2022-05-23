
"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de
uma sequência de inteiros (também não vazia) com a maior soma. A função deve
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que
calcula o prefixo de uma sequência com a maior soma. Tendo essa função
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""


def maxsoma(lista):
    mx = lista[0]
    last = lista[0]
    for i in range(1, len(lista)):
        if last > 0:
            last += lista[i]
        else:
            last = lista[i]
        mx = max(last,mx)
    return mx

def main():
    print("<h3>maxsoma</h3>")
    lista = [1,2,3,4,-11,1,2,3,4,5]
    print("in:", lista)
    print("out:", maxsoma(lista))


if __name__ == '__main__':
    main()

'''
 for list in lists:
    check if sumlist < numero:
        return 0
    elif:
        
        
 
 '''