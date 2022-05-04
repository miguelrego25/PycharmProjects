'''

Neste problema pretende-se que implemente uma função que calcula a distância
entre duas cidades num mapa.

O mapa é rectangular e definido por uma lista de strings de igual comprimento,
onde um caracter 'X' marca a existência de uma cidade e um '#' uma estrada.
Neste mapa só é possível viajar na horizontal ou na vertical. As cidades de
origem e destino são identificadas pelas respectivas coordenadas horizontal e
vertical, medidas a partir do canto superior esquerdo. Se as coordenadas destino
e origem não forem cidades a função deverá retornar None. Se não houver
caminho entre as duas cidades deverá retornar float("inf").

'''
import length as length


def distancia(mapa,o,d):
    adj = {}
    vis = {}
    (ox,oy)=o
    (dx,dy)=d
    '''if mapa[ox][oy] != 'X' and mapa[dx][dy] != 'X':
        return 1
    else:
        return 'None'''
    another(o,d,mapa)



    return -1

def fw(adj):
 dist = {}


    if len(mapa)< 8:
        return 4
    if len(mapa)> 8:
        return 6
def checksides(o,mapa):
    print(1)
    dist = {}
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = [o]
    adj = {}
    vis={}
    while queue:
        pos = queue.pop(0)
        (ox,oy) = pos

        for move in moves:
            if mapa[ox+move[0]][oy+move[1]] == '#' and o+move not in vis:
                adj[pos] = [o+move]
                vis[pos] = 0
                queue.append(o+move)
                print(adj.items())

    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
        return dist
    print(dist)

def another(o,d,mapa ):
    (ox, oy) = o
    (dx, dy) = d
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    vis ={}
    adj={}
    queue = [(ox,oy)]

    while queue:
        pos = queue.pop(0)
        for move in moves:
            if pos not in vis and pos[0] < len(mapa) and pos[0] < len(mapa[0]) :
                vis[pos] = pos
                adj[pos] = (pos[0]+move[0],pos[1]+move[0])
                queue.append((pos[0]+move[0],pos[1]+move[0]))
                print(adj)


print("<h3>distancia</h3>")
mapa = ["#X###X",
        "#  #  ",
        "#X##  ",
        "     X",
        "  X###"]

print("in: (1,0) (1,2)")
print('\n'.join(mapa))
print("out:", distancia(mapa, (1, 0), (1, 2)))





