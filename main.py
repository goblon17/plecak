from plecak_sil import PlecakSil
from plecak_rek import PlecakRek
from plecak_dyn import PlecakDyn
from timeit import default_timer as timer

def pomierz(f, przed, n):
    start = timer()
    f(przed, n)
    end = timer()
    return (end-start)*1000

n_tab = [5,10,15,20,25]
cel = 15
przedmioty = []

for n in n_tab:
    del przedmioty[:]
    file = open("przedmioty{:d}.txt".format(n), "r")
    for lin in file:
        c,w = map(int, lin.split())
        przedmioty.append([c,w])
    file.close()

    print("{:d} silowy: {:f}.ms".format(n, pomierz(PlecakSil,przedmioty,cel)))
    print("{:d} rekure: {:f}.ms".format(n, pomierz(PlecakRek,przedmioty,cel)))
    print("{:d} dynami: {:f}.ms".format(n, pomierz(PlecakDyn,przedmioty,cel)))

cele = [10,15,20,25,30,40,50]

for ncel in cele:
    del przedmioty[:]
    file = open("przedmioty{:d}.txt".format(10), "r")
    for lin in file:
        c,w = map(int, lin.split())
        przedmioty.append([c,w])
    file.close()

    print("{:d} silowy: {:f}.ms".format(10, pomierz(PlecakSil,przedmioty,ncel)))
    print("{:d} rekure: {:f}.ms".format(10, pomierz(PlecakRek,przedmioty,ncel)))
    print("{:d} dynami: {:f}.ms".format(10, pomierz(PlecakDyn,przedmioty,ncel)))