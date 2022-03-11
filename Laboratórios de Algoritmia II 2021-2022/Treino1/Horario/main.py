"""

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

"""

def horario(ucs,alunos):
    ucss= ucs.items()
    alunoss = alunos.items()
    dds = (list(range(5)))

    for dia in dds:
        



    return dds



##
# Main function of the Python program.
#
##


def main():
    print("<h4>horario</h4>")
    ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1), "cp": ("terca",14,2),"so": ("quinta",9,3)}
    alunos = {5000: {"la2","cp"}, 2000: {"la2","cp","pi"},3000: {"cp","poo"}, 1000: {"la2","cp","so"}}
    print(horario(ucs,alunos))

if __name__ == '__main__':
    main()
