'''

Implemente uma função que calcula quantas sequências de n bits existem onde
não aparecem dois 1s seguidos.

Sugere-se que começe por definir uma função recursiva que calcula quantas
sequências de n bits começadas por um dado bit existem onde não aparecem
dois 1s seguidos.

'''

'''
        main criar uma lista vazia onde vamos fazer apppend
        criar uma lista com todos os elementos
        
    '''
def binarioaux(n, last):
    if n>0:
        if last == 0:
            return binarioaux(n-1, 1) + binarioaux(n-1, 0)
        elif last == 1:
            return binarioaux(n-1, 0)
    if n == 0 and last == 1:
        print(last)
        return 1
    elif n == 0 and last == 0:
        print(last)
        return 1

def binario(n):
    m = binarioaux(n-1, 1) + binarioaux(n-1, 0)
    print(m)
    return m



'''
    return len(finallist[0]) + len(finallist[1])

def binarioaux(n,last,):
    if n == 0 and last == 1:
        print(n)
        return 1
    if n == 0 and last == 0:
        print(n)
        return 1
    if last == 1:
        binarioaux(n-1, last-1)
    elif last == 0:
        binarioaux(n-1, last+1)
        binarioaux(n-1, last)




def binarioaux(n,last,seq):
    if n == 0 and last == 1:
        seq.append(1)
        print(seq)

        return 1
    if n == 0 and last == 0:
        seq.append(0)
        print(seq)
        return 1
    if last == 1:
        binarioaux(n-1, 1, seq.append(1))
    if last == 0:
        binarioaux(n-1, 0, seq.append(0))
        binarioaux(n-1, 1, seq.append(0))


'''



'''
def binario(n):
    lista = list(range(0,n))
    last = 0
    listseq = []
    for l in lista:
        listseq.append(binarioaux(n-1, 0, []))
        listseq.append(binarioaux(n-1, 1, []))
    print(listseq)
    
def binarioaux(n, last, seq):
    if last == 0 and n == 0:
        seq.append(0)
        print(seq)
        return seq
    elif last == 1 and n == 0:
        seq.append(1)
        return seq
    elif last == 1:
        seq.append(1)
        binarioaux(n-1, last-1,seq)
    elif last == 0:
        seq.append(0)
        binarioaux(n-1, last+1,seq)
        binarioaux(n-1, last,seq)

'''






def main():
    print("<h3>binario</h3>")

    print("binario(5) =", binario(4))







if __name__ == '__main__':
    main()

''' def test_binario_0(self):
        with test_timeout(self,1):
            self.assertEqual(binario(5),13)

    def test_binario_1(self):
        with test_timeout(self,1):
            self.assertEqual(binario(10),144)'''
