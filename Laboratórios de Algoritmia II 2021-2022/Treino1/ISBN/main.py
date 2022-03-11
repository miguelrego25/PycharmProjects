'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos.
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos,
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''
import math
def isbn(livros):
    dic = {}
    livroslist = livros.items()
    listsemcontrolo = []
    for a,b in livroslist:
        dic[a] = 0

    for a,b in livroslist:
        c=list(map(int, list(str(b))))
        digitcotrolo = c.pop()
        indice =0
        #calcular o valor do numero sem o digito de controlo
        for numero in c:
            if indice % 2 == 0:
                dic[a] += numero * 3
            else:
                dic[a] += numero
            indice=indice+1

        dic[a] = dic[a] - (math.floor(dic[a]/10))*10

        if dic[a] == digitcotrolo:
            dic[a] = "valido"
        else:
            dic[a] = "invalido"

        x = dic.items()
        finalist = []
        for a,b in x:
            if b == "valido":
                continue
            if b == "invalido":
                finalist.append(a)

        x= sorted(finalist, key = lambda x:x[0])




    return finalist

  #  (9*1)+(7*3)+(8*1)+(9*3)+(7*1)+(2*3)+(2*1)+(0*3)+(3*1)+(6*3)+(7*1)+(5*3) 7
  #  (9*1)+(7*3)+(8*1)+(9*3)+(8*1)+(9*3)+(6*1)+(6*3)+(0+1)+(4*3)+(0*1)+(1*3) 1
def main():
    print("<h3>isbn</h3>")
    livros = livros = {

        "Ensaio sobre a cegueira":"9789896604011"

    }
    print("in:",livros)
    print("out:",isbn(livros))

if __name__ == '__main__':
    main()

#