def getVal(przedmioty, n):
    i = 0
    cena = 0
    waga = 0
    while n > 0:
        if(n % 2 == 1):
            cena += przedmioty[i][0]
            waga += przedmioty[i][1]
        i += 1
        n >>= 1
    return cena, waga

def PlecakSil(przedmioty, cel):
    n = len(przedmioty)
    wynikc = 0
    i = 0
    while i < 2**n:
        c, w = getVal(przedmioty, i)
        if w <= cel:
            if c >= wynikc:
                wynikc = c
        i += 1
    return wynikc