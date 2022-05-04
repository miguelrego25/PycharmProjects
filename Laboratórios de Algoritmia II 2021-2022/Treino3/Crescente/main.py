"""

Implemente uma função que dada uma sequência de inteiros, determinar o
comprimento da maior sub-sequência (não necessariamente contígua) que se
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""

def crescente(lista):
    if lista == 0:
        return 0
    results = []
    for i in range(len(lista)):
        results.append(biggrz(lista[i:]))
    return max(results)

def biggrz(rtlista):
    x = []
    for i in range(len(rtlista)):
        if rtlista[0] < rtlista [i]:
            x.append(biggrz(rtlista[i:]))
    return 1+max([0] + x)


def main():
    print("<h3>crescente</h3>")
    lista = [5, 2, 7, 4, 3, 8]
    print("in:", lista)
    print("out:", crescente(lista))


if __name__ == '__main__':
    main()
'''

            lista = [5,2,7,4,3,8]
            self.assertEqual(crescente(lista),3)

            lista = [15,27,14,38,26,55,46,65,85]
            self.assertEqual(crescente(lista),6)'''