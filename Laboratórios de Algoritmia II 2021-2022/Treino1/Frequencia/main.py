'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

'''Como resolver:
1- criar uma lista de tuplos (palavra, nº de ocurrencias)
2- a cada palavra ver se ela esta na lista caso contrario append da palavra a lista com nº de ocurrencias 0
3- fazer o sort das palavras por ordem alfabetica 
    
'''
def frequencia(texto):
 dic = {}
 iterador = 0;
 listatexto=texto.split()
 maior = 100000
 for x in listatexto:
     if x in dic:
         dic[x] += 1
     else:
         dic[x] = 1

 finalsortes = sorted(dic.items())
 finalsortes1 = sorted(finalsortes, key=lambda x: x[1], reverse=True)

 return finalsortes

def main():
    print("<h3>frequencia</h3>")
    texto = "o tempo perguntou ao tempo quanto tempo o tempo tem tel"
    print("in:",texto)
    print("out:",frequencia(texto))

if __name__ == '__main__':
    main()
