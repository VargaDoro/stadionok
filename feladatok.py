from datetime import datetime
def hany_newyorki(lista):
    db:int=0
    for i in range(0, len(lista), 1):
        if (lista[i].varos == "New York"):
            db += 1
    return db

def osszcs(lista):
    ossz:int=0
    for i in range(0, len(lista), 1):
        ossz+=lista[i].csapatok_szama
    return ossz

def ezerkilencszaz_elott(lista):
    datum=datetime.strptime("1900-01-01", "%Y-%m-%d")
    for i in range(0, len(lista), 1):
        if (lista[i].elso_merk < datum):
            elott = i
            print(lista[i])

def ketszazeve(lista):
    datum =datetime.strptime("1824-11-21", "%Y-%m-%d") 
    keresett:int = 0
    for i in range(0, len(lista), 1):
        if ( lista[i].utolso_merk > datum):
            keresett = i
    return keresett

def buffaloban(lista):
    csapatok:int=0
    for i in range(0, len(lista), 1):
        if lista[i].varos == "Buffalo":
            csapatok+=lista[i].csapatok_szama
    return csapatok

