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
'''


def main(h):
 c = first(h)
 while (c != None):
 if valid(h,c):
 return c
 c = next(h,c)


def main():
    print("<h3>amigos</h3>")
    conhecidos = {('pedro','maria'),('jose','francisca'),('pedro','pedro')}
    print("in:", conhecidos)
    print("out:", amigos(conhecidos))


if __name__ == '__main__':
    main()
