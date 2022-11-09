#! /usr/bin/python3
import pandas as pd

def mittaustarve():
    lapsen_ikä = input("Kerro lapsen ikä vuosissa: ")
    try:
        lapsen_ikä = int(lapsen_ikä)
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
        lapsen_ikä = int(lapsen_ikä)
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

def lisää_lapsi(taulukko):
    tiedot = {}
    nimi = input("Kerro lapsen nimi: ")
    ikäKK = int(input("Kerro lapsen ikä kuukausissa: "))
    jalankoko = float(input("Kerro lapsen tämän hetken jalankoko yhden yhden desimaalin tarkkuudella: "))
    tiedot["IkäKK"] = ikäKK
    tiedot["JalankokoCM"] = jalankoko
    ikä_vuosissa = ikäKK / 12

    if ikä_vuosissa < 4 :
        tiedot["Jalankasvu Vuodessa"] = "1,5-2mm/kk"
        tiedot["Mittausväli"] = "Joka 3.kk"
    elif ikä_vuosissa > 3 and ikä_vuosissa < 7:
         tiedot["Jalankasvu Vuodessa"] = "1,0mm/kk"
         tiedot["Mittausväli"] = "Joka 4.kk"
    elif ikä_vuosissa > 6 and ikä_vuosissa < 11 :
        tiedot["Jalankasvu Vuodessa"] = "< 1,0mm/kk"
        tiedot["Mittausväli"] = "Joka 5.kk"

    taulukko[nimi] = tiedot
    print(taulukko)




def muokkaa_tietoja(taulukko):
    print("Tässä kaikkie nimet: ")
    for k, v in taulukko.items():
        print(k)
    kenen_tiedot = input("Kenen tietoja haluat muokata? Käytä nimeä. ")
    if kenen_tiedot in taulukko.keys():
        uutta_vai_olemassa = input("Haluatko lisätä uutta tietoa vai muokata olemassa olevaa tieoa? Kirjoita 'uusi' uuden tiedon lisäämiseksi tai 'olemassa' päivittääksesi olemassa olevaa tietoa. ")
        if uutta_vai_olemassa == "olemassa":
            tieto = input("Muutatko jalankokoa vai ikää? Kirjoita 'ikä' tai 'koko'. ")

            if tieto == "koko":
                koko = float(input("Kerro uusi koko yhden desimaalin tarkuudella: "))
                taulukko[kenen_tiedot]["JalankokoCM"] = koko
                print(f"Päivitetyt tiedot: {taulukko[kenen_tiedot]}")

            elif tieto == "ikä":
                uusi_ikä = int(input("Kerro uusi ikä kuukausissa: "))
                taulukko[kenen_tiedot]["IkäKK"] = uusi_ikä
                print(f"Päivitetyt tiedot: {taulukko[kenen_tiedot]}")

            else:
                print("Näppäily virhe?. Koita uudestaan.")
        
        elif uutta_vai_olemassa == "uusi":
            määritys = input("Mitä tietoa haluat lisätä? Esimerkki: 'hiusväri', 'paino' tai 'pituus' ")
            yksikkö = input("Kirjoita tieto, joka lisätään: ")
            taulukko[kenen_tiedot][määritys] = yksikkö
            print(f"Lisätty tieto: {taulukko[kenen_tiedot]}")

        else:
            print("Näppäily virhe?. Koita uudestaan.")
    else:
        print("Henkilöä ei löydy. Koita ensiksi lisätä se.")

def luo_taulukko(taulukko):
    df = pd.DataFrame(taulukko)
    print(df)
    df.to_csv('jalankasvu.csv')



def main():
    print("Kenkuliohjelma on tässä.")
    taulukko = {}
    while True:
    
        print("1. Kerro kuinka usein lapsen kenkä tulisi mitata.")
        print("2. Kerro kuinka paljon lapsen jalka kasvaa.")
        print("3. Lisää lapsi ohjelmaan.")
        print("4. Muokkaa lapsen tietoja, kuten ikää tai jalankokoa.")
        print("5. Luo taulukosta csv tiedosto/taulukko")
        print("6. Poistu ohjelmasta.")
        print("")
        
        valinta = input("Paina vastaavaa numeroa tehdäksesi kyseisen toiminnon: ")
        if valinta == "1":
            mittaustarve()
        elif valinta == "2":
            jalankasvu()
        elif valinta == "3":
            lisää_lapsi(taulukko)
        elif valinta == "4":
            muokkaa_tietoja(taulukko)
        elif valinta == "5":
            luo_taulukko(taulukko)
        elif valinta == "6":
            break
        else:
            print("Näppäily virhe?. Koita uudestaan.")

if __name__ == "__main__":
    main()