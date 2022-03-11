def robot(comandos):
    dic = {"N": 0, "S": 0, "E": 0, "O": 0}
    keyy = 'Y'
    key = 'N'
    flag = 0
    finallist = []
    actualdic = {'X': 0, 'Y': 0}

    for i in range(len(comandos)):
        if comandos[i] == 'A':
            if flag == 1:
                actualvalue(dic, actualdic, key)
                flag = 0
            dic[key] += 1
            if key == 'N':
                actualdic[keyy] += 1
            elif key == 'S':
                actualdic[keyy] -= 1
            elif key == 'E':
                actualdic[keyy] += 1
            elif key == 'O':
                actualdic[keyy] -= 1
        if comandos[i] == 'E':
            flag = 1
            key = keynext(key, 'esq')
            keyy = nextkey(keyy)
        if comandos[i] == 'D':
            flag = 1
            key = keynext(key, 'dir')
            keyy = nextkey(keyy)
        if comandos[i] == 'H':
            flag = 0
            key = 'N'
            finallist.append(apenndlist(dic))
            dic = {"N": 0, "S": 0, "E": 0, "O": 0}
            print (actualdic.items())
            actualdic = {'X': 0, 'Y': 0}
    return finallist

def nextkey(key):
    if key == 'X':
        return 'Y'
    if key == 'Y':
        return 'X'
def actualvalue (dicc, actualdic ,key):
    if key == 'N':
        dicc[key] += actualdic['Y']
    if key == 'S':
        dicc[key] += actualdic['Y']
    if key == 'O':
        dicc[key] += actualdic['X']
    if key == 'E':
        dicc[key] += actualdic['X']


def apenndlist (dic):
    a = ((dic['O']), (dic['S']), (dic['E']), (dic['N']))
    return a


def keynext(orientacao,mudanca):
    if orientacao == 'N' and mudanca == 'dir':
        return 'E'
    if orientacao == 'N' and mudanca == 'esq':
        return 'O'
    if orientacao == 'E' and mudanca == 'dir':
        return 'S'
    if orientacao == 'E' and mudanca == 'esq':
        return 'N'
    if orientacao == 'S' and mudanca == 'dir':
        return 'O'
    if orientacao == 'S' and mudanca == 'esq':
        return 'E'
    if orientacao == 'O' and mudanca == 'dir':
        return 'N'
    if orientacao == 'O' and mudanca == 'esq':
        return 'S'




def main():
    print("<h3>robot</h3>")
    cs = "EEAADAAAAAADAAAADDDAAAHAAAH"
    print("in:",cs)
    print("out:",robot(cs))

if __name__ == '__main__':
    main()
