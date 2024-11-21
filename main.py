from Stadion import Stadion
import filebeolvas
import feladatok

stadionok=filebeolvas.beolvas("stadionok.txt", [])
for i in range(0,len(stadionok),1):
    print(stadionok[i])

db=feladatok.hany_newyorki(stadionok)
print(f"Ennyi New Yorki stadion van: {db}")

ossz=feladatok.osszcs(stadionok)
print(f"Az összes csapatszám: {ossz}******************************************")

print("Akiknek 1900.01.01. előtt volt mérkőzésük: ")
feladatok.ezerkilencszaz_elott(stadionok)

ota=feladatok.ketszazeve(stadionok)
print(f"Ennyi stadion nem játszott 200 éve: {ota}")

csapatok=feladatok.buffaloban(stadionok)
print(f"Ennyi csapat játszott Buffaloban: {csapatok}")

