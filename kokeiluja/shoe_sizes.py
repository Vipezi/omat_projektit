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

    kumpaan_tiedostoon = input("Haluatko lisätä nämä vanhaan csv tiedostoon vai luoda uuden? Vastaa 'vanhaan' tai 'uuteen'.")
    if kumpaan_tiedostoon == "vanhaan":
        tuotu_taulukko = muokkaa_csv()
        tuotu_taulukko[nimi] = tiedot
        print(tuotu_taulukko)
        tallennetaanko = input("Tallennetaanko päivitys? 'kyllä' tallentaa, muu vastaus jatkaa ohjelmaa. ")
        if tallennetaanko == "kyllä":
            tallenna_csv(tuotu_taulukko)
            print("")
        else:
            print("Ohjelma jatkuu.")
            print("")
    elif kumpaan_tiedostoon == "uuteen":
        tallenna_csv(taulukko)
        taulukko[nimi] = tiedot
        print(taulukko)

    else:
        print("Kokeile uudestaan. Näppäily virhe.")




def muokkaa_tietoja(taulukko):
    print("Tässä kaikkien nimet: ")
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

def tallenna_csv(taulukko):
    kysymys = input("Haluatko luoda kokonaan uuden tiedoston vai päivittää nykyisen tiedoston? Vastaa 'päivittää' tai 'luoda'. ")
    if kysymys == "päivittää":
        df = pd.DataFrame(taulukko).T
        print(df)
        df.to_csv('jalankasvu.csv')

    elif kysymys == "luoda":
        df = pd.DataFrame(taulukko).T
        print(df)
        df.to_csv('jalankasvu.csv')
    else:
        print("Taisi tulla näppäily virhe. Koita uudestaan.")

def muokkaa_csv():
    df = pd.read_csv("jalankasvu.csv").T
    df = df.to_dict()
    return df

def main():
    print("Kenkuliohjelma on tässä.")
    print("")
    taulukko = {}
    while True:
        print("")
        print("1. Kerro kuinka usein lapsen kenkä tulisi mitata.")
        print("2. Kerro kuinka paljon lapsen jalka kasvaa.")
        print("3. Lisää lapsi ohjelmaan.")
        print("4. Muokkaa lapsen tietoja, kuten ikää tai jalankokoa.")
        print("5. Tallenna csv tiedosto/taulukko")
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
            tallenna_csv(taulukko)
        elif valinta == "":
            break
        else:
            print("Näppäily virhe?. Koita uudestaan.")

if __name__ == "__main__":
    main()