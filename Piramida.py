from sys import exit
from random import randint

class Pogon(object):
    # soba_mapa = Mapa('vhod')
    def __init__(self, soba_mapa):
        self.soba_mapa = soba_mapa

    def igraj(self):
        # Trenutna soba dolocimo kot Mapa('vhod').prvi_prizor() = Vhod()
        trenutna_soba = self.soba_mapa.prvi_prizor()
        # Zadnja_soba dolocimo Mapa('vhod').naslednja_soba('konec') = Konec()
        zadnja_soba = self.soba_mapa.naslednja_soba('konec')
        mrtva_soba = self.soba_mapa.naslednja_soba('mrtev')

        while trenutna_soba != zadnja_soba and trenutna_soba != mrtva_soba:
            # spremenljivki dolocimo Vhod().enter() = return 'hodnik'
            naslednja_soba_ime = trenutna_soba.enter()
            # trenutna_soba spremenimo Mapa('vhod').naslednja_soba(naslednja_soba_ime) = Hodnik()
            trenutna_soba = self.soba_mapa.naslednja_soba(naslednja_soba_ime)

        trenutna_soba.enter()

class Vhod(object):

    def enter(self):
        print("\nSi na vhodu v piramido in imas 3 mozne vhode levo, \n" +
        "desno ali naravnost.")

        vhod = input("Vpisi L, D ali N, da izberes vhod: ").lower()

        if vhod == 'l':
            print("\nStopil si skozi levi vhod. V vrat te je zadela, \n" +
            "strupena puscica in si umrl.")
            return 'mrtev'

        if vhod == 'd':
            print("\nNaredil si par korakov naprej in padel v past, kjer \n" +
            "si umrl")
            return 'mrtev'

        if vhod == 'n':
            print("\n\tIzbral si pravo pot in nadaljujes raziskovanje.\n")
            return 'hodnik'

class Hodnik(object):

    def enter(self):
        print("Po vstopu odkrijes dolg hodnik, ki se razcepi na 3 \n" +
        "mostove. Izberi pot, ki je lahko levo, desno ali naravnost.")

        pot = input("Vpisi L, D ali N, da izberes most: ").lower()

        if pot == 'l':
            print("\nIzbral si napacen most. Most se podre in pades v past.")
            return 'mrtev'

        if pot == 'n':
            print("\nIzbral si napacen most. Most se podre in pades v past.")
            return 'mrtev'

        if pot == 'd':
            print("\n\tIzbral si pravo pot in nadaljujes raziskovanje.\n")
            return 'soba1'



class Soba(object):

    def enter(self):
        print("Vstopil si v sobo kjer je levo sarkofag, naravnost je temen \n" +
        "predor in desno je predor prekrit s pajkovo mrezo. Izberi smer proti" +
        " cemu hoces iti.")

        smer = input("Vpisi L, D ali N, da izberes smer: ").lower()

        if smer == 'l':
            print("\nPriblizas se sarkofagu in iz njega skoci mumija, ki te ubije")
            return 'mrtev'

        if smer == 'd':
            print("\nIzbral si predor s pajkovo mrezo. Ven skoci strupen pajek,\n" +
            "ki te ubije.")
            return 'mrtev'

        if smer == 'n':
            print("\n\tIzbral si pravo pot in nadaljujes raziskovanje.\n")
            return 'zlata_soba'

class ZlataSoba(object):

    def enter(self):
        print("Vstopil si v zlatu sobo, kjer lahko izberes svojo nagrado. \n" +
        "Lahko vzames vso zlato ali skrivnosten amulet.")

        izbira = input("Vpisi Z, da vzames vso zlato, ali A za amulet: ").lower()

        if izbira == 'z':
            print("\nPiramida se zacne tresti in strop se zrusi na tebe in umres.")
            return 'mrtev'

        if izbira == 'a':
            print("\nVzel si amulet, ki ti podari moc vecnega zivljenja.")
            return 'konec'

class Konec(object):

    def enter(self):
        print("\n\tZ novim zakladom uspesno zapustis piramido. Zmagal si!\n")
        return 'konec'

class Mrtev(object):

    opcije = [
        "Vec srece prihodnjic.",
        "Uf mogoce poskusi katero drugo igro...",
        "F",
        "Opica bi znala premagat to igro..."
    ]

    def enter(self):
        print(Mrtev.opcije[randint(0, len(self.opcije)-1)])
        return 'mrtev'

class Mapa(object):

    sobe = {
        'vhod' : Vhod(),
        'hodnik' : Hodnik(),
        'soba1' : Soba(),
        'zlata_soba' : ZlataSoba(),
        'konec' : Konec(),
        'mrtev' : Mrtev()
    }

    # zacetek = 'vhod'
    def __init__(self, zacetek):
        self.zacetek = zacetek
    # vstavi parameter 'vhod'
    def naslednja_soba(self, ime_sobe):
        val = Mapa.sobe.get(ime_sobe)
        return val

    # vrne Vhod()
    def prvi_prizor(self):
        return self.naslednja_soba(self.zacetek)

    def izhod(self):
        exit(1)
