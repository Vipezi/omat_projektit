#! /usr/bin/python3
import pandas as pd

def mittaustarve():
    lapsen_ikä = input("Kerro lapsen ikä vuosissa: ")
    try:
        int(lapsen_ikä)
        if lapsen_ikä < 4:
            print("Lapsen jalka tulisi mitata joka 3. kk, eli noin 4 kertaa vuodessa.\n")
        elif lapsen_ikä > 3 and lapsen_ikä < 7:
            print("Lapsen jalka tulisi mitata joka 4. kk, eli noin 3 kertaa vuodessa.\n")
        elif lapsen_ikä > 6 and lapsen_ikä < 11:
            print("Lapsen jalka tulisi mitata joka 5. kk, eli noin 2 kertaa vuodessa.\n")
        else:
            print("Tämän ikäluokan lapsista en osaa sanoa. Tämä ohjelma on tarkoitettu 1-10 vuotiaille lapsille.")
    except ValueError as e:
        print("Vastaa kysymykseen numeroilla kiitos!")

def jalankasvu():
    lapsen_ikä = input("Kerro lapsen ikä vuosissa: ")
    try:
        int(lapsen_ikä)
        if lapsen_ikä < 4:
            print("Lapsen jalka kasvaa noin 1,5-2mm/kk.\n")
        elif lapsen_ikä > 3 and lapsen_ikä < 7:
            print("Lapsen jalka kasvaa noin 1,0mm/kk.\n")
        elif lapsen_ikä > 6 and lapsen_ikä < 11:
            print("Lapsen jalka kasvaa noin  < 1,0mm/kk.\n")
        else:
            print("Tämän ikäluokan lapsista en osaa sanoa. Tämä ohjelma on tarkoitettu 1-10 vuotiaille lapsille.")
    except ValueError as e:
        print("Vastaa kysymykseen numeroilla kiitos!")

def lisää_lapsi():
    rivi = []
    nimi = input("Kerro lapsen nimi: ")
    rivi.append(nimi)
    ikä = input("Kerro lapsen ikä: ")
    rivi.append(ikä)
    koko = input("Kerro lapsen jalan koko: ")
    rivi.append(koko)
    rivi = 
    taulukko = pd.DataFrame()
    taulukko = taulukko.merge(rivi)
    
  









def main():
    print("Kenkuliohjelma on tässä.")
    while True:
    
        print("1. Kerro kuinka usein lapsen kenkä tulisi mitata.")
        print("2. Kerro kuinka paljon lapsen jalka kasvaa.")
        print("3. Lisää lapsi ohjelmaan.")
        print("4. Muokkaa lapsen tietoja, kuten ikää tai jalankokoa.")
        print("5. Poistu ohjelmasta.")
        print("")
        
        valinta = input("Paina vastaavaa numeroa tehdäksesi kyseisen toiminnon: ")
        if valinta == "1":
            mittaustarve()
        elif valinta == "2":
            jalankasvu()
        elif valinta == "3":
            lisää_lapsi()

if __name__ == "__main__":
    main()