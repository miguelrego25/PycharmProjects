
def saltos(o, d):
    dic = {}
    queue = [o]
    vis = {o}
    moves = [(2, 1), (1, 2), (-2, 1), (2, -1), (-2, -1), (-1, 2), (1, -2), (-1, -2)]

    while queue:
        v = queue.pop(0)
        if v == d:
            break
        if v not in dic:
            dic[v] = 0
        for move in moves:
            pos = (v[0] + move[0], v[1] + move[1])
            print(pos)
            if pos not in vis:
                vis.add(pos)
                dic[pos] = dic[v] + 1
                queue.append(pos)
    return dic[d]

def main ():
    print("<h3>saltos</h3>")
    print("in: (0,0) (1,1)")
    print("out:", saltos((0, 0), (1, 1)))
    return
