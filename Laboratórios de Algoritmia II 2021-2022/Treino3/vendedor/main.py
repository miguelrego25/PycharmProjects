# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""

Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção,
tem que escolher a melhor combinação de produtos a transportar dentro desse limite
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar,
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições,
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o               nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade
aos produtos que aparecem primeiro na lista de entrada.

"""

def vendedor(capacidade,produtos):
    listaporworth = calcularworth()
    return -1,[]

def calcularworth(capacidade,produtos,atual):
    list = []
    for (nome,valor,peso) in produtos:
        list =


def main():
    print("<h3>vendedor</h3>")
    produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]
    print("in:",14,produtos)
    print("out:",vendedor(14,produtos))


if __name__ == '__main__':
    main()