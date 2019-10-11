def procura(caminho, raiz, destino, pai, cont):
    if raiz == destino:
        print(cont)
        return
    for pivo in caminho[raiz]:
        if pivo != pai:
            procura(caminho, pivo, destino, raiz, cont + 1)
entr1 = input().split()
dist = (int(entr1[0]))
caminho = {}
for i in range(dist):
    caminho[i + 1] = []
for j in range(dist-1):
    entr2 = input().split()
    caminho[int(entr2[0])].append(int(entr2[1]))
    caminho[int(entr2[1])].append(int(entr2[0]))
procura(caminho, int(entr1[1]), int(entr1[2]), None, 0)
