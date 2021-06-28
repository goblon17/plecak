from random import randint

przedmioty = []

n_tab = [5,10,15,20,25]

for n in n_tab:
    przedmioty = []
    for i in range(n):
        przedmioty.append([randint(1,20), randint(1,20)])
    
    file = open("przedmioty{:d}.txt".format(n), "w")
    for przedmiot in przedmioty:
        file.write("{} {}\n".format(przedmiot[0], przedmiot[1]))
    file.close()