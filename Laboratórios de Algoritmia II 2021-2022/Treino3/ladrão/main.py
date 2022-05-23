"""
Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada,
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro.

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.
"""



def ladrao(capacidade, objetos):
    if capacidade == 0:
        return 0
    r = 0
    tmp = objetos.copy()
    for obj in objetos:
        if obj[2] <= capacidade:
            tmp.remove(obj)
            r = max(r,obj[1], ladrao(capacidade-obj[2], tmp))
    return r

def main():
    print("<h3>ladrao</h3>")
    objectos = [("microondas", 30, 6), ("jarra", 14, 3), ("giradiscos", 16, 4), ("radio", 9, 2)]
    print("in:", 10, objectos)
    print("out:", ladrao(10, objectos))


if __name__ == '__main__':
    main()
