def PlecakGo(przedmioty, cel, n):
    if n == 0 or cel == 0:
        return 0
    if (przedmioty[n-1][1] > cel):
        return PlecakGo(przedmioty, cel, n-1)
    else:
        return max(przedmioty[n-1][0] + PlecakGo(przedmioty, cel - przedmioty[n-1][1], n-1), PlecakGo(przedmioty, cel, n-1))

def PlecakRek(przedmioty, cel):
    return PlecakGo(przedmioty, cel, len(przedmioty))