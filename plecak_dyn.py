def PlecakDyn(przedmioty, cel):
    n = len(przedmioty)
    tab = [[0 for i in range(cel+1)] for n in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, cel+1):
            if przedmioty[i-1][1] <= j:
                tab[i][j] = max(przedmioty[i-1][0] + tab[i-1][j - przedmioty[i-1][1]], tab[i-1][j])
            else:
                tab[i][j] = tab[i-1][j]
    return tab[n][cel]