'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade:
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade,
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a
letras do alfabeto, e cada rua começa (e acaba) no cruzamento
identificado pelo primeiro (e último) caracter do respectivo nome.

'''


def tamanho(ruas):
    return -1

def main():
    print("<h3>tamanho</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:", ruas)
    print("out:", tamanho(ruas))
