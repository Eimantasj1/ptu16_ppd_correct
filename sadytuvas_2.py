import json

try:
    with open("fridge.json", "r+") as saldytuvas_dict:
        saldytuvas = json.load(saldytuvas_dict)
except:
    saldytuvas = {}
    with open("fridge.json", "w") as saldytuvas_dict:
        json.dump(saldytuvas, saldytuvas_dict)

class Saldytuvas:
    turinys = saldytuvas
    meniu = """
 1 - pridėti naują produktą 
 2 - papildyti produkto kiekį
 3 - ištraukti produktą nurodant kiekį
 4 - peržiūrėti produktus
 5 - ieškoti produktų
 6 - Suzinoti saldytuvo svori
 7 - Recepto patikrinimas (ar pakanka reikalingu produktu saldytuve) 
 0 - išėjimas
         """

    def meniu_pasirinkimas():
        print(Saldytuvas.meniu)

    def prideti(self, produktas, kiekis):
        self.turinys[produktas] = kiekis

    def papildyti(self) -> str | float :
        """Funkcija isves menu, kur bus parodyta lentele 
        su visais maisto produktais ir jiems priskirti 
        eiles numeriai
        """
        indeksas = 0

        print("Saldytuve yra tokie produktai: ", "\n")
        print(f"{'Nr.':3s} | {'Maisto produktas':15s} | {'Produkto kiekis':10s}", end="\n")
        for produktas in self:
            print(f"{indeksas+1:>3d} | {produktas:<16s} | {self[produktas]}")
            indeksas += 1

        pasirinktas_indeksas = int(input("Parasykite norimo produkto numeri: ")) -1
        prideti = int(input("Parasykite kiek norite prideti produkto: "))

        pasirinktas_produktas = self[pasirinktas_indeksas]
        self[pasirinktas_produktas] += prideti

        return self
    
    def istraukti(self, product:str, quantity:float):
        pass

    def perziureti(self):
        pass

    def ieskoti_produkta(self, product:str):
        pass

    def svoris(self):
        pass

    def receptas(self, product:str, quantity:float):
        pass

    def ijungti(self):
        
        Saldytuvas.meniu_pasirinkimas()
        while True:  
            pasirinkimas = input("Pasirinkite veiksma: ")
            if pasirinkimas == "0":
                with open("fridge.json", "w") as saldytuvas_json:
                    saldytuvas_json = json.dump(Saldytuvas.turinys, saldytuvas_json, indent=2)
                break
            elif pasirinkimas == "1":
                Saldytuvas.prideti(
                    produktas=input('Iveskite produkto pavadinima'), kiekis=float(input('Iveskite kieki'))
                    )
#             elif pasirinkimas == "2":
#                 saldytuvas = papildyti(saldytuvas)
#             elif pasirinkimas == "3":
#                 saldytuvas = istraukti(saldytuvas)
#             elif pasirinkimas == "4":
#                 perziureti(saldytuvas)
#             elif pasirinkimas == "5":
#                 produktas = input("Koki produkta ieskote? ")
#                 ieskoti_produkta(produktas, saldytuvas)
#             elif pasirinkimas == "6":
#                 print(f'Bendras produktu svoris: {skaiciuoti(saldytuvas)} kg.')
            elif pasirinkimas == "7":
                receptas = {}
                while True:
                    produktas = input('Iveskite produkta , arba "0", jeigu norite baigti.')
                    if produktas == '0':
                        with open("saldytuvas.json", "w") as saldytuvas_json:
                            saldytuvas_json = json.dump(Saldytuvas.turinys, saldytuvas_json, indent=2)
                        break
                    kiekis = input('Iveskite kieki')
                    receptas[produktas] = float(kiekis)
                ar_iseina(saldytuvas, receptas)

Saldytuvas.ijungti()    