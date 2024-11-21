from datetime import datetime

class Stadion:
    def __init__(self,nev:str="",varos:str="",csapatok_szama:int=0,elso_merk:str="",utolso_merk:str=""):
        self.nev=nev
        self.varos=varos
        self.csapatok_szama=int(csapatok_szama)
        #itt le kellene kezelni, ha nem számot kap akkor mivan?
        self.elso_merk=datetime.strptime(elso_merk, "%Y-%m-%d")
        self.utolso_merk=datetime.strptime(utolso_merk, "%Y-%m-%d")

    def __str__(self):
        return (f"Csapat neve: {self.nev}\n"
                f"Város: {self.varos}\n"
                f"Csapatok száma: {self.csapatok_szama}\n"
                f"Első mérkőzés: {self.elso_merk}\n"
                f"Utolsó mérkőzés: {self.utolso_merk}\n"
                f"*********************\n"
                f"\n")
    
