
"""
Classe: Soldat
Objet : chaque soldat
Attribut : Attaque, vie...
"""

hdv=1

class Unite():
    soldats_crees = 0
    archers_crees = 0

    def __init__(self, type):
        soldats_crees = 0
        archers_crees = 0

        if type=="soldat":
            print("Création d'un soldat...")
            self.vie=4
            self.attaque=3
            Unite.soldats_crees+=1

        elif type=="archer":
            print("Création d'un archer...")
            self.vie=2
            self.attaque=5
            Unite.archers_crees+=1
    
S1=Unite("soldat")
A1=Unite("archer")
A2=Unite("archer")

print(A1.attaque)
print(S1.attaque)

print("Nombre de soldats crées : {}, et nombre d'archers crées : {}".format(Unite.soldats_crees, Unite.archers_crees))
