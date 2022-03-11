'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    dic={}
    finallist=[]

    for x in nomes:
        dic[x] = len(list(x.split()))

    pil1 = sorted(dic.items())
    pil  = sorted(pil1,key=lambda x: x[1], reverse=False )

    for i in pil:
        finallist.append(i[0])
    return finallist



def main():
    print("<h3>apelidos</h3>")
    nomes = ["Jose Carlos Bacelar Almeida",
             "Maria Joao Frade",
             "Jose Bernardo Barros",
             "Jorge Sousa Pinto",
             "jose alcino Pereira Cunha",
             "Xico Esperto"]
    print("in:",nomes)
    print("out:",apelidos(nomes))

if __name__ == '__main__':
    main()
#https://careerkarma.com/blog/python-sort-a-dictionary-by-value/
#https://docs.python.org/3/howto/sorting.html