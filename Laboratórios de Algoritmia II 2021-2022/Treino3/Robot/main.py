"""

Implemente uma função que determina qual a probabilidade de um robot regressar
ao ponto de partido num determinado número de passos. Sempre que o robot dá um
passo tem uma determinada probabilidade de seguir para cima ('U'), baixo ('D'),
esquerda ('L') ou direita ('R'). A função recebe o número de passos que o
robot vai dar e um dicionário com probabilidades de se movimentar em cada uma
das direcções (as chaves são os caracteres indicados entre parêntesis).
O resultado deve ser devolvido com a precisao de 2 casas decimais.

"""

def probabilidade(passos,probs):
    dict = {}
    if passos == 0:
        return 1
    if passos%2 == 1:
        return 0
    dict = {(0,0):{0:1}}
    return round(probabilidadeaux(passos,probs,(0,0),dict),2)

def probabilidadeaux(passos,probs,coords,dict):
    if coords not in dict:
        dict[coords] = {0:0}
    if passos in dict[coords]:
        return dict[coords][passos]
    if passos == 0:
        if coords[0] == 0 and coords[1] == 0:
            return 1
        else:
            return 0
    dict[coords][passos] = probabilidadeaux(passos-1,probs,(coords[0],coords[1]+1),dict) * probs['U'] + probabilidadeaux(passos-1,probs,(coords[0],coords[1]-1),dict) * probs['D'] + probabilidadeaux(passos-1,probs,(coords[0]+1,coords[1]),dict) * probs['R'] + probabilidadeaux(passos-1,probs,(coords[0]-1,coords[1]),dict) * probs['L']
    return dict[coords][passos]



'''def test_probabilidade_1(self):
        with test_timeout(self,2):
            probs = {'U':0.25,'D':0.25,'L':0.25,'R':0.25}
            self.assertEqual(probabilidade(2,probs),0.25)
        
    def test_probabilidade_2(self):
        with test_timeout(self,2):
            probs = {'U':0.17,'D':0.33,'L':0.29,'R':0.21}
            self.assertEqual(probabilidade(6,probs),0.08)
    '''
def main():
    print("<h3>probabilidade</h3>")
    probs = {'U':0.17,'D':0.33,'L':0.29,'R':0.21}
    print("in:", 6, probs)
    print("out:", probabilidade(6, probs))


if __name__ == '__main__':
    main()
