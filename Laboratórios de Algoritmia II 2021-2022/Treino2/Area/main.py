'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical.

'''

#p sao as coordenadas de origem
#mapa sao as listas de strings que conteem os pontos e os asteriscos

def area(p,mapa):
    vis=[]
    area1(p,mapa,vis)
    print(vis)
    return len (vis)

def         area1(p,mapa,vis):
    x = p[0]
    y = p[1]
    vis.append(p)
    #if and x > -1 and x < 5 and y > -1 and y < 5:

    if x+1<5:
        if mapa[x+1][y] == '.' and (x+1,y) not in vis:
            area1((x+1,y),mapa,vis)
    if y+1<5:
        if mapa[x][y+1] == '.' and (x,y+1) not in vis:
           area1((x, y+1), mapa, vis)
    if x-1>0:
        if mapa[x - 1][y] == '.' and (x - 1, y) not in vis:
            area1((x-1, y), mapa, vis)
    if y-1>0:
        if mapa[x][y-1] == '.' and (x,y-1) not in vis:
            area1((x, y-1), mapa, vis)






def main():
    print("<h3>area</h3>")
    mapa = ["..*..",
            ".*.*.",
            "*....",
            ".*.*.",
            "..*.."]
    print("in:",(3,2))
    print('\n'.join(mapa))
    print("out:",area((3,2),mapa))

if __name__ == '__main__':
    main()

