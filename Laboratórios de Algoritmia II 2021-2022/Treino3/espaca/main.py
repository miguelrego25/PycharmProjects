"""

Implemente uma função que, dada uma frase cujos espaços foram retirados,
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação),
a função recebe uma lista de palavras válidas a considerar na reconstrução
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.



def espaca(frase, palavras):
   return espacaRec(frase,palavras)[0]

def espacaRec(frase,palavras):
    dic = dict()
    dic[frase] = ['',0]
    #fazer uma lista com a frase[len(palavra):] e sacar a menor
    for palavra in palavras:
        if frase.startswith(palavra):
            if frase[len(palavra):] not in dic:
                lis = espacaRec(frase[len(palavra):], palavras)
                if lis[0] == '':
                    dic[frase[len(palavra):]] = [palavra,lis[1]+len(palavra)]
                else:
                    dic[frase[len(palavra):]] = [palavra + ' ' + lis[0], lis[1]+len(palavra)]
    print(dic.values())
    return max(dic.values(), key=lambda n: n[1])
"""


def espaca (frase, palavras):
    return espacarecursivo(frase, palavras,{})

def espacarecursivo(frase, palavras,dic):
    for palavra in frase:
        if frase.startswith(palavra):
            dic





def main():
    palavras = ["e", "o", "so", "maior", "este", "curso", "urso", "es", "maio"]
    espaca("estecursoeomaior",palavras)
    return espaca("estecursoeomaior",palavras)






'''testes
        with test_timeout(self,2):
           palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
            self.assertEqual(espaca("estecursoeomaior",palavras),"este curso e o maior")
                            este curso e o maior
        with test_timeout(self,2):
            palavras = ["o","oga","ga","gato","gatom","mia","eava","ava","e","a","va","vaca","mu","muge"]
            self.assertEqual(espaca("ogatomiaeavacamuge",palavras),"o gato mia e a vaca muge")'''
if __name__ == '__main__':
    main()