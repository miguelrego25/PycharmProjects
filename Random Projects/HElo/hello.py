'''
PYCHARM_DEBUG=True
def fw(adj):
    dist = {}
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


def tamanho(ruas):
    adj = {}
    maior = float("-inf")
    for rua in sorted(ruas, key=len, reverse=True):
        if rua[0] not in adj:
            adj[rua[0]] = {}

        if rua[-1] not in adj:
            adj[rua[-1]] = {}

        adj[rua[0]][rua[-1]] = len(rua)
        adj[rua[-1]][rua[0]] = len(rua)

    dists = fw(adj)
    for a in dists:
        for b in dists[a]:
            if dists[a][b] > maior:
                maior = dists[a][b]
    return maior

def main():
    print("<h3>tamanho</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:", ruas)
    print("out:", tamanho(ruas))
    '''
def main():
    print("2")
    print("Hello World")
    print(")")
    print("hell")
    return 0